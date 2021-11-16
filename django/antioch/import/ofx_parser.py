# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 20:09:22 2021

@author: marcu
"""

import re
from datetime import datetime

def get_xml_block(text, block_tag):
    pattern = re.compile(
        f"<{block_tag}>(.*?)</{block_tag}>", re.DOTALL)
    matches = re.findall(pattern, text)
    if len(matches) == 0:
        return None
    elif len(matches) == 1:
        return matches[0]
    else:
        return matches

def parse_date(date, date_only = True):
    """ Parse dates of format 20210804000000 """
    if date is None: return
    dtime = datetime.strptime(date, "%Y%m%d%H%M%S")
    if date_only:
        return dtime.date()
    else:
        return dtime

class OFX:
    def __init__(self, filename = None):
        # if filename is None, create a blank OFX object which can be
        # populated with import_raw later
        if filename is None:
            self.filename = None
            self.text = None
            return

        self.filename = filename
        self.import_file(filename)
        self._parse()

    def import_raw(self, text):
        self.text = str(text)
        self._parse()
        return self

    def import_file(self, filename):
        with open(filename) as f:
            text = f.read()
        self.text = text
        self._parse()
        return self

    def _parse(self):
        if self.text is None:
            raise AttributeError

        # Parse headers
        headers = ["OFXHEADER", "DATA", "VERSION", "SECURITY", "ENCODING",
                   "CHARSET", "COMPRESSION", "OLDFILEUID", "NEWFILEUID"]
        for attr in headers:
            pattern = re.compile(f"^.*?\n?{attr}:(?P<value>.*?)\n.*$",
                                 flags = re.DOTALL)
            match = re.match(pattern, self.text)
            if match is None:
                self.__dict__[attr.lower()] = None
            else:
                self.__dict__[attr.lower()] = match["value"]

        self.signon_messages = SignOnMessages(
            get_xml_block(self.text, "SIGNONMSGSRSV1"))

        self.bank_messages = BankMessages(
            get_xml_block(self.text, "BANKMSGSRSV1"))

        self.transactions = self.bank_messages.transactions

class Status:
    def __init__(self, text):
        self.text = text
        tags = ["CODE", "SEVERITY"]
        for tag in tags:
            self.__dict__[tag.lower()] = get_xml_block(text, tag)

class SignOnMessages:
    def __init__(self, text):
        self.text = text
        if text is None: return
        self.sonrs = get_xml_block(text, "SONRS")
        self.status = Status(get_xml_block(self.sonrs, "STATUS"))
        self.server_date = parse_date(get_xml_block(self.sonrs, "DTSERVER"))
        self.language = get_xml_block(self.sonrs, "LANGUAGE")
        self.intu_bid = get_xml_block(self.sonrs, "INTU.BID")

class BankMessages:
    def __init__(self, text):
        self.text = text
        # Statement transaction response
        self.stmttrnrs = get_xml_block(text, "STMTTRNRS")
        self.trnuid = get_xml_block(self.stmttrnrs, "TRNUID")
        self.status = Status(get_xml_block(text, "STATUS"))

        # Statement response
        self.stmtrs = get_xml_block(self.stmttrnrs, "STMTRS")
        self.currency = get_xml_block(self.stmtrs, "CURDEF")
        self.bank_account = BankAccount(
            get_xml_block(self.stmtrs, "BANKACCTFROM"))

        self.transactions = Transactions(
            get_xml_block(self.stmtrs, "BANKTRANLIST"))

class Transactions:
    def __init__(self, text):
        self.text = text
        self.date_start = parse_date(get_xml_block(text, "DTSTART"))
        self.date_end = parse_date(get_xml_block(text, "DTEND"))
        self.transactions = [
            Transaction(trns) for trns in get_xml_block(text, "STMTTRN")
            ]
        self.count = len(self.transactions)

    def __iter__(self):
        self._i = -1
        return self

    def __next__(self):
        if self._i < self.count - 1:
            self._i += 1
            return self.transactions[self._i]
        else:
            raise StopIteration

class BankAccount:
    def __init__(self, text):
        self.text = text
        tags = ["BANKID", "ACCTID", "ACCTTYPE"]
        for tag in tags:
            self.__dict__[tag.lower()] = get_xml_block(text, tag)

class Transaction:
    def __init__(self, text):
        self.text = text
        self.type = get_xml_block(text, "TRNTYPE")
        self.date_posted = parse_date(get_xml_block(text, "DTPOSTED"))
        self.amount = float(get_xml_block(text, "TRNAMT"))
        self.fit_id = get_xml_block(text, "FITID")
        self.counter_party = get_xml_block(text, "NAME")
        self.reference = get_xml_block(text, "MEMO")

if __name__ == "__main__":
    filename = r"D:\Users\Marcus\Downloads\TransactionHistory (1).ofx"
    ofx = OFX(filename = filename)
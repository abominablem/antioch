# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 22:49:41 2021

@author: marcu
"""
import pandas as pd
import ofx_parser as ofxp
import functions as f
from sqlite_database import TableCon

transactions_db = TableCon(db = r'.\sqlite_db\transactions.db',
                           table = 'transactions',
                           debug = True)

class TransactionHandler:
    def __init__(self):
        return

    def add_transaction(self, transaction):
        if not isinstance(transaction, ofxp.Transaction):
            raise ValueError("transaction is not instance of Transaction "
                             "class")
        transactions_db.add_row(**transaction.__dict__)

    def get_transactions(self, columns = "*", **filters):
        results = transactions_db.filter(filters, columns)
        return results

    def import_transactions(ofx):
        if not isinstance(ofx, ofxp.OFX):
            raise ValueError("ofx is not instance of OFX class")
    
        transactions = ofx.bank_messages.transactions.transactions
        attributes = transactions[0].__dict__.keys()
    
        attribute_dict = {}
        for attr in attributes:
            attribute_dict[attr] = f.get_class_attr(transactions, attr)
    
        df = pd.DataFrame.from_dict(attribute_dict)
        return df

if __name__ == "__main__":
    filename = r"D:\Users\Marcus\Downloads\TransactionHistory.ofx"
    ofx = ofxp.OFX(filename = filename)
    # df = import_transactions(ofx)
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 22:49:41 2021

@author: marcu
"""
import pandas as pd
from ofx_parser import OFX

def get_class_attr(instances, attr):
    attributes = []
    for instance in instances:
        attributes.append(instance.__dict__[attr])
    return attributes

def import_transactions(ofx):
    if not isinstance(ofx, OFX):
        raise ValueError("ofx is not instance of OFX class")

    transactions = ofx.bank_messages.transactions.transactions
    attributes = transactions[0].__dict__.keys()

    attribute_dict = {}
    for attr in attributes:
        attribute_dict[attr] = get_class_attr(transactions, attr)

    df = pd.DataFrame.from_dict(attribute_dict)
    return df


ofx = OFX(r"D:\Users\Marcus\Downloads\TransactionHistory.ofx")

df = import_transactions(ofx)
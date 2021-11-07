# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 00:21:15 2021

@author: marcu
"""

def get_class_attr(instances, attr):
    attributes = []
    for instance in instances:
        attributes.append(instance.__dict__[attr])
    return attributes
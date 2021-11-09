# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 20:03:55 2021

@author: marcu
"""

from django.db import models

class Transactions(models.Model):
    fit_id = models.CharField(max_length = 255)
    date_posted = models.DateField()
    date_entered = models.DateField()
    counter_party = models.CharField(max_length = 255)
    reference_text = models.CharField(max_length = 255)
    type = models.CharField(max_length = 255)
    amount = models.FloatField()
    date_inserted = models.DateField()
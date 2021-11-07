# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 22:48:18 2021

@author: marcu
"""
import tkinter as tk
from tkinter import ttk
import arrange_widgets as aw
import described_widgets as dw
from mh_logging import Logging
from datetime import datetime

log = Logging()

class Antioch:
    def __init__(self, trace = None):
        log(self, "__init__", trace)
        self.root = tk.Tk()
        self.name = self.__class__.__name__

        self.testing_mode = True
        self.running = True
        self.start_time = datetime.now()
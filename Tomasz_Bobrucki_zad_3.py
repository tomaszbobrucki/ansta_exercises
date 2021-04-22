# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 15:48:07 2021

@author: Tomek
"""

from decimal import Decimal
import numpy as np


def zad_3():
    #option_1
    list_decimals_1 = [Decimal(num/2) for num in range(4, 12)]
    #option_2
    list_decimals_2 = np.linspace(2.0,5.5,8)
    #option_3
    list_decimals_3  = np.arange(2.0, 6.0, 0.5)
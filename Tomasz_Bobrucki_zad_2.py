# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 23:53:29 2021

@author: Tomek
"""


def zad_2():
    begin = input()
    list_1 = begin[:(begin.index("]") + 1)]
    count = int(begin[begin.index("]") + 3:])
    print('[' + ','.join(str(num) for num in range(1, count + 1) if str(num) not in list_1) + ']')
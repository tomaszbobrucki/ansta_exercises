# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 15:28:54 2021

@author: Tomek
"""


def zad_1():
    while True:
        str1 = input("Please insert first postcode: ('XX-XXX'): ")
        if len(str1) != 6 or str1[2] != "-":
            print("Wrong postcode format!")
        else:
            break
    while True:
        str2 = input("Please insert second postcode: ('XX-XXX'): ")
        if len(str2) != 6 or str2[2] != "-":
            print("Wrong postcode format!")
        else:
            break
    num_str1 = int(str1[:2]+str1[3:]) 
    num_str2 = int(str2[:2]+str2[3:])  
    for x in range(num_str1, num_str2 + 1):
        new = str(x)
        print(new[:2] + "-" + new[2:])
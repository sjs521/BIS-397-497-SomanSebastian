#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 15:46:14 2020

@author: sebastian_soman
"""
# Score: 21/25
# This function was supposed to work on any list of numbers but
# be tested on 10 random numbers. Instead, you have hard-coded
# it to work on only 10 numbers.
import statistics

def descriptive():
    values = []
    for value in range (0,10):
        values.append(int(input("Enter Value: ")))
    total = sum(values)
    median = statistics.median(values)
    ssd = statistics.stdev(values)
    psd = statistics.pstdev(values)
    print(f'Mean is: {total}\n')
    print(f'Median is: {median}\n')
    print(f'Sample Standard Deviation is: {ssd}\n')
    print(f'Population Standard Deviation is: {psd}') 

descriptive()


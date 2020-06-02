#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 17:12:41 2020

@author: sebastian_soman
"""

max1 = 0
max2 = 0

for number in range(0, 10):
    x = int(input('Enter an integer: '))
    if x > max1:
        max1 = x
    if max1 > max2:
        x = max2
        max2 = max1
        max1 = x
        
print('The largest number is', max2)
print('The second largest number is', max1)
        
        
        
    
    
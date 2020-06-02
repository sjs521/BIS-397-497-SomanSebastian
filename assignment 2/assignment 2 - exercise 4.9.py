#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 15:37:48 2020

@author: sebastian_soman
"""

#conversion formula
def fahrenheit(celsius):
    return round((9 / 5) * celsius + 32, 1)

print('Celsius Fahrenheit')
for celsius in range (1, 101):
    print(f'{celsius:<2}\t', fahrenheit(celsius))




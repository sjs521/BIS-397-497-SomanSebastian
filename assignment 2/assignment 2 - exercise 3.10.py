#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 16:35:41 2020

@author: sebastian_soman
"""


# Reimplement Exercise 2.12 to use a loop that calculates 
# and displays the amount of money 
# you’ll have each year at the ends of years 1 through 30
principal = 1000
rate = .07

for year in range(1, 31):
    amount = principal * (1 + rate) ** year
    print(f'{year:>2}{amount:>10.2f}')
    
    
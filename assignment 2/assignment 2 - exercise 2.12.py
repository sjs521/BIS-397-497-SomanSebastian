#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 18:30:42 2020

@author: sebastian_soman
"""

p=1000
r=.07

#Amount on deposit after 10 years
n=10
amount=p*(1+r)**n
final_amount="${:,.2f}".format(amount)
print(f'Amount after 10 years: {final_amount}')

#Amount on deposit after 20 years
n=20
amount=p*(1+r)**n
final_amount="${:,.2f}".format(amount)
print(f'Amount after 20 years: {final_amount}')

#Amount on deposit after 30 years
n=30
amount=p*(1+r)**n
final_amount="${:,.2f}".format(amount)
print(f'Amount after 30 years: {final_amount}')










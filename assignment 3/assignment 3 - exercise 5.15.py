#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 17:08:03 2020

@author: sebastian_soman
"""

from operator import itemgetter

invoice_tuples = [(83, 'Electric sander', 7, 57.98),
                  (24, 'Power saw', 18, 99.99),
                  (7, 'Sledge Hammer', 11, 21.50),
                  (77, 'Hammer', 76, 11.99),
                  (39, 'Jig saw', 3, 79.50)]

# part a:
print(sorted(invoice_tuples, key=itemgetter(1)))

# part b:
print(sorted(invoice_tuples, key=itemgetter(3)))

# part c:
c_tuple = ()
for item in invoice_tuples:
    y = ((item[1]), item[2])
    c_tuple = c_tuple + (y,)
print(sorted(c_tuple,key=itemgetter(1)))

# part d
d_tuple = ()
for item in invoice_tuples:
    a = ((item[1]),item[2]*item[3])
    d_tuple = d_tuple + (a,)
print(sorted(d_tuple,key=itemgetter(1)))

# part e
for item in d_tuple:
    if item[1] >= 200 and item[1] <= 500:
        print(item)

# part f
total = 0
for item in d_tuple:
    total += item[1]
print(total)
    
    
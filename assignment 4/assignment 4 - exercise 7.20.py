#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 20:16:15 2020

@author: sebastian_soman
"""

import random
import numpy
import timeit # I wasn't getting the exact output in the chart from the textbook
              # so I referred to the internet and found this to work rather than %timeit

values = [10**x for x in range(0,7)]
def list_test(size):
   test = []
   for i in range(size):
       test.append(random.randint(0,7))

def array_test(size):
   test = numpy.random.rand(size)

print("Number of values\t\tList average execution time\tArray average execution time")
for i in values:
  
   list_timer = timeit.Timer(lambda: list_test(i))
   array_timer = timeit.Timer(lambda: array_test(i))
   print(f"{i}\t\t\t\t\t{list_timer.timeit(5)}\t\t\t{array_timer.timeit(5)}")

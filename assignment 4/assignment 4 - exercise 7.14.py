#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 20:03:13 2020

@author: sebastian_soman
"""


import numpy as np

array1 = np.array([[0, 1], [2, 3]])
array2 = np.array([[4, 5], [6, 7]])
array1
array2
# part a: vstack array1 on top of array2
array3 = np.vstack((array1, array2))
array3

# part b: hstack with array2 to the right of array1
array4 = np.hstack((array1, array2))
array4

# part c: Use vertical stacking with two copies of array4 to create a 4-by-4 array5
array5 = np.vstack((array4, array4))
array5

# part d: Use horizontal stacking with two copies of array3 to create a 4-by-4 array6.
array6 = np.hstack((array3, array3))
array6

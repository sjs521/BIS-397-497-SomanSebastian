#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 19:14:30 2020

@author: sebastian_soman
"""


import numpy as np

powers_of_two = [2**x for x in range(6)]
powers_of_two

powers_array = np.array(powers_of_two).reshape((2,3))
powers_array

# flatten
print('Flatten:', powers_array.flatten())
print(powers_array)
# ravel
print('Ravel:', powers_array.ravel())
print(powers_array)

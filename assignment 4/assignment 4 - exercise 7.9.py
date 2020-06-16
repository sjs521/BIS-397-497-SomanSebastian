#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 19:40:51 2020

@author: sebastian_soman
"""


import numpy as np

values = np.array([x for x in range(1,16)])
values_2d = values.reshape(3,5)
values_2d

# part a: select row 2
values_2d[2]

# part b: select column 4
values_2d[:,4]

# part c: select rows 0 and 1
values_2d[0:2]

# part d: select columns 2-4
values_2d[:,2:5]

# part e: select the element that is in row 1 and column 4
values_2d[1,4]

# part f: select all elements from rows 1 and 2 that are in columns 0, 2 and 4
values_2d[1:3,[0,2,4]]


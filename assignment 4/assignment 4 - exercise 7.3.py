#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 18:52:19 2020

@author: sebastian_soman
"""


import numpy as np

numbers = np.arange(2,19,2).reshape(3,3)
numbers

numbers2 = np.arange(9,0,-1).reshape(3,3)
numbers2

product = numbers * numbers2
product

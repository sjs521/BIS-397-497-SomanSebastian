#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 19:07:21 2020

@author: sebastian_soman
"""
import pandas as pd

def display_table(a):
    return pd.DataFrame(a)

test_list = [[1,2,3],
             [4,5,6],
             [7,8,9]]
             
display_table(test_list)

            
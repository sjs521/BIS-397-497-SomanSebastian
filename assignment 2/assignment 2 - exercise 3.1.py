#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 16:35:57 2020

@author: sebastian_soman
"""

# initialize variables
passes = 0  # number of passes # number of failures

# process 10 students 
student = 0
while student < 10:
    # get one exam result
    result = int(input('Enter result (1=pass, 2=fail): '))
    if result == 1:
        passes += 1
        student += 1
    elif result == 2:
        student += 1
    else: #if result is not a 1 or 2, student variable doesn't increment
        print('Invalid Input')
    
# termination phase
print('Passed:', passes)
print('Failed:', 10-passes)

if passes > 8:
    print('Bonus to instructor')
    
    
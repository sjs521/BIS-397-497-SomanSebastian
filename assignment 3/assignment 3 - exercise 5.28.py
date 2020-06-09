#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 19:47:30 2020

@author: sebastian_soman
"""

import statistics

responses = [1,2,5,4,3,5,2,1,3,3,1,4,3,3,3,2,3,3,2,5]

minimum = min(responses)
maximum = max(responses)
response_range = maximum - minimum
mean = statistics.mean(responses)
median = statistics.median(responses) 
mode = statistics.mode(responses)
variance = statistics.variance(responses)
std_dev = statistics.stdev(responses)


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 12:44:57 2020

@author: sebastian_soman
"""


import pandas as pd

YT = pd.read_csv('/Users/sebastiansoman/Downloads/yellow_tripdata_2017-06.csv')
pd.set_option('display.float_format', lambda x: '%.5f' % x)

#data cleaning based on taxi requirements
YT.drop(YT[YT['trip_distance'] > 100].index, inplace=True)
YT.drop(YT[YT['passenger_count'] == 0].index, inplace=True)
YT.drop(YT[YT['trip_distance'] == 0].index, inplace=True)
YT.drop(YT[YT['fare_amount'] <= 0].index, inplace=True)
YT.drop(YT[YT['fare_amount'] >= 1000].index, inplace=True)
YT.drop(YT[YT['extra'] <= 0].index, inplace=True)
YT
YT.describe()
YT.to_csv('YT_curated.csv', index = False)




# Rules we agree to
# trip_distance <= 100 (already implemented)
# delete any rows where passengers = 0 
# delete trip distance = 0
# fare amount make greater than zero, lt 1,000
# make "extra" >= 0



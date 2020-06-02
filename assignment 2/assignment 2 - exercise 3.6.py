#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 16:24:17 2020

@author: sebastian_soman
"""


response1 = input('What is your problem? ')
response2 = input('Have you had this problem before (yes or no)? ')
if response2 == 'yes':
    print('Well, you have it again.')
if response2 == 'no':
    print('Well, you have it now.')
    

# I don't believe this conversation would convince the the user 
# that the entity at the other end exhibits intelligent behavior
# because it doesn't respond to the first question and gives a vague positive
# diagnosis regardless of if the individual has had the problem before
    
    


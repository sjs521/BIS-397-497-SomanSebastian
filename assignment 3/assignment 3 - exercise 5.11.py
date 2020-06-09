#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 20:17:42 2020

@author: sebastian_soman
"""
import string

def summarize_letters(word):
    count = {}
    lowercase_word = word.lower()
    for char in lowercase_word:
        if char in count and char.isalpha():
            count[char] = count[char] + 1
        if char not in count and char.isalpha():
            count[char] = 1
        list_of_tuples = [(char, count) for char, count in count.items()]
    return list_of_tuples        

test = 'aaaaAbcdefghijklmz'
print(summarize_letters(test))

alphabet = string.ascii_lowercase
if test.lower() >= alphabet:
    print('The string has all letters of the alphabet')
else:
    print('The string does not have all letters of the alphabet')
    
   

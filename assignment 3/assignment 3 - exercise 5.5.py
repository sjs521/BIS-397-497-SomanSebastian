#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 19:57:30 2020

@author: sebastian_soman
"""


alphabet = 'abcdefghijklmnopqrstuvwxyz'

# part a: first half of string using starting and ending indices
first_half = alphabet[0:13]

# part b: first half of string using only ending index
first_half2 = alphabet[:13]

# part c: second half of string using starting and ending indices
second_half = alphabet[13:26]

# part d: second half of string using only starting index
second_half2 = alphabet[13:]

# part e: every second letter in string starting with 'a'
second_letter = alphabet[::2]

# part f: entire string in reverse
reverse_alphabet = alphabet[::-1]

#part g: every third letter of string in reverse starting with 'z'
third_letter = alphabet[::-3]

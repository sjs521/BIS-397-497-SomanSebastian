#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 20:10:25 2020

@author: sebastian_soman
"""

test_string = 'I like sports and I like food and other stuff'

word_count = {}
for word in test_string.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(f'{"Word":<10}Count')
for word, count in sorted(word_count.items()):
    print(f'{word:<10}{count}')
          
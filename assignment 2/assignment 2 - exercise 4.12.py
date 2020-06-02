#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 17:11:45 2020

@author: sebastian_soman
"""

import random

clock = 0
tortoise_position = 1
hare_position = 1
end = 70

def tortoise_move(tortoise_position):
    move = random.randrange(1, 11)
    
    if 1 <= move <= 5: #fast plod
        tortoise_position += 3
    elif 6 <= move <= 7: #slip
        tortoise_position -= 6
    else: #slow plod
        tortoise_position += 1
    
    if tortoise_position < 1:
        tortoise_position = 1
    elif tortoise_position > end:
        tortoise_position = end
        
    return tortoise_position

def hare_move(hare_position):
    move = random.randrange(1, 11)
    
    if 3 <= move <= 4: #big hop
        hare_position += 9
    elif move == 5: #big slip
        hare_position -= 12
    elif 6 <= move <= 8: #small hop
        hare_position += 1
    elif move > 8: #small slip
        hare_position -= 2
        
    if hare_position < 1:
        hare_position = 1
    elif hare_position > end:
        hare_position = end
    
    return hare_position

def print_positions(tortoise_position, hare_position):
    for count in range(1, end + 1):
        if count == tortoise_position and count == hare_position:
            print('OUCH!!!', end='')
        elif count == tortoise_position:
            print( 'H', end='')
        elif count == hare_position:
            print('T', end='')
        else:
            print(' ', end='')


print('BANG !!!!!')
print('AND THEY\'RE OFF !!!!!')


while (tortoise_position < end) and (hare_position < end):
    tortoise_position = tortoise_move(tortoise_position)
    hare_position = hare_move(hare_position)
    print_positions(tortoise_position, hare_position)
    clock += 1

if tortoise_position >= hare_position:
    print('\n\nTORTOISE WINS!!! YAY!!!')
elif hare_position >= tortoise_position:
    print('\n\nHare wins. Yuch.')


    
    
        
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 15:37:59 2020

@author: sebastian_soman
"""

import random

def roll_dice():
    # creates random rolls for 5 die
    die1 = random.randrange(1,7)
    die2 = random.randrange(1,7)
    die3 = random.randrange(1,7)
    die4 = random.randrange(1,7)
    die5 = random.randrange(1,7)
    return [die1, die2, die3, die4, die5]  

def display_dice(dice):
    # displays the die
    die1, die2, die3, die4, die5 = dice
    print(f'Your roll is: {die1} {die2} {die3} {die4} {die5}')

die_values = roll_dice()
display_dice(die_values)  

def reroll(dice):
    #reroll prompt then adjusts initial die list
    reroll_values = input('Enter the dice you would like to reroll (separate by comma; enter -99 to stop): ')
    final_reroll_values= reroll_values.split(',')
    reroll_list = [int(num) for num in final_reroll_values]
    delete_value = reroll_list.index(-99)
    del reroll_list[delete_value] #creates list with all inputs except -99
    
    #matches indicies with original die
    for index, die in enumerate(reroll_list):
        reroll_list[index] = int(die) - 1
    for index in reroll_list:
        die_values[index] = random.randrange(1,6)
    print('Your new roll is: ')
    for die in die_values:
        print(die, end=' ')
        
#last step is a repeated option to reroll 
reroll(die_values)
print('\nOne more chance to reroll...') 
reroll(die_values)
print('--> These are your final die!')



    

    


    
        
        
        
        
    






    






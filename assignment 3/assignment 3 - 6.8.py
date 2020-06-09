#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 20:22:51 2020

@author: sebastian_soman
"""


def convert(num):
  
   l = len(num)

   if (l == 0):
       print("empty string")
       return

  
   if (l > 4):
       print("Not testing more than 4 digits before the decimal");
       return

   single_digits = ["zero", "one", "two", "three",
                   "four", "five", "six", "seven",
                   "eight", "nine"]

   two_digits = ["", "ten", "eleven", "twelve",
               "thirteen", "fourteen", "fifteen",
               "sixteen", "seventeen", "eighteen",
               "nineteen"]

   tens_multiple = ["", "", "twenty", "thirty", "forty",
                   "fifty", "sixty", "seventy", "eighty",
                   "ninety"]

   tens_power = ["hundred", "thousand"]

  
   # For single digit number
   if (l == 1):
       print(single_digits[ord(num[0]) - '0'])
       return

   x = 0
   while (x < len(num)):
      
       # first 2 digits
       if (l >= 3):
           if (ord(num[x]) - 48 != 0):
               print(single_digits[ord(num[x]) - 48],
                                       end = " ")
               print(tens_power[l - 3], end = " ")
           l -= 1
       else:    
          
          if (ord(num[x]) - 48 == 1):
               sum = (ord(num[x]) - 48 +
                   ord(num[x+1]) - 48)
                  
               print(two_digits[sum] , end = " ")
               return

          elif (ord(num[x]) - 48 == 2 and
               ord(num[x + 1]) - 48 == 0):
               print("twenty", end = " ")
               return
              
          else:
               i = ord(num[x]) - 48
               if(i > 0):
                   print(tens_multiple[i], end = " ")
               else:
                   print("", end = "")
               x += 1
               if(ord(num[x]) - 48 != 0):
                   print(single_digits[ord(num[x]) - 48], end = " ")
       x += 1

amount = input("Enter Amount : ")

amount_num = amount.split('.')

# part before the decimal
convert((amount_num[0]))

# part after decimal part
if(len(amount_num[1]) == 1):
    print("and "+ amount_num[1] + '0/100')
else:
    print("and "+ amount_num[1] + '/100')


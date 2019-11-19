# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 14:28:09 2019

@author: user
"""

value  = int(input("Enter any number"))

while value != 1:
    print (value)
    if value % 2 == 0 :
        value =  value / 2
    else:
        value = (3 * value) + 1
    
print(value)
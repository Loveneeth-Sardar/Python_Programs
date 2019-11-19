# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 20:04:57 2019

@author: user
"""

import random

def Dice_Rolling():
    print ('Dice Rolling Simulator')
    User_input = (input('Press yes to start otherwise no: ')).lower()
    if(User_input == 'yes' or 'y' or 'YES' or 'Y'):
        r1 = random.randint(1,6)
        print (r1)
    elif(User_input == 'no' or 'n' or 'NO' or 'N'):
        print('Stopped Simulator')
    else:
        print(User_input)
        Dice_Rolling()
        
    
Dice_Rolling()

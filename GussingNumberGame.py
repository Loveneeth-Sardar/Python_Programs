# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 13:55:52 2019

@author: user
"""

def GuessingNumberGame():
    User_name =input('Enter your name ')
    print('Hello '+str(User_name) + '!Let us play a game ')
    print('You have only 3 attempts')
    GuessNum = int(input('Guess any number from 1-9 :'))
    secretNum = 8
    Guesscount = 1
    while (secretNum != GuessNum and Guesscount < 3  ):
        print('Oops! wrong Guess')
        GuessNum = int(input('Guess any number from 1-9 :'))
        Guesscount = Guesscount +1 
        
        
    if(secretNum == GuessNum):
        print ('You Win')
    else:
        print('You Lost')
        
   
GuessingNumberGame()


    
        
        
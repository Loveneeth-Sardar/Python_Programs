# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 12:45:12 2019

@author: user
"""
import time

answer_1 = ["N","n"]
answer_2  = ["S","s"]
answer_3 = ["E","e"]
answer_4 = ["W","w"]



def text_adventure():
    print("Welcome to happy Home.Which direction you would like to go? 'N','S','E' or 'W'")
    choice = input(">>>")
    time.sleep(2)
    if choice in answer_1:
        North_Direction()
    elif choice in answer_2:
        South_Direction()
    elif choice in answer_3:
        East_Direction()
    elif choice in answer_4:
        West_Diretion()
    else:
        print("Wrong option")
        text_adventure()
    
        
    
def North_Direction():
    print("This is the kitchen.There is a passage E,W,S")
    choice = input(">>>")
    time.sleep(2)
    if choice in answer_2:
        East_Direction()
    elif choice in answer_3:
        West_Diretion()
    elif choice in answer_4:
        South_Direction()
    else:
        print("Wrong press")
        North_Direction()
    
        
def South_Direction():
    print("This is a livingroom.Here you can watch tv and play some vedio games.The passage to other rooms E and W ")
    choice = input(">>>")
    time.sleep(2)
    if choice in answer_3:
        East_Direction()
    elif choice in answer_4:
        West_Diretion()
     
def East_Direction():
    print("This is bedroom where you can rest and take a good nap.You can acesses to other room using W.")
    choice =  input(">>>")
    time.sleep(2)
    if choice in answer_4:
        West_Diretion()

def West_Diretion():
    time.sleep(2)
    print("This is a balcony.Where you can relax have some coff and watch set.This is the deadend. ")
   
        
text_adventure()   
    
  
    
    
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 11:29:24 2019

@author: user
"""

#### Simple Interest ######


def simple_interest():
    P = int(input("Enter The amount"))
    R = float(input("Rate of interest per year"))
    T= int(input("Time in total number of months"))
    A = (P * T * R) / 100
    print("Your interest is ",A) 

simple_interest()   

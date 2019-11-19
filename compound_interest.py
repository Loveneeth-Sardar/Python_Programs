# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 11:53:18 2019

@author: user
"""



def compound_interest(): 
  
    # Calculates compound interest  
    
    P = int(input("Enter principal balance: "))
    R = float(input("Rate of interest per year in decimal :"))
    r = (R / 100)
    t = int(input("Total in months :"))
    CI = P * (pow((1 + r / 100), t)) 
    print("Compound interest is", CI) 
  
# Driver Code  
compound_interest() 

    
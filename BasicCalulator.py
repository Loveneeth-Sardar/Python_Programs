# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 15:22:26 2019

@author: user
"""

def add(num1,num2):
    return num1 + num2


def sub(num1,num2):
    return num1 - num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2

print("Basic Calculator")

user_value = int(input("1.Addition \n"\
      "2.Substraction \n" \
      "3.multilpiation \n" \
      "4.Division "))
num1= int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

if user_value == 1:
    print(add(num1,num2))

elif user_value == 2:
    print(sub(num1,num2))
    
elif user_value == 3:
    print(mul(num1,num2))

elif user_value == 4:
    print(div(num1,num2))

else:
    print("Wrong operator")
    

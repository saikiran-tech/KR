# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 09:12:12 2019

@author: SAI KIRAN REDDY
"""

import random as rand
r = rand.randint(1,9)
guess = 0
count = 0
while guess!= "exit":
    guess = input("Guess the number: ")
    if guess == "exit":
        break
    
    guess = int(guess)
    count+=1
    
    if guess<r:
        print("Too low ")
    elif guess>r:
        print("Too high ")
    else:
        print("You got correct for",count,"trials")
        

        
        
    
    


    

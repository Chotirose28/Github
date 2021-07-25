# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 21:34:34 2021
Stick in the pile
@author: Chotirose
"""
import random

number_stick = int(input('How many stick (N) in the pile?: '))
print("There are",number_stick,"sticks in the pile.")
name = str(input("What is your name: "))

def player(number):
    number_take = int(input(name + ", how many sticks you will take (1 or 2): "))
    if number_take > 0:
        if number_take <= 2:
            if number_take <= number_stick:
                print(name + ', take', number_take, 'stick')
            else:
                number_take = 0
                print('There are not enough stick to take')
        else:
            number_take = 0
            print('No you cannot take more than 2 stick!')
    else:
        number_take = 0
        print('No you cannot take less than 1 stick!')
    return number_take

def computer(number):
    number_com_take = random.randint(1, 2)
    if number_com_take > number_stick:
        number_com_take = 0
    else:
        print('I, smart computer, take', number_com_take)
    return number_com_take


while number_stick > 0:
    number_take = player(number_stick)
    if number_take != 0:
        print(number_take)
        number_stick = number_stick - number_take
        print(number_stick)
    else:
        continue
    if number_stick == 0:
        print(name + ', take the last stick.')
        print('I, smart computer, win!!!!')
        
    m = True
    while m == True:
        number_com_take = computer(number_stick)
        if number_com_take != 0:
            print(number_com_take)
            number_stick = number_stick - number_com_take
            print(number_stick)
            m = False
        else:
            continue
    if number_stick == 0:
        print('I, smart computer, take the last stick.')
        print(name + ' win, I, smart computer, am sad T_T')
    
    
    
    
    
        
        
        
        
        
        

   
    
    
    
    
    


    

# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 21:34:34 2021
HW A3 Stick in the pile
@author: Chotirose
"""

number_stick = int(input('How many sticks (N) in the pile?: '))
print("There are",number_stick,"sticks in the pile.")
name = str(input("What is your name: "))

def player(number):
    number_take = int(input(name + ", how many sticks you will take (1 or 2): "))
    if number_take > 0:
        if number_take <= 2:
            if number_take <= number_stick:
                pass
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

def com(number):
    if number%3 == 0:
        return 2
    else:
        return 1
    
def print_result(number):
    if number == 1:
        print('There is', number_stick, 'in the pile')
    if number > 1:
        print('There are', number_stick, 'in the pile')

while number_stick > 0:
    number_com_take = com(number_stick)
    number_stick = number_stick - number_com_take
    print('I, smart computer, takes', number_com_take)
    print_result(number_stick)
    if number_stick == 0:
        print('I, smart computer take the last stick.')
        print(name, 'win. I, smart computer, am sad T_T')
    
    m = True
    while m == True and number_stick > 0:
        number_take = player(number_stick)
        if number_take != 0:
            number_stick = number_stick - number_take
            print_result(number_stick)
            m = False
        else:
            continue
        if number_stick == 0:
            print(name + ', takes the last stick.')
            print('I, smart computer, win!!!!')


        
     
        
        
        
        

     
    
    
    
    


    

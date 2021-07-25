# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 21:34:34 2021
Stick in the pile
@author: Chotirose
"""

number_stick = int(input('How many stick (N) in the pile?: '))
print("There are",number_stick,"sticks in the pile.")
name = str(input("What is your name: "))

def player(number):
    number_take = int(input(name + ", how many sticks you will take (1 or 2): "))
    if number_take >= 0:
        if number_take <= 2:
            if number_take <= number_stick:
                print(name + ', take', number_take, 'stick')
            else:
                print('There are not enough stick to take')
                player(number)
        else:
            print('No you cannot take more than 2 stick!')
            player(number)
    else:
        print('No you cannot take less than 1 stick!')
        player(number)
    return number_take
    

number_take = player(number_stick)
number_stick = number_stick - number_take
print(number_take)

    

# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 23:33:54 2021
HW04_B1
@author: Chotirose
"""
l = []
l2 = []

'''
use for collect the recieved number as string in the list
number refers to amount of number we would like to collect from user (length of list)
'''
def recieve(number):
    while number > 0:
        a = int(input('Type your number: '))
        if a >= 0:
            l.append(str(a))
            number -= 1
    return l  

#use for create the biggest number by concatenate string
def biggestnum(k):
    biggest = ""
    for i in (k):
        biggest += i
    return biggest

#ask for number and stop when length of the list l = 4
recieve(4)      

'''
compare number in string type to find the biggest and arrange in order
by compare XY > YX or not then compare it again with b to make sure 
that it is the biggest number and collect the number in l2 
then remove it from l
(at first, assign b as '0' because it is the possible smallest number)
'''
while len(l) > 0:
    b = '0'
    for i in range (len(l)):
        for j in range (i+1, len(l)):
            if l[i] + l[j] > l[j] + l[i]:
                if l[i]+b > b+l[i]:
                    b = l[i]
            else:
                if l[j]+b > b + l[j]:
                    b = l[j]
    l2.append(b)
    l.remove(b)
    if len(l) == 1:
        l2.append(l[0])
        l.remove(l[0])

#show the output
print(biggestnum(l2))
    

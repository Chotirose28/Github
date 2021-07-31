# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 23:33:54 2021
HW04_B1
@author: Chotirose
"""
l = []
m = True
a = '0'

def recieve(m):
    a = int(input('Type your number: '))
    if a >= 0:
        l.append(str(a))

while m == True:
    recieve(m)
    if len(l) == 4:
        m = False

for i in range (len(l)):
    for j in range (i+1, len(l)):
        if l[i] + l[j] > l[j] + l[i]:
            if l[i]+a > a+l[i]:
                a = l[i]
        else:
            if l[j]+a > a + l[j]:
                a = l[j]
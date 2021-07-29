# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 23:33:54 2021
HW04_B1
@author: Chotirose
"""
l = []
m = True

while m == True:
    a = int(input('Type your number: '))
    if a >= 0:
        l.append(a)
    else:
        continue
    if len(l) == 4:
        m = False


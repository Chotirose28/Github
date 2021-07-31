# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 23:33:54 2021
HW04_B1
@author: Chotirose
"""
l = []
l2 = []
m = True

def recieve(m):
    a = int(input('Type your number: '))
    if a >= 0:
        l.append(str(a))
    return l

while m == True:
    recieve(m)
    if len(l) == 4:
        m = False

n = True
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

biggest = ""
for i in range (len(l2)):
    biggest += l2[i]

print(biggest)


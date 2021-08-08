# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 12:41:52 2021
HW5
@author: Chotirose
"""
'''
Decision variable:  x1 = vanilla ice cream
                    x2 = strawberry ice cream
Objective function: Maximum profit = 2x1 + 3x2
Constraints: 0.5x1 + 0.2x2 <= 10
            x1 + x2 <= 30
            x1 >= 0
            x2 >= 0
'''
import numpy as np
C = np.array([[2, 3]]) #Coefficient for x1 and x2
A = np.array([[0.5, 0.2],
              [1, 1]]) #Constraint left side
B = np.array([10,
              30]) #Constraint right side

#Constraint of x1 and x2 >= 0
bnd = [(0, float("inf")),
   (0, float("inf"))]

from scipy.optimize import linprog
opt = linprog(c=-C, A_ub=A, b_ub=B,bounds=bnd, method="revised simplex")
print(opt)










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
            x1 >= 0
            x2 >= 0
'''
import numpy as np
A = np.array([2, 3]).reshape(1,2) #Coefficient for x1 and x2
B = np.array([[0.5, 0.2]]) #Constraint left side
C = np.array([10]) #Constraint right side








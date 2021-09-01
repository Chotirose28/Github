# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 22:21:46 2021
HW6
@author: Chotirose
"""
import pandas as pd

df = pd.read_csv('C:/Users/Choti/Documents/270702/avocado.csv')

#1
largest = df.groupby(['region'])[['Total Volume']].sum()
largest_sorted =  largest.sort_values(by = 'Total Volume', ascending = [False])
''' The region which sold the largest amount is West'''
biggest = df.groupby(['region'])[['Total Volume', '4046', '4225','4770']].sum()
biggest_sort = biggest.sort_values(by = 'Total Volume', ascending = [False])
'''In the West region, the biggest lot of sold avocado came from 4046'''
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 22:21:46 2021
HW6
@author: Chotirose
"""
'''
In avocado dataset, the region column consist of regions, cities, island and state.
So, the real region in this dataset are GreatLakes, Midsouth, Northeeast, 
Northern New Enngland, Plains, Sount Central, Southeast and West 
(the regions in this dataset is close to Bureau of Economic Analysis regions).
Note: US has many ways to define region
'''
import pandas as pd

df = pd.read_csv('C:/Users/Choti/Documents/270702/avocado.csv')

#1
amount = df.groupby(['region'])[['Total Volume']].sum()
largest =  amount.sort_values(by = 'Total Volume', ascending = [False])
''' The region which sold the largest amount is West (1.08678e+09)'''
lot = df.groupby(['region'])[['Total Volume', '4046', '4225','4770']].sum()
biggest = lot.sort_values(by = 'Total Volume', ascending = [False])
'''In the West region, the biggest lot of sold avocado came from 4046 (3.98591e+08)'''

#2
smallest = amount.sort_values(by = 'Total Volume', ascending = [True])
''' The region which sold the smallest amount is NorthernNewEngland (7.15329e+07)'''
biggest = lot.sort_values(by = 'Total Volume', ascending = [True])
'''In the Plains , the biggest lot of sold avocado came from 4225 (5.36093e+07)'''

#3
price = df.groupby(['region'])[['AveragePrice']].mean()
price_sorted = price.sort_values(by = 'AveragePrice', ascending = [False])
''' The region which sold the highest price of avocado in average is Northeast (1.60192)'''

#4
df['income'] = df['AveragePrice']*df['Total Volume']
Total_income = df.groupby(['region'])[['income']].sum()
print(Total_income)
'''
GreatLakes           6.886618e+08
Midsouth             6.157238e+08
Northeast            9.600079e+08
NorthernNewEngland   8.962525e+07
Plains               3.600366e+08
SouthCentral         8.740593e+08
Southeast            7.036306e+08
West                 1.066834e+09
'''

#5
df['number'] = df['4046']/4 + df['4225']/9 + df['4770']/12
avocado_number = df.groupby(['region'])[['number']].sum()
print(avocado_number)
'''
GreatLakes           5.729755e+07
Midsouth             5.390177e+07
Northeast            6.203637e+07
NorthernNewEngland   6.742007e+06
Plains               4.578964e+07
SouthCentral         1.601211e+08
Southeast            9.528098e+07
West                 1.347616e+08

The region which sold the largest number of avocados is South Central
'''

#6
unit_or_bag = df[['Total Bags', 'number']].sum()
print(unit_or_bag)
'''
Total Bags    4.373176e+09
number        1.969986e+09
dtype: float64

Normally, customers buy the avocados in a bags
'''

#7
#Extract month from date
date = df['Date']
month = [c.split("-")[1] for c in date]
df['month'] = month

#find the month which is the best time to sell avocado
best_time = df.groupby(['month'])[['Total Volume']].sum()
best_time_sorted = best_time.sort_values(by= 'Total Volume', ascending = [False])
print(best_time_sorted)
'''
       Total Volume
month              
02     1.760529e+09
01     1.756531e+09
03     1.623952e+09
05     1.470745e+09
07     1.298881e+09
04     1.235792e+09
06     1.202566e+09
08     1.128375e+09
12     1.086807e+09
10     1.028756e+09
09     9.763016e+08
11     9.541687e+08

So, the month which is the best time to sell avocado is Febuary (02)
'''
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
However, in this HW, the region is considered as the area. 
So, we do not care if it is an actually region or not.
'''
import pandas as pd

df = pd.read_csv('C:/Users/Choti/Documents/270702/avocado.csv')

#For undefined region (do not care if it a actually region or not)
#1 Which region sold the largest amount of avocado?
amount = df.groupby(['region'])[['Total Volume']].sum()
largest =  amount.sort_values(by = 'Total Volume', ascending = [False])
largest.head()  #show the 1st 5 records
''' The region which sold the largest amount is TotalUS (5.864740e+09).'''

#In this region, where the biggest lot of sold avocado came from (4046, 4225, 4770)?
lot = df.groupby(['region'])[['Total Volume', '4046', '4225','4770']].sum()
biggest = lot.sort_values(by = 'Total Volume', ascending = [False])
biggest.head(1)  #show the 1st record
'''In the TotalUS, the biggest lot of sold avocado came from 4046 (2.054936e+09).'''

#2 Which region sold the smallest amount of avocado?
smallest = amount.sort_values(by = 'Total Volume', ascending = [True])
smallest.head()     #show the 1st 5 records
''' The region which sold the smallest amount is Syracuse (1.094267e+07)'''
#In this region, where the biggest lot of sold avocado came from (4046, 4225, 4770)?
biggest = lot.sort_values(by = 'Total Volume', ascending = [True])
biggest.head(1)     #show the 1st record
'''In the Syracuse, the biggest lot of sold avocado came from 4225 (6.390341e+06).'''

#3 Which region sold the highest price of avocado in average?
price = df.groupby(['region'])[['AveragePrice']].mean()
price_sorted = price.sort_values(by = 'AveragePrice', ascending = [False])
price_sorted.head() #show the 1st 5 records
''' The region which sold the highest price of avocado in average is HartfordSpringfield (1.818639 US Dollar).'''

#4 Find the total amount of income (Avg_Price*Total_Volume) of each region.
df['income'] = df['AveragePrice']*df['Total Volume']    #create 'income' column
Total_income = df.groupby(['region'])[['income']].sum()
print(Total_income)
'''
                           income
region                           
Albany               2.176672e+07
Atlanta              9.379337e+07
BaltimoreWashington  1.799084e+08
Boise                1.534667e+07
Boston               1.265429e+08
BuffaloRochester     3.154509e+07
California           1.121414e+09
Charlotte            4.574304e+07
Chicago              1.791106e+08
CincinnatiDayton     4.498958e+07
Columbus             3.156295e+07
DallasFtWorth        1.756093e+08
Denver               1.459828e+08
Detroit              6.912624e+07
GrandRapids          3.785124e+07
GreatLakes           6.886618e+08
HarrisburgScranton   5.295472e+07
HartfordSpringfield  7.118645e+07
Houston              1.655713e+08
Indianapolis         3.402474e+07
Jacksonville         3.348396e+07
LasVegas             5.480905e+07
LosAngeles           4.842276e+08
Louisville           1.749555e+07
MiamiFtLauderdale    1.185815e+08
Midsouth             6.157238e+08
Nashville            3.572664e+07
NewOrleansMobile     4.867626e+07
NewYork              3.351955e+08
Northeast            9.600079e+08
NorthernNewEngland   8.962525e+07
Orlando              6.961121e+07
Philadelphia         9.981583e+07
PhoenixTucson        1.384515e+08
Pittsburgh           2.319481e+07
Plains               3.600366e+08
Portland             1.128646e+08
RaleighGreensboro    5.983780e+07
RichmondNorfolk      4.734482e+07
Roanoke              2.740928e+07
Sacramento           9.480870e+07
SanDiego             9.352710e+07
SanFrancisco         1.858341e+08
Seattle              1.251791e+08
SouthCarolina        6.952808e+07
SouthCentral         8.740593e+08
Southeast            7.036306e+08
Spokane              1.715649e+07
StLouis              3.743946e+07
Syracuse             1.520519e+07
Tampa                7.695906e+07
TotalUS              6.387593e+09
West                 1.066834e+09
WestTexNewMexico     1.215654e+08

(in US Dollar)
'''

#5 Let AVOCADO Average Weight: 4046 => 4 ounces, 4225 => 9 ounces, 4770 => 12 ounces
#Find the number of sold avocadoes by region?
df['Number_of_Avocado'] = df['4046']/4 + df['4225']/9 + df['4770']/12  #find number of avocado and store in 'Number_of_Avocado' column
number = df.groupby(['region'])[['Number_of_Avocado']].sum()
number_sorted = number.sort_values(by= 'Number_of_Avocado', ascending = [False])
print(number_sorted)
'''
                     Number_of_Avocado
region                                
TotalUS                   7.506388e+08
SouthCentral              1.601211e+08
California                1.414498e+08
West                      1.347616e+08
Southeast                 9.528098e+07
LosAngeles                6.845295e+07
Northeast                 6.203637e+07
GreatLakes                5.729755e+07
Midsouth                  5.390177e+07
Plains                    4.578964e+07
PhoenixTucson             3.338693e+07
DallasFtWorth             3.323216e+07
Houston                   3.070056e+07
WestTexNewMexico          2.373108e+07
NewYork                   2.020583e+07
SanFrancisco              1.807756e+07
MiamiFtLauderdale         1.645062e+07
Chicago                   1.393341e+07
Atlanta                   1.352807e+07
BaltimoreWashington       1.260212e+07
Denver                    1.247834e+07
SanDiego                  1.203062e+07
Sacramento                1.056749e+07
Tampa                     1.013142e+07
Portland                  9.927132e+06
Seattle                   9.455807e+06
Orlando                   9.280617e+06
SouthCarolina             8.635995e+06
Boston                    8.607525e+06
NewOrleansMobile          7.208896e+06
LasVegas                  6.751638e+06
NorthernNewEngland        6.742007e+06
Detroit                   6.720597e+06
Philadelphia              5.953621e+06
RaleighGreensboro         5.143921e+06
Nashville                 5.024405e+06
RichmondNorfolk           5.002926e+06
HartfordSpringfield       4.549392e+06
Jacksonville              4.265906e+06
HarrisburgScranton        4.183936e+06
Columbus                  3.921197e+06
StLouis                   3.802083e+06
Charlotte                 3.592665e+06
CincinnatiDayton          2.846748e+06
Roanoke                   2.751174e+06
Indianapolis              2.329401e+06
GrandRapids               2.314695e+06
Boise                     1.911415e+06
Pittsburgh                1.828299e+06
Spokane                   1.596770e+06
Albany                    1.571607e+06
BuffaloRochester          1.343352e+06
Louisville                1.140420e+06
Syracuse                  7.953276e+05

(in unit of avocado)

Which region sold the largest number of avocados?
Ans. The region which sold the largest number of avocados is TotalUS.
'''

#6 Normally, the customers buy the avocados by unit or in a bags?
unit_or_bag = df[['Total Bags', 'Number_of_Avocado']].sum()
print(unit_or_bag)
'''
Total Bags               4.373176e+09
Number_of_Avocado        1.969986e+09
dtype: float64

Total Bags is greater than Number of avocado
Ans. Normally, customers buy the avocados in a bags
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

So, the month which is the best time to sell avocado is February (02)
'''
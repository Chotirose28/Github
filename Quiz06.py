# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 14:41:01 2021
#Exercise: Pandas
@author: Chotirose
"""
import pandas as pd

#Read csv file
df = pd.read_csv("Salaries.csv")

#Quiz 1
#Read the first 10 row
df.head(10)     #give result as row[0] to row[9]

#Read the first 20 row
df.head(20)     #give result as row[0] to row[19]

#Read the first 50 row
df.head(50)     #give result as row[0] to row[49]

#Read the last few record
df.tail(3)      #give result as row[75] to row[77]

#1
#Group data using rank
df_rank = df.groupby(['rank'])

#2
#Calculate mean value for each numeric column per each group
df_rank.mean()
''' 
result in every column:                 
                phd    service         salary
rank                                          
AssocProf  15.076923  11.307692   91786.230769
AsstProf    5.052632   2.210526   81362.789474
Prof       27.065217  21.413043  123624.804348
'''

#3
#Calculate mean salary for each professor rank:
df.groupby('rank')[['salary']].mean()
'''
result in only column 'salary'
                  salary
rank                    
AssocProf   91786.230769
AsstProf    81362.789474
Prof       123624.804348
'''

#4
#Calculate mean salary for each professor rank:
df.groupby(['rank'], sort = False)[['salary']].mean()
''' 
now, the group key are not sorted and result as following:
                  salary
rank                    
Prof       123624.804348
AssocProf   91786.230769
AsstProf    81362.789474
''' 

#Filtering
#5
#Calculate mean salary for each professor rank:
df_sub = df[df['salary'] > 120000]
print(df_sub)   #result in 25 rows

#6
#Select only those rows that contain female professors:
df_f = df[df['sex'] ==  'Female']
print(df_f)     #result in 39 rows

#Slicing
#7
#Select column salary:
df['salary']    #return only value in clumn name 'salary'

#8
#Select more than one column and/or make the output to be a DataFrame:
df[['rank', 'salary']]      #return 2 column

#9
#Selecting rows
#Select rowa by their position
df[10:20]       #return row[10] to row[19]

#10
#Method loc (select a range of row, using their labels)
#Select rows by their labels:
df_sub.loc[10:20,['rank','sex','salary']]
'''
result as following:
    rank   sex  salary
10  Prof  Male  128250
11  Prof  Male  134778
13  Prof  Male  162200
14  Prof  Male  153750
15  Prof  Male  150480
19  Prof  Male  150500
'''

#11
#Method iloc(select a range of row and/or column, using their position)
#Select rows by their position:
df_sub.iloc[10:20, [0,3,4,5]]
'''
result as following:
    rank  service     sex  salary
26  Prof       19    Male  148750
27  Prof       43    Male  155865
29  Prof       20    Male  123683
31  Prof       21    Male  155750
35  Prof       23    Male  126933
36  Prof       45    Male  146856
39  Prof       18  Female  129000
40  Prof       36  Female  137000
44  Prof       19  Female  151768
45  Prof       25  Female  140096
'''

#Sorting
#12
#Create a new data frame from the original sorted by the column Salary
df_sorted = df.sort_values(by = 'service') #sort data by using service column
df_sorted.head()
'''
result as following:
        rank discipline  phd  service     sex  salary
55  AsstProf          A    2        0  Female   72500
23  AsstProf          A    2        0    Male   85000
43  AsstProf          B    5        0  Female   77000
17  AsstProf          B    4        0    Male   92000
12  AsstProf          B    1        0    Male   88000
'''

#13
#We can sort the data using 2 or more columns:
df_sorted = df.sort_values(by = ['service', 'salary'], ascending = [True, False])
df_sorted.head(10)
'''
result as following:
        rank discipline  phd  service     sex  salary
52      Prof          A   12        0  Female  105000
17  AsstProf          B    4        0    Male   92000
12  AsstProf          B    1        0    Male   88000
23  AsstProf          A    2        0    Male   85000
43  AsstProf          B    5        0  Female   77000
55  AsstProf          A    2        0  Female   72500
57  AsstProf          A    3        1  Female   72500
28  AsstProf          B    7        2    Male   91300
42  AsstProf          B    4        2  Female   80225
68  AsstProf          A    4        2  Female   77500

the data is sorted by service column in ascending and salary column in descending
as respectively
'''
#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd 
import numpy as np
health = pd.read_csv('/Users/agnelvarghesepaikkatt/Documents/Data1002 group project/CSV_POSTCODE HEALTH 3/TAB 4-Table 1.csv')

#removing NP values
health.drop(health.index[health['Unnamed: 5'] == 'NP'], inplace = True)

#filtering out data by keeping only "NSW" in "State"
health.set_index("Unnamed: 0", inplace=True)
a = (health.loc['NSW'])

#filtering out data by keeping only "1 year" in "Age group"
a.set_index("Unnamed: 4",inplace=True)
d = (a.loc['1 year'])

#filtering out data by keeping only "2016-17" in "Reporting year"
d.set_index("Unnamed: 3",inplace=True)
b = (d.loc['2016-17'])

#Dropping all columns except "Postcode" and "Percent fully immunised(%)"
b = b.drop("Unnamed: 6",axis=1)
b = b.drop("Unnamed: 2",axis=1)


#Renaming Columns because their name changed while importing
b.rename(columns = {'Unnamed: 1':'Postcode', 'Unnamed: 5':'Percent fully immunised(%)'}, inplace = True)
#Removing duplicates
c = b.drop_duplicates(keep = False)
#Saving the output in a csv and .xlsx file
c.to_csv('healthcleanfin.csv',encoding="utf-8",index=False)
c.to_excel('healthcleanfin.xlsx',encoding="utf-8",index=False)
#On printing "c" we get an extra column Unnamed:3 but this column cannot be dropped and does not show up in the csv


#Some basic summaries on the dataset
import pandas as pd
import numpy as np
health_summary = pd.read_csv('/Users/agnelvarghesepaikkatt/Downloads/healthcleanfin.csv')
#Grouping postcodes by the percentage of 1 year olds that are fully immunised
health_sum = health_summary.sort_values(by=['Percent fully immunised(%)'])
print(health_sum)
print("\n")
#The frequency of percentage range of children immunised
health_sumfreq = health_sum.groupby('Percent fully immunised(%)').count()
print(health_sumfreq)
print("\n")
#Plotting a histogram on health_semfreq
health_sumfreq.hist(column = 'Postcode')
print("\n")
#median of health_semfreq
print(health_sumfreq.median())
print("\n")
#standard deviation of health_semfreq
print(health_sumfreq['Postcode'].std())
print("\n")
#mean of health_semfreq
print(health_sumfreq.mean(axis = 0))
print("\n")
#What was the maximum frequency of percentage range of children immunised
maxm = health_sumfreq['Postcode'].max()
print(maxm)
print("\n")
#What was the minimum frequency of percentage range of children immunised
minm = health_sumfreq['Postcode'].min()
print(minm)
print("\n")
#Total frequency of percentages or toal number of values
Total = health_sumfreq['Postcode'].sum()
print(Total)


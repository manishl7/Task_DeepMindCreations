# -*- coding: utf-8 -*-
"""Task_deepmindcreations.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-hJvfIYqBiyC-zBznSbK6Z40DYMNyxrO
"""

from bs4 import BeautifulSoup
import requests
url=BeautifulSoup('https://www.worldometers.info/coronavirus/','html.parser')
response=requests.get(url)
data=response.text
soup=BeautifulSoup(data,'lxml')

tags=soup.table
tag=tags.find_all('tr',align=False)
list1=[]#Initializing an empty list
for i in tag:
  list1.append(i.get_text())#Assigning data to the list
l2=[]
for j in list1:
  l1=j.split('\n')
  l2.append(l1[2:-1])
for c in l2: #Using F-literal string for better visualization of data
  print(f"{c[0]:{30}}{c[1]:<{20}}{c[2]:{20}}{c[3]:{20}}{c[4]:{20}}{c[5]:{20}}{c[6]:{20}}{c[7]:{20}}{c[8]:{20}}{c[9]:{20}}{c[10]:{20}}{c[11]:{20}}{c[12]:{20}}{c[13]:{20}}{c[14]:{20}}{c[15]:{20}}")

#Visualing data using Matplob lib

import pandas as pd
import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt


#Sorting names

newdata=[]
for c in l2: 
  newdata.append(c[0])
#print(newdata)
a=newdata[0:-8]
#print(a) #Shows first item in the list i.e country's name
cn=[]
for i in range(8,230): #For removing the garbage values from the list as pop and remove method weren't effective
  cn.append(a[i]) 
print(cn)
print(len(cn))

#Sorting total cases

tc=[]
for d in l2:
  tc.append(d[1])
sortedTC=[]
# print(len(tc))
# print(tc)
for i in range(8,230):
  sortedTC.append(tc[i])
print(sortedTC) #gives total cases count in sorted manner
print(len(sortedTC))


fig = go.Figure([go.Bar(x=cn, y=(sortedTC))])
fig.show()

#Displaying same data in pie chart:

# fig = go.Figure(data=[go.Pie(labels=cn, values=sortedTC)])
# fig.show()






























































































































































































































































































































































































































































































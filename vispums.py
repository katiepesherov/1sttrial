#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 12:28:29 2020

@author: kpesh
"""


#NAME: Paul Sogbe, Ekaterina Pesherov
#DATE: May-2020
#COURSE: CPSC-51100
#SEMESTER: SummerI, 2020
#ASSIGNMENT: Programming Assignment 6

print("CPSC-51100, SummerI, 2020")
print("June 2020")
print("NAME: Paul Sogbe, Ekaterina Pesherov")
print("PROGRAMMING ASSIGNMENT #6\n")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#import data
df=pd.read_csv("ss13hil.csv")
fig=plt.figure(dpi=400,figsize=(15,20))

#2x2 plot
ax1=fig.add_subplot(2,2,1)


#upper left graph
HHL=df.HHL.value_counts()
ax1.pie(HHL,startangle=240)
ax1.set_title("Household Languages")
plt.ylabel('HHL')
languages = ['English Only','Spanish', 'Other Indo-European','Asian and Pacific Island languages','Other']
#print(HHL)

ax1.legend(languages,
          loc="upper left")

ax2=fig.add_subplot(2,2,2)
ax3=fig.add_subplot(2,2,3)
ax4=fig.add_subplot(2,2,4)

#place holder data
d=[1,2,3,4,5]
d2=[10,11,12,13,14]

#place holders for real data
ax2.hist(d2,bins=3,color='k',alpha=0.1)
ax3.hist(d2,bins=3,color='k',alpha=0.1)
ax4.scatter(d,d2,s=100)
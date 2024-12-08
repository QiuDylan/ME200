#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 15:07:07 2024

@author: dylanqiu
"""

import numpy as np
import matplotlib.pyplot as plt
"""
tracker_data1 = np.genfromtxt("finaldata1.txt" , skip_header= 1, delimiter = "")
tracker_data1 = np.nan_to_num(tracker_data1,nan=0.0)
tracker_data2 = np.genfromtxt("finaldata2.txt" , skip_header= 1, delimiter = "")
tracker_data2 = np.nan_to_num(tracker_data2,nan=0.0)
tracker_data3 = np.genfromtxt("finaldata3.txt" , skip_header= 1, delimiter = "")
tracker_data3 = np.nan_to_num(tracker_data3,nan=0.0)


t = np.genfromtxt("finaldata.txt", skip_header=1, usecols=0 ) #first column of tracker_data
x = np.genfromtxt("finaldata.txt", skip_header=1, usecols=1 ) #second ""
y = np.genfromtxt("finaldata.txt", skip_header=1, usecols=2 ) #third ""
"""

theta = 24 * np.pi /180 #Windscreen angle in radians



fig0 = plt.figure()
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace= None, hspace=.75)
ax0 =fig0.add_subplot(311)
ax0.plot(t1,x1,label='x1 vs t') #speed set 1
ax0 =fig0.add_subplot(312)
ax0.plot(t2,x2,label='x2 vs t') #speed set 2
ax0 =fig0.add_subplot(313)
ax0.plot(t2,x2,label='x3 vs t') #speed set 3


print()
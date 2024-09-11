#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 17:29:24 2024

@author: dylanqiu
Dylan Qiu & Jake Peyser ME200
"""

import numpy as np
import matplotlib.pyplot as plt

tracker_data = np.genfromtxt("workshop2data.txt" , skip_header= 1, delimiter = "")
tracker_data = np.nan_to_num(tracker_data,nan=0.0)
print(tracker_data)

t = np.genfromtxt("workshop2data.txt", skip_header=1, usecols=0 ) #first column of tracker_data
x = np.genfromtxt("workshop2data.txt", skip_header=1, usecols=1 ) #second ""
y = np.genfromtxt("workshop2data.txt", skip_header=1, usecols=2 ) #third ""
#dt= 0.001 #delt t

dydt = np.gradient(y, t)
d2ydt2 = np.gradient(dydt,t)
dxdt = np.gradient(x,t)
d2xdt2 = np.gradient(dxdt,t)
f, ax = plt.subplots(1)
#plt.plot(t,x,label='dx/dt')
plt.plot(x,t,label='x vs t')
plt.plot(y,t,label='y vs t')
#plt.plot(t,y,label='y vs t') #raw plot
#plt.plot(t,dydt,label= 'dy/dt')
#plt.plot(t,dxdt,label= 'dx/dt')
#plt.plot(t,d2xdt2,label= 'a_x')
#plt.plot(t,d2ydt2,label= 'a_y')
#ax.set_ylim(ymin=0)
#ax.set_xlim(xmin=0)
plt.xlabel("x(m)")
#plt.ylabel("accel(m/s**2)")
plt.ylabel("t(s)")
plt.legend()

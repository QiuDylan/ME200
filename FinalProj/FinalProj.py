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
"""
t1 = np.genfromtxt("finaldata1.txt", skip_header=1, usecols=0 ) #first column of tracker_data
x1 = np.genfromtxt("finaldata1.txt", skip_header=1, usecols=1 ) #second ""
y1 = np.genfromtxt("finaldata1.txt", skip_header=1, usecols=2 ) #third ""
t2 = np.genfromtxt("finaldata2.txt", skip_header=1, usecols=0 ) #first column of tracker_data
x2 = np.genfromtxt("finaldata2.txt", skip_header=1, usecols=1 ) #second ""
y2 = np.genfromtxt("finaldata2.txt", skip_header=1, usecols=2 ) #third ""


theta = 24 * np.pi /180 #Windscreen angle in radians
g = 9.81 #m/s^2
mu_k = 0.3  #between wiper and windscreen

wiper = 24.5 * 25.4 #link dc mm 

fd = 3.17 * 25.4 #mm
gf = 12.69 * 25.4 #mm
og = 2.11 * 25.4 #mm
od = 13.4 * 25.4 #mm 
mass_wiper = 3.48 #kg

def link_equations(a_wiper):
    F_wiper = mass_wiper * a_wiper - mu_k * mass_wiper * g * np.cos(theta)
    
    #m_torque = 1

    return F_wiper 
"""
fig0 = plt.figure()
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace= None, hspace=.75)
ax0 =fig0.add_subplot(211)
ax0.plot(t1,x1,label='x1 vs t') #position graph speed set 1
ax0.set_ylabel("x_position [m]")
ax0.set_xlabel('time[s]')
ax0.set_xlim(0,8)
ax0.legend()
ax0 =fig0.add_subplot(212)
ax0.plot(t2,x2,label='x2 vs t') #position graph speed set 2
ax0.set_ylabel("x_position [m]")
ax0.set_xlabel('time[s]')
ax0.set_xlim(0,8)
ax0.legend()
"""
fig1 = plt.figure()
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace= None, hspace=.75)
ax1 =fig1.add_subplot(211)
ax1.plot(x1,y1,label='x1 vs y1') #position graph speed set 1
ax1.set_ylabel("y1")
ax1.set_xlabel('x1')
#ax1.set_xlim(0,8)
ax1.legend()
ax1 =fig1.add_subplot(212)
ax1.plot(x2,y2,label='x2 vs y2') #position graph speed set 2
ax1.set_ylabel("y")
ax1.set_xlabel('x')
#ax1.set_xlim(0,8)
ax1.legend()


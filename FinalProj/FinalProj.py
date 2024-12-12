#!/usr/bin/env 
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
gf = 12.5 * 25.4 #mm
og = 1.97 * 25.4 #mm
od = 13.4 * 25.4 #mm 
mass_wiper = 3.48 #kg

m_rpm1 = 45 
m_rpm2 = 65
def find_v_wiper1(m_rpm):
    w_m =  m_rpm * np.pi / 180 #convert rpm to rad/s
    v_gx = w_m * og * np.cos(np.radians(52.45))
    v_gy = w_m * og * np.sin(np.radians(52.45))
    w_fd = (v_gy-v_gx * np.tan(np.radians(15.4))) / (fd * (np.sin(np.radians(25.1)) - np.cos(np.radians(25.1)) * np.tan(np.radians(15.4))))
    w_gf = (w_fd * fd * np.cos(25.1 * np.pi/180) - v_gx)/ (gf* np.cos(15.4 * np.pi/180))
    v_fx = v_gx + w_gf * gf * np.cos(15.4 * np.pi/180)
    v_fy = v_gx + w_gf * gf * np.sin(15.4 * np.pi/180)
    v_wiper = w_fd * fd 
    v_wiper *= 1/100 #convert to m/s
    
    return v_wiper 

def find_v_wiper2(m_rpm):
    w_m =  m_rpm * np.pi / 180 #convert rpm to rad/s
    v_gx = w_m * og * np.cos(np.radians(59.4))
    v_gy = w_m * og * np.sin(np.radians(59.4))
    w_fd = (v_gy-v_gx * np.tan(np.radians(17.4))) / (fd * (np.sin(np.radians(180-132.569-17.4)) - np.cos(np.radians(180-132.569-17.4)) * np.tan(np.radians(17.4))))
    w_gf = (w_fd * fd * np.cos((180-32.569-17.4) * np.pi/180) - v_gx)/ (gf* np.cos(17.4 * np.pi/180))
    v_fx = v_gx + w_gf * gf * np.cos(17.4 * np.pi/180)
    v_fy = v_gx + w_gf * gf * np.sin(17.4 * np.pi/180)
    v_wiper = w_fd * fd 
    v_wiper *= 1/100 #convert to m/s
    
    return v_wiper 
def find_a_wiper1():
    t = 1.5 - 0.833 #s
    a_1 = find_v_wiper1(m_rpm1) / t
    return a_1 

def find_a_wiper2():
    t = 1 - 0.5 #s
    a_2 = find_v_wiper2(m_rpm2) / t
    return a_2

def friction():
    F_wiper = mu_k * mass_wiper * g * np.cos(theta)
   
    return F_wiper 

def m_torque(): #find motor torque using acceleration found before 
    a_1 = find_a_wiper1()
    F_c = friction() - (mass_wiper * a_1 )
    t_d1 = fd * F_c # input torque into 4 bar linkage 
    t_motor1 = t_d1 * fd * np.cos(np.radians(90-49.59)) * og * np.sin(np.radians(37.045)) 
    
    a_2 = find_a_wiper2()
    F_c2 = (mass_wiper * a_2) - friction() 
    t_d2 = fd * F_c2 # input torque into 4 bar linkage 
    t_motor2 = t_d2 * fd * np.cos(np.radians(90-42.569)) * og * np.sin(np.radians(42))
    
    t_motor1 *= 1/10000 #convert to nm
    t_motor2 *= 1/10000
    return t_motor1,t_motor2



v_wiper1 = find_v_wiper1(m_rpm1)
print("Wiper velocity at setting 1 = %.3g m/s" %v_wiper1)
v_wiper2 = find_v_wiper2(m_rpm2)
print("Wiper velocity at setting 2 = %.3g m/s"%v_wiper2)
a_1 = find_a_wiper1()
print("Wiper acceleration at setting 1 = %.3g m/s^2"%a_1)
a_2 = find_a_wiper2()
print("Wiper acceleration at setting 2 = %.3g m/s^2"%a_2)
F_wiper1 = friction()
print("Friction = %.3g N"%F_wiper1)
Force1 = mass_wiper * a_1
print("m*a_1 = %.3g N"%Force1)
Force = mass_wiper * a_2
print("m*a_2 = %.3g N"%Force)
t_motor = m_torque()[0]
print("motor torque slow = %.5g Nm"%t_motor)
t_motor2 = m_torque()[1]
print("motor torque fast = %.5g Nm"%t_motor2)



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
"""

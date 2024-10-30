# -*- coding: utf-8 -*-
"""
Dylan Qiu & Clarence Tang & Ethan Chia
Created on Tue Oct 12 07:18:56 2021
Pendulum with Large initial angle
@author: george.sidebotham2
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#INITIAL CONDITIONS
theta_0 = 10.   #deg, initial angle
omega_0 = 0.   #rad/sec released from rest
#INPUT PARAMETERS
L = 0.9     #m, length of pendulum
g = 9.81    #m/s^2, gravity
#DERIVED PARAMETERS
theta_0 = theta_0 * np.pi/180   #rad, unit conversion
tau = 2*np.pi*np.sqrt(L/g)    #s, time constant for small angle pendulum

#DEFINE FUNCTION FOR EQUATIONS OF MOTION
def eom(x,t):
    theta, omega = x
    xdot = np.zeros(2)
    xdot[0] = omega
    xdot[1] = -g/L*np.sin(theta)
    return xdot

#Initial Conditions
x0 = [theta_0, omega_0]

#Define time array
t = np.linspace(0, 10*tau, 1000)
#SOLVE SYSTEM OF EQUATIONS
sol = odeint(eom,x0,t)
theta = sol[:,0]            #rad, extract angle
omega = sol[:,1]            #rad/sec, extract angular speed
T_mg = L*omega**2/g + np.cos(theta)

#FIND PEAKS (brute force method), then frequency
peak_idx= []   #initialize
for i in range(len(theta)-2):
    if theta[i+2] < theta[i+1] and theta[i] < theta[i+1]:
        peak_idx = np.append(peak_idx,i+1)
period = t[int(peak_idx[-1])] - t[int(peak_idx[-2])]   
freq = 1/period
print('frequency = %.4f Hz' %freq)
print('Small Angle frequency = %.4f' %(1/tau))     
print("Maximum Tension = %.3f *mg" %max(T_mg))
#Plot Results
plt.figure(1)
plt.subplot(3,1,1)
plt.plot(t,theta*180/np.pi,label='theta (deg)')
plt.ylabel('Theta (deg)')
plt.subplot(3,1,2)
plt.plot(t,omega, label='omega (rad/s)')
plt.ylabel('Omega (Revs/sec)')
plt.subplot(3,1,3)
plt.plot(t,T_mg)
plt.ylabel("T/mg")
plt.xlabel('time (sec)')  

#Plendulum
#Inputs
l = 1.835 #m
w = 0.0425 #m
t = 0.006 #m
m = 0.226 #kg
def density(l,w,t,m):
    density = m / (l*w*t)
    return density

def I_cm(l,w,t,m):
    i_cm = m*(w**2/12+l**2/12)
    return i_cm

def I_anchor(l,w,t,m):
    Icm = I_cm(l,w,t,m)
    i_anchor = Icm + m * (l/2)**2 
    return i_anchor

theta = theta_0
def T_react(l,w,t,m, theta):
    Ft = m*g*np.sin(theta)
  
    return Ft
def N_react(l,w,t,m, theta):
    Fn = m*g*np.cos(theta)
    print(Fn)
    return Fn
    
def driver():
    density1 = density(l,w,t,m)
    i_cm1 = I_cm(l,w,t,m)
    i_anchor1 = I_anchor(l,w,t,m)
    Ft = T_react(l,w,t,m,theta)
    Fn = N_react(l,w,t,m,theta)
    print('Density = %.4f kg/m^3' %density1)
    print('I_cm = %.4f kg*m^2' %i_cm1)
    print('I_anchor = %.4f kg*m^2' %i_anchor1)
    print('F_t = %.4f N' %Ft)
    print('F_n = %.4f N' %Fn)
    


driver()



# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 13:51:48 2022

@author: michelle.rosen

Dylan Qiu & Jake Peyser ME200
"""

import numpy as np
import matplotlib.pyplot as plt


#Uncomment each function to work on it! 

# CONVERT RADIAL AND TRANSVERSE (COORDINATES, VELOCITY, ACCELERATION) TO CARTESIAN
def RTtoCartesian(val_transverse, val_radial, theta):
    
    val_x =  val_radial *np.cos(theta) - val_transverse * np.sin(theta)
    val_y =  val_radial *np.sin(theta) + val_transverse * np.cos(theta)
    return [val_x,val_y]

#CALCULATE TOTAL TIME IN THE AIR 
def TimeInTheAir(x,y,vx,vy):
     #You can use np.roots or do some algebra to find the solution 
     #If you use roots, make sure to only return ONE solution
     g= 9.81 #m/s^2
     time = (vy+ np.sqrt(vy**2+2*g*y))/g
     return time

# #CALCULATE TRAJECTORY AND RETURN X, Y, VX, AND VY THROUGHOUT
def Trajectory(x0,y0,vx0,vy0,time_list):
     time_list = np.linspace(0,3,1000)
     g= 9.81 #m/s^2
     g_list = [g] * len(time_list)
    
#     #Calculate vx (should be a list of the same length as time_list)
     vx= vx0 * time_list
#     #Calculate x position (use time_list - see if you can avoid for loops!)
     x = x0 + vx * time_list
    
#     #Calculate vy (use time_list - see if you can avoid for loops!)
     vy= vy0 * time_list - 0.5 * g * time_list**2
#     #Calculate y position (use time_list - see if you can avoid for loops!)
     y = y0 + vy * time_list - 0.5 * g * time_list**2
    
     return [x,y,vx,vy]


def PlotTraj(x,y,vx,vy,time):  
    fig0 = plt.figure()
    ax0 =fig0.add_subplot(311)
    ax0.plot(time,vx, label='vx')
    ax0.plot(time,vy, label='vy')
    ax0.set_ylabel("velocity, v [m/s]")
    ax0.set_xlabel('time[s]')
    ax0.legend()
    
    ax1 =fig0.add_subplot(312)
    ax1.plot(time,x, label='x')
    ax1.plot(time,y, label='y')
    ax1.set_ylabel("position [m]")
    ax1.set_xlabel('time[s]')
    ax1.legend()
    
    ax2 =fig0.add_subplot(313)
    ax2.plot(x,y, label='Trajectory')
    ax2.set_ylabel("y position [m]")
    ax2.set_xlabel('x position [m]')
    ax2.legend()
    
    return fig0

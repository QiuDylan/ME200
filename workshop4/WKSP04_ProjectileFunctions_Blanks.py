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
def Trajectory(x0,y0,vx0,vy0, time_list):
     #time_list = np.linspace(0,time,100)
     x0_list = np.full(len(time_list), x0)
     y0_list = np.full(len(time_list), y0)
     vx0_list = np.full(len(time_list), vx0)
     vy0_list = np.full(len(time_list), vy0)
     g = 9.81 #m/s^2
     g_list = np.full(len(time_list), g)

#     #Calculate vx (should be a list of the same length as time_list)
     vx = vx0_list
     
#     #Calculate x position (use time_list - see if you can avoid for loops!)
     x = x0_list + vx * time_list
    
#     #Calculate vy (use time_list - see if you can avoid for loops!)
     vy = vy0_list -  g_list * time_list
#     #Calculate y position (use time_list - see if you can avoid for loops!)
     y = y0_list + vy * time_list - 1/2 * g_list * time_list**2
     
    
     return [x,y,vx,vy]

def PlotTraj(x,y,vx,vy,time_list):
    
    fig0 = plt.figure()
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace= None, hspace=.75)
    
    ax0 =fig0.add_subplot(311)
    ax0.plot(time_list,vx, label='vx')
    ax0.plot(time_list,vy, label='vy')
    ax0.set_ylabel("velocity, v [m/s]")
    ax0.set_xlabel('time[s]')
    
    ax0.legend()
    
    ax1 =fig0.add_subplot(312)
    ax1.plot(time_list,x, label='x')
    ax1.plot(time_list,y, label='y')
    ax1.set_ylabel("position [m]")
#    ax1.set_ylim(0)
    ax1.set_xlabel('time[s]')
    ax1.set_xlim(0)
    ax1.legend()
    
    ax2 =fig0.add_subplot(313)
    ax2.plot(x,y, label='Trajectory')
    ax2.set_ylabel("y position [m]")
 #   ax2.set_ylim(0)
    ax2.set_xlabel('x position [m]')
  #  ax2.set_xlim(0)
    ax2.legend()
    
    return fig0

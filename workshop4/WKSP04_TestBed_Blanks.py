# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 13:55:03 2022

@author: michelle.rosen

Dylan Qiu & Jake Peyser ME200
"""

## IMPORT NECESSARY LIBRARIES
## AS YOU WRITE THESE FUNCTIONS IN PROJECTILE FUNCTIONS, UNCOMMENT THE IMPORT LINE
import numpy as np
import matplotlib.pyplot as plt
from WKSP04_ProjectileFunctions_Blanks import RTtoCartesian
from WKSP04_ProjectileFunctions_Blanks import TimeInTheAir
from WKSP04_ProjectileFunctions_Blanks import Trajectory
from WKSP04_ProjectileFunctions_Blanks import PlotTraj


## TEST YOUR RT TO CARTESIAN CONVERSION ##

#POSITIONS
r= 1
transverse= 0
theta= np.pi/4
[x, y]=RTtoCartesian(transverse, r, theta)
print('x = %.3g' %x)
print('y = %.3g \n' %y)

#VELOCITIES
vr= 1
v_theta= 1
theta= np.pi/4
[vx, vy]=RTtoCartesian(v_theta, vr, theta)
print('vx = %.3g' %vx)
print('vy = %.3g \n' %vy)


# ## TEST YOUR TIME IN THE AIR FUNCTION ##

x= 1#m
y= 1#m
vx=1 #m/s
vy= 1#m/s
t=TimeInTheAir(x,y,vx,vy)
print('t = %.3g \n' %t)


# ##TEST YOUR TRAJECTORY CALCULATION FUNCTION##



x0= 0 #m
y0= 9.81#m
vx0= 0#m/s
vy0= 0 #m/s
time= TimeInTheAir(x0,y0,vx0,vy0)
[x, y,vx, vy]=Trajectory(x0,y0,vx0,vy0,time)

fig1=PlotTraj(x,y,vx,vy,time)
fig1.suptitle('TITLE')

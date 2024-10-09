# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 16:39:54 2021

Dylan Qiu ME200 
Workshop Week 6
Impact and Coefficient of Restitution
@author: Prof. Rosen
"""

import numpy as np
import matplotlib.pyplot as plt

#SETUP VARIABLES 
g = 9.81 #m/s^2 

slo_mo_framerate=240 #fps (check your phone!)
tracker_framerate = 30 #fps (default)

#IMPORT DATA# 

tracker_data = np.genfromtxt("Workshop6_TrackerData.txt" , skip_header= 1, delimiter = "")
tracker_data = np.nan_to_num(tracker_data,nan=0.0)
#remove first three rows of data (you may or may not need this line depending on how tracker uploaded your data - take a look at the first few rows and make sure the time step is constant)
#tracker_data=tracker_data[3:, :]
#tracker_time=tracker_data[:0] #pull out time (will restart at zero later)
tracker_time = np.genfromtxt("Workshop6_TrackerData.txt", skip_header=1, usecols=0)
tracker_x = np.genfromtxt("Workshop6_TrackerData.txt", skip_header=1, usecols=1)
tracker_y = np.genfromtxt("Workshop6_TrackerData.txt", skip_header=1, usecols=2)
#tracker_x = tracker_data[:1]
#tracker_y=tracker_data[:2]
tracker_vx=tracker_data[:3]
tracker_vy=tracker_data[:4]
tracker_ax=tracker_data[:5]
tracker_ay=tracker_data[:6]


print(tracker_time)

tracker_time=tracker_time-tracker_time[0] #reset tracker initial time to zero

dt_tracker=np.diff(tracker_time)[0]

#Plot tracker data
fig1 = plt.figure()
plt.subplot(3,1,1)
plt.plot(tracker_time,tracker_x,label='x')
plt.plot(tracker_time,tracker_y, label='y')
plt.legend()
plt.title('Position')
plt.xlabel('Time [s]')
plt.ylabel('Position [m]')

plt.subplot(3,1,2)
plt.plot(tracker_time,tracker_vx, label='vx')
plt.plot(tracker_time,tracker_vy, label = 'vy')
plt.legend()
plt.title('Velocity')
plt.xlabel('Time [s]')
plt.ylabel('Velocity [m/s]')

plt.subplot(3,1,3)
plt.plot(tracker_time,tracker_ax, label='ax')
plt.plot(tracker_time,tracker_ay, label='ay')
plt.legend()
plt.title('Acceleration')
plt.xlabel('Time [s]')
plt.ylabel('Acceleration [m/s^2]')

#FIND PEAKS AND TROUGHS#
#Use zero crossings of velocity
#use moving average to smooth the velocity data
def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w

window=5 #window for moving average- ADJUST THIS IF THE PEAKS AREN'T DETECTING PROPERLY
smoothed_vy=moving_average(tracker_vy,window) #smooth the velocity data

#plot velocity and smoothed velocity
fig = plt.figure(2)

plt.plot(tracker_time, tracker_vy, label='y velocity')
plt.plot(tracker_time[int((window-1)/2-1):int((-window-1)/2)],smoothed_vy,label='y velocity smoothed')
plt.title('y Velocity and Smoothed y Velocity')
plt.xlabel('Time [s]')
plt.ylabel('Velocity [m/s]')
plt.legend()

#Find peaks (max heights) and bounces 
#You may need to play with some of the smoothing values or how many data points before the zero to work with your own video
zero_crossings_vy = np.where(np.diff(np.sign(smoothed_vy)))[0] #find where v_y crosses zero (hits ground or reaches peak)

#separate into bounces and peaks by looking at the velocity data a few time steps before
tops = []
bounces = [] 
tops=np.append(tops,0)
i=0
for i in range (0, len(zero_crossings_vy)):
    if smoothed_vy[zero_crossings_vy[i]-5]>0: #if velocity before the zero crossing is positive, it's a peak
        tops=np.append(tops,zero_crossings_vy[i])
    else: 
        bounces = np.append(bounces,zero_crossings_vy[i])
    i+=1

tops=tops.astype(int) #convert to integers to use as indices
bounces=bounces.astype(int)

#plot height and the tops/bounces to make sure we got them all - LOOK AT THIS GRAPH
plt.figure(3)
plt.plot(tracker_time,tracker_y, label='Height')
plt.plot(tracker_time[tops],tracker_y[tops],'r.',label='Peaks')
plt.plot(tracker_time[bounces], tracker_y[bounces],'g*',label="Bounces")
plt.title('Peaks and Bounces')
plt.ylabel('Height [m]')
plt.xlabel('Time [m]')
plt.legend()

#CALCULATE COEFFICIENT OF RESTITUTION - MOST WORK SHOULD BE HERE! #
"""
e_vel=
e_avg_vel=

e_height=
e_avg_height=
"""
##SET COR HERE FOR SIMULATION##
#e = ((2*g*h_1)**1/2)/((2*g*h_3)**1/2)





##SIMULATION##
#Initialize variables for simulation
y0=tracker_y[0] #m, intiial drop height (extract from tracker data)
vy0=0 #m/s, initial drop velocity
x0=tracker_x[0] #m, initial x position
vx0=(0.001)/(0.033) #m/s initial x velocity - NOTE: YOU MAY NEED TO ADJUST THIS INDEX
t_fall1 = (2*y0/g)**1/2 #time of bounce
T=tracker_t[:-1] #t-final
Y=tracker_y[:-1] #y-final
X=tracker_x[:-1] #x-final
t1 = np.linspace(0, t_fall1, 1000) #t1
t2 = np.linspace(t_fall1, T, 1000)
v_beforeimpact = (2*g*y0)**(1/2)
v_afterimpact = (2*g*Y)**(1/2)

dt = 0.0005 #timestep (s) for simulation

#drop to first bounce
t_temp = np.arange(0,t1,dt) #set up temporary time array of arbitrary length
y_temp = -0.5*g*t_temp**2+vy0*t_temp+y0 #calculate height 
x_temp= vx0*t_temp+x0 #calculate x position (assume no acceleration)
zero_crossing = np.where(np.diff(np.sign(y_temp)))[0] #find where height crosses zero (hits ground)
t_temp = t_temp[0:zero_crossing[0]] #chop off the end of t_temp after the ball hits the ground (no negative height)
y_temp = y_temp[0:zero_crossing[0]] #chop off the end of y_temp
x_temp = x_temp[0:zero_crossing[0]]

v_beforeimpact = np.append(v_beforeimpact, (y_temp[-1]-y_temp[-2])/dt) #calculate velocity before impact

T=np.append(T,t_temp) #append t_temp to the end of T
Y=np.append(Y,y_temp) #append y_temp to the end of Y
X=np.append(X,x_temp)

#Subsequent bounces
y_ground = 0 #point where the ball bounces - can adjust this to match your video
i = 1 #set up index for bounces
numbounce = 5 #how many bounces to look at

for i in range(1,numbounce):
     
    v_afterimpact=np.append(v_afterimpact,-v_beforeimpact[i-1]*e) #calculate velocity after impact
    
    t_temp = np.arange(0,5,dt) #set up temporary time array of arbitrary length
    y_temp = -0.5*g*t_temp**2+v_afterimpact[i-1]*t_temp+y_ground#calculate height 
    x_temp =  vx0*t_temp+X[-1]
    zero_crossing = np.where(np.diff(np.sign(y_temp)))[0] #find where height crosses zero (hits ground)
    t_temp = t_temp[0:zero_crossing[1]] #chop off the end of t_temp after the ball hits the ground (no negative height). Note: index is 1 because the array always has a 0 first (the way we defined t_temp guarantees it) and we want the other number instead) 
    y_temp = y_temp[0:zero_crossing[1]] #chop off the end of y_temp
    x_temp = x_temp[0:zero_crossing[1]] #chop off the end of x_temp
    
    v_beforeimpact = np.append(v_beforeimpact, (y_temp[-1]-y_temp[-2])/dt) #calculate velocity before impact
    t_temp = t_temp+T[-1]+dt
    T=np.append(T,t_temp) #append t_temp to the end of T
    Y=np.append(Y,y_temp) #append y_temp to the end of Y
    X=np.append(X,x_temp)
    i += 1

#Plot position and trajectory of simulation versus data
plt.figure(4)
plt.subplot(3,1,1)
plt.plot(T,X,label='Simulation')
plt.plot(tracker_time,tracker_x,label='Data')
plt.legend()
plt.title('Simulation vs. Data - Horizontal Distance')
plt.ylabel('x Distance [m]')
plt.xlabel('Time [s]')

plt.subplot(3,1,2)
plt.plot(T,Y,label='Simulation')
plt.plot(tracker_time,tracker_y,label='Data')
plt.legend()
plt.title('Height')
plt.ylabel('Height[m]')
plt.xlabel('Time [s]')

plt.subplot(3,1,3)
plt.plot(X,Y,label='Simulation')
plt.plot(tracker_x,tracker_y,label='Data')
plt.legend()
plt.ylabel('Height[m]')
plt.xlabel('x Distance [m]')
plt.title('Trajectory')

#Find velocity and accelerations of simulation data 
VX=np.diff(X)/dt
VY=np.diff(Y)/dt

AX=np.diff(VX)/dt
AY=np.diff(VY)/dt

#Plot velocity and acceleration versus data
fig5 = plt.figure()
plt.subplot(2,2,1)
plt.plot(T[1:],VX,label='Sim')
plt.plot(tracker_time,tracker_vx,label='Data')
plt.legend()
plt.title('vx')
plt.ylabel('vx [m/s]')
plt.xlabel('Time [s]')

plt.subplot(2,2,3)
plt.plot(T[1:],VY,label='Sim')
plt.plot(tracker_time,tracker_vy,label='Data')
plt.legend()
plt.title('vy')
plt.ylabel('vy [m/s]')
plt.xlabel('Time [s]')

plt.subplot(2,2,2)
plt.plot(T[2:],AX,label='Sim')
plt.plot(tracker_time,tracker_ax,label='Data')
plt.legend()
plt.title('ax')
plt.ylabel('ax [m/s^2]')
plt.xlabel('Time [s]')

plt.subplot(2,2,4)
plt.plot(T[2:],AY,label='Sim')
plt.plot(tracker_time,tracker_ay,label='Data')
plt.legend()
plt.title('ay')
plt.ylabel('ay [m/s^2]')
plt.xlabel('Time [s]')
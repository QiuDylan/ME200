#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 11:20:35 2024

@author: dylanqiu
"""

from sympy.physics.mechanics import dynamicsymbols, ReferenceFrame, Point, RigidBody, inertia, KanesMethod, mechanics_printing, mlatex
from sympy import symbols, diff, simplify, lambdify, solve
from scipy.optimize import fsolve
from numpy import array, linspace, rad2deg, deg2rad, append, interp
import numpy as np
from numpy.linalg import pinv, inv
from scipy.integrate import odeint, solve_ivp
from scipy.optimize import fmin
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import display, Latex

l1 = 0.25
l2 = 1
l3 = 1
a1 = np.pi/2
dy = 0
dx = 0.95
Fbar = lambda a1,x: np.array([l1*np.sin(a1)+l2*np.sin(x[0])-l3*np.sin(x[1])-dy,
                           l1*np.cos(a1)+l2*np.cos(x[0])-l3*np.cos(x[1])-dx])

a1 = np.linspace(0, 2*np.pi)
a2 = np.zeros(len(a1))
a3 = np.zeros(len(a1))
xsol = np.array([0, np.pi/4])
for i in range(len(a1)):
    xsol = fsolve(lambda x: Fbar(a1[i], x), xsol)
    a2[i] = xsol[0]
    a3[i] = xsol[1]
"""    
plt.plot(a1, a2, label = r'$\theta_2$')
plt.plot(a1, a3, label = r'$\theta_3$')
plt.xlabel(r'$\theta_1$ (radian)')
plt.ylabel('output angle (radian)')
plt.legend()

rA = l1*np.vstack([np.cos(a1), np.sin(a1)])
rB = rA + l2*np.vstack([np.cos(a2), np.sin(a2)])
rC = rB - l3*np.vstack([np.cos(a3), np.sin(a3)])
rP = rA + l2/2*np.vstack([np.cos(a2), np.sin(a2)])
links_x_locations = np.vstack([np.zeros(len(a1)), 
                              rA[0, :],
                              rB[0, :],
                              rC[0, :]])
links_y_locations = np.vstack([np.zeros(len(a1)), 
                              rA[1, :],
                              rB[1, :],
                              rC[1, :]])
i = 10
plt.plot(links_x_locations[:, i], 
        links_y_locations[:, i], 'k-o')
plt.plot(rA[0,:], rA[1,:], label = 'hinge A')
plt.plot(rB[0,:], rB[1,:], label = 'hinge B')
plt.plot(rC[0,:], rC[1,:], label = 'hinge C')
plt.plot(rP[0,:], rP[1,:], label = 'midpoint AB')
plt.legend()
plt.title('Paths and orientation for\n'+ 
          r'$\theta_1$ = {:.1f}, $\theta_2$ = {:.1f}, $\theta_3$ = {:.1f}'.format(a1[i], a2[i], a3[i]))
plt.axis('equal');
"""
drive_rate = 10 #rad/s
dFbar = lambda a1, a2, a3, dx: np.array([l1*drive_rate*np.sin(a1)+\
                                         l2*dx[0]*np.sin(a2)-\
                                         l3*dx[1]*np.sin(a3),\
                                         l1*drive_rate*np.cos(a1)+\
                                         l2*dx[0]*np.cos(a2)-\
                                         l3*dx[1]*np.cos(a3)])

da1 = np.ones(len(a1))*10
da2 = np.zeros(len(a1))
da3 = np.zeros(len(a1))
xsol = np.array([0, 0])
plt.plot(a1, da1, label = r'$\dot{\theta}_1$')
plt.plot(a1, da2, label = r'$\dot{\theta}_2$')
plt.plot(a1, da3, label = r'$\dot{\theta}_3$')
plt.legend()
plt.xlabel(r'$\theta_1$ (radian)')
plt.ylabel('output angular speed (radian/s)')

for i in range(len(a1)):
    xsol = fsolve(lambda dx: dFbar(a1[i], a2[i], a3[i], dx), xsol)
    da2[i] = xsol[0]
    da3[i] = xsol[1]
    













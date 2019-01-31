# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 15:07:29 2019

@author: toabi
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

choice = np.array([0,1])
prob = [0.995,0.005]

A = np.array([[0,0,0,0,0,0,0],
             [0,0,0,1,0,0,0],
             [0,1,0,1,0,0,0],
             [0,0,1,1,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0]])

B = np.random.randint(2, size=(50, 50))
Z = np.random.choice(choice,size = (500,500),p=prob)
print(Z)

def animate(i):
    def iterate(Z):
        # Count neighbours
        N = (Z[0:-2,0:-2] + Z[0:-2,1:-1] + Z[0:-2,2:] +
             Z[1:-1,0:-2]                + Z[1:-1,2:] +
             Z[2:  ,0:-2] + Z[2:  ,1:-1] + Z[2:  ,2:])
        
        #rules
        birth = ((N==2) | (N==6))& (Z[1:-1,1:-1]==0)
        survive = ((N==2) | (N==3)) & (Z[1:-1,1:-1]==1)
        Z[...] = 0
        Z[1:-1,1:-1][birth | survive] = 1
        return Z

    
    iterate(Z)
    p.set_data(Z)
       
    
fig = plt.figure()
p = plt.imshow(Z,interpolation='nearest', animated = True)
plt.set_cmap('summer')

ani = animation.FuncAnimation(fig, animate, interval=1)
plt.show()

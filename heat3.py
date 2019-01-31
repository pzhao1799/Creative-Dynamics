# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 15:58:58 2019

@author: toabi
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

N=128
A= np.zeros((N,N))
A[30:40,0] = 100
A[-1,115:120]= -100
A[0,70:80]= -100
A[60:80,-1]= 100

 
# Display it
fig = plt.figure()
p = plt.imshow(A, interpolation='nearest',animated = True)
plt.set_cmap('OrRd')

 
eps= 0.9
def animate(i):
    Aold= np.copy(A)         
    
    A[1:N-1,1:N-1]= (1-eps)*Aold[1:N-1,1:N-1] + eps*( Aold[1:N-1,0:N-2] + Aold[1:N-1,2:N] + Aold[0:N-2,1:N-1] + Aold[2:N,1:N-1] )/4.0 
            
    A[:,0]   = A[:,1]   
    A[:,-1] = A[:,-2]   
    A[0,:]   = A[1,:]   
    A[-1,:] = A[-2,:]   

    A[30:100,0] = 100
    A[-1,115:120]= -100
    A[0,70:80]= -100
    A[60:80,-1]= 100

    p.set_data(A)
    
ani = animation.FuncAnimation(fig, animate, interval=1)
plt.show()
 
   
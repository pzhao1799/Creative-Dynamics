# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 11:56:28 2019

@author: toabi
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 08:46:58 2019

@author: stewjo
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

def f(u,v):
    a= 0.75
    b= 0.0006
    rho= 17   # 1/epsilon 
    return rho*u*(1.0-u)*(u-(v+b)/a)

def g(u,v):
    return u-v

def wrap(A):    
    # wrap
    A[:,0]= A[:,-4]
    A[:,1]= A[:,-3]
    
    A[:,-2]= A[:,2]
    A[:,-1]= A[:,3]
    
    A[0,:]= A[-4,:]
    A[1,:]= A[-3,:]
    
    A[-2,:]= A[2,:]
    A[-1,:]= A[3,:]

    return A    

N= 128 
U= np.random.rand(N,N)
V= np.random.rand(N,N)
wrap(U)
wrap(V)
U[55:69,1] = 0.95
#U[20:22,31:33] = 0.95
U[20:30,37:38] = 0.95  
U[105:107,81:83] = 0.95  




# Display it
fig = plt.figure()
p = plt.imshow(U, interpolation='nearest',animated = True)
plt.set_cmap('viridis')
 

deps= 0.1
eps= 0.1
def animate(i):
    # diffuse     
    Uold= np.copy(U)
    U[1:N-1,1:N-1]= (1-eps)*Uold[1:N-1,1:N-1] + deps*( Uold[1:N-1,0:N-2] + Uold[1:N-1,2:N] + Uold[0:N-2,1:N-1] + Uold[2:N,1:N-1] )/4.0 

    # react         
    Uold= np.copy(U)
    Vold= np.copy(V)
    U[1:N-1,1:N-1]= Uold[1:N-1,1:N-1] + eps*f(Uold[1:N-1,1:N-1],Vold[1:N-1,1:N-1])
    V[1:N-1,1:N-1]= Vold[1:N-1,1:N-1] + eps*g(Uold[1:N-1,1:N-1],Vold[1:N-1,1:N-1])
    #V[0,:]= V[-1,:] = 0
    #V[:,0]= V[:,-1] = 0
    #U[0,:]= U[-1,:] = 0
    #U[:,0]= U[:,-1] = 0
    wrap(U)
    wrap(V)
    U[55:69,1] = 0.95
    #U[20:22,31:33] = 0.95
    U[20:30,37:38] = 0.95  
    U[105:107,81:83] = 0.95    
    p.set_data(U)
    
    
ani = animation.FuncAnimation(fig, animate, interval=1)
plt.show()
 
   
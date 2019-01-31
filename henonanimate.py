# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 15:16:53 2019

@author: toabi
"""
from matplotlib import pyplot as plt
from matplotlib import animation
#import numpy as np
from numba import jit

# parameters
a = 1.4
b = 0.3
frame = 1000

#chaos lists
X, Y = [], []
X2, Y2 = [], []

#initial values
delta = 2.2250738585072014e-10
x0 = 0.1
y0 = 0.1
x1 = 0.1 + delta
y1 = 0.1 + delta
    
#graph
fig = plt.figure()
plt.xlim(-1.5,1.5)
plt.ylim(-0.5,0.5)
graph, = plt.plot([],[],'r1',markersize = 30)
graph2, = plt.plot([],[],'b2',markersize = 30)

# Henon Map function
@jit
def henonMap(x,y):
    xnew = 1-a*x*x+y
    ynew = b*x
    return xnew, ynew

for i in range(frame):
    xi, yi = henonMap(x0,y0)
    xi2, yi2 = henonMap(x1,y1)
    X.append(xi)
    Y.append(yi)
    X2.append(xi2)
    Y2.append(yi2) 
    x0, y0 = xi, yi
    x1, y1 = xi2, yi2

def animateA(i):
    graph2.set_data(X2[i+10], Y2[i+10])
    return graph2

def animateB(i):
    graph.set_data(X[i+10], Y[i+10])
    return graph

#plt.plot(X, Y, color='black', s=5)
#ax.scatter(X2, Y2, color='blue', s=5)
#plt.savefig('henon.png', dpi = 1000)
anim = []
anim.append(animation.FuncAnimation(fig,animateA, interval = 100))
anim.append(animation.FuncAnimation(fig,animateB, interval = 100))
#anim.save('henonanimate.gif', writer='imagemagick', fps=30)
plt.show()
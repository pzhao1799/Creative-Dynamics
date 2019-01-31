# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 19:50:31 2019

@author: toabi
"""
from matplotlib import pyplot as plt
import numpy as np

# parameters
x0 = np.random.random()
y0 = np.random.random()
u = 0.9
t = 0.4-6/(1+(x0**2)+(y0**2))

# Ikeda Map function
def ikedaMap(x,y,u,t):
    xnew = 1+u*(x*np.cos(t)-y*np.sin(t))
    ynew = u*(x*np.sin(t)+y*np.cos(t))
    return xnew, ynew

X, Y = [], []

for i in range(100000):
    xi, yi = ikedaMap(x0,y0,u,t)
    X.append(xi)
    Y.append(yi)
    x0, y0 = xi, yi

fig, ax = plt.subplots(figsize=(8,8))
ax.scatter(X, Y, color='red', s=0.2)
plt.savefig('ikeda.png', dpi = 1000)
plt.show()
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 09:37:03 2019

@author: toabi
"""

import matplotlib.pyplot as plt
#from matplotlib import animation
import numpy as np

fig = plt.subplots(figsize=(10,10))

def equationA(a,b,x,y,eps):
    return x + eps*(a*x+b*y)

def equationB(c,d,x,y,eps):
    return y + eps*(c*x+d*y)

m = 2
a = np.random.uniform(-m,m)
b = np.random.uniform(-m,m)
c = np.random.uniform(-m,m)
d = np.random.uniform(-m,m)

iteration = 1000
eps = 0.01

for k in range(iteration):
    X = [np.random.uniform(-1,1)]
    Y = [np.random.uniform(-1,1)]
    for i in range(20):
        xnew = equationA(a,b,X[i],Y[i],eps)
        ynew = equationB(c,d,X[i],Y[i],eps)
        X.append(xnew)
        Y.append(ynew)

    plt.plot(X, Y, 'b-',) 

plt.show()
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 15:24:44 2019

@author: toabi
"""
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(8,8))

def logistic(r,x):
    return r*x*(1-x)

r = np.linspace(0,4,10000)

x = 0.0001

for n in range(1000):
    x = logistic(r,x)
    ax.plot(r,x,',r',alpha = 0.25)

ax.set_xlim(2.5, 4)
plt.savefig('bifurcate.png', dpi = 1000)
plt.show()

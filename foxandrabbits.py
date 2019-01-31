# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 15:25:16 2019

@author: toabi
"""

import matplotlib.pyplot as plt
import numpy as np

def logistic(x):
    return x + 0.0001*(1 - (2 * x))

fig, ax = plt.subplots(figsize=(10,10))

t = range(-10000,10000)
x = 0
X = []

for i in t:
    x = logistic(x)
    X.append(x)
    
ax.set_xlim(-10000, 10000)
ax.set_ylim(0,0.5)
plt.plot(t,X)
plt.show()
    
    
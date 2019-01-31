# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 15:16:53 2019

@author: toabi
"""
from matplotlib import pyplot as plt

# parameters
a = 1.4
b = 0.3

# Henon Map function
def henonMap(x,y):
    xnew = 1-a*x*x+y
    ynew = b*x
    return xnew, ynew

delta = 2.2250738585072014e-308
x0 = 0.1 - delta
y0 = 0.1 - delta

X, Y = [], []
for i in range(1000):
    xi, yi = henonMap(x0,y0)
    X.append(xi)
    Y.append(yi)
    x0, y0 = xi, yi

fig, ax = plt.subplots(figsize=(8,8))
ax.scatter(X, Y, color='red', s=0.2)
plt.savefig('henon.png', dpi = 1000)
plt.show()
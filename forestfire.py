# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 20:05:36 2019

@author: toabi
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import colors
from numba import jit

neighbours = ((-1,-1), (-1,0), (-1,1), (0,-1), (0, 1), (1,-1), (1,0), (1,1))
EMPTY = 0
TREE = 1
FIRE = 2
ROCK = 3

colors_list = [(0,0,0), (0,0.7,0), (1,0,0), (1,1,1), 'white']
cmap = colors.ListedColormap(colors_list)
bounds = [0,1,2,3,4]
norm = colors.BoundaryNorm(bounds, cmap.N)

@jit
def iterate(X):

    #A burning cell turns into an empty cell
    #A tree will burn if at least one neighbor is burning
    #A tree ignites with probability f even if no neighbor is burning
    #An empty space fills with a tree with probability p
    
    X1 = np.zeros((ny, nx))
    for ix in range(1,nx-1):
        for iy in range(1,ny-1):
            if X[iy,ix] == EMPTY and np.random.random() <= p:
                X1[iy,ix] = TREE
            if X[iy,ix] == TREE:
                X1[iy,ix] = TREE
                for dx,dy in neighbours:
                    if X[iy+dy,ix+dx] == FIRE:
                        X1[iy,ix] = FIRE
                        break
                else:
                    if np.random.random() <= f:
                        X1[iy,ix] = FIRE
            if X[iy,ix] == ROCK:
                X1[iy,ix] = ROCK

    return X1

# initial population density
forest_fraction = 0.1
rock_fraction = 0.02

#new tree
p = 0.005

#fire  probabibility
f = 0.00005

#dimensions
nx = 250 
ny = 250

X  = np.zeros((ny, nx))
X[1:ny-1, 1:nx-1] = np.random.randint(0, 2, size=(ny-2, nx-2))
X[1:ny-1, 1:nx-1] = np.random.random(size=(ny-2, nx-2)) < forest_fraction
#X[1:ny-1, 1:nx-1] = np.random.random(size=(ny-2, nx-2)) < rock_fraction

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
ax.set_axis_off()
im = ax.imshow(X, cmap=cmap, norm=norm)

@jit
def animate(i):
    im.set_data(animate.X)
    animate.X = iterate(animate.X)

animate.X = X

anim = animation.FuncAnimation(fig, animate, interval = 100)
plt.show()
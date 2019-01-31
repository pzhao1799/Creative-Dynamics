# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 18:09:12 2019

@author: toabi
"""
import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D


def rossler(x, y, z, a=0.2, b=0.2, c=5.7):
    x_dot = -y-z
    y_dot = x+a*y
    z_dot = b+z*(x-c)
    return x_dot, y_dot, z_dot


dt = 0.01
stepCnt = 100000

# Need one more for the initial values
xs = np.empty((stepCnt + 1,))
ys = np.empty((stepCnt + 1,))
zs = np.empty((stepCnt + 1,))

# Setting initial values
xs[0], ys[0], zs[0] = (0., 1., 1.05)

# Stepping through "time".
for i in range(stepCnt):
    # Derivatives of the X, Y, Z state
    x_dot, y_dot, z_dot = rossler(xs[i], ys[i], zs[i])
    xs[i + 1] = xs[i] + (x_dot * dt)
    ys[i + 1] = ys[i] + (y_dot * dt)
    zs[i + 1] = zs[i] + (z_dot * dt)

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot(xs, ys, zs, lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Rossler Attractor")
plt.savefig('rosslerstatic.png', dpi = 1000)
plt.show()
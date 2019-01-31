# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 16:10:17 2019

@author: toabi
"""

from matplotlib import pyplot as plt
import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import animation

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1], projection='3d')
ax.axis('off')

def lorenz(x, y, z, s=10, r=28, b=2.667):
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot

def update(num, data, line):
    line.set_data(data[:2, :num])
    line.set_3d_properties(data[2, :num])

dt = 0.01
stepCnt = 10000

xs = np.zeros((stepCnt + 1,))
ys = np.zeros((stepCnt + 1,))
zs = np.zeros((stepCnt + 1,))

xs2 = np.zeros((stepCnt + 1,))
ys2 = np.zeros((stepCnt + 1,))
zs2 = np.zeros((stepCnt + 1,))

xs[0], ys[0], zs[0] = (3, 3, 3)
xs2[0], ys2[0], zs2[0] = (3.01, 3.01, 3.01)

for i in range(stepCnt):
    x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i])
    xs[i + 1] = xs[i] + (x_dot * dt)
    ys[i + 1] = ys[i] + (y_dot * dt)
    zs[i + 1] = zs[i] + (z_dot * dt)
    x_dot2, y_dot2, z_dot2 = lorenz(xs2[i], ys2[i], zs2[i])
    xs2[i + 1] = xs2[i] + (x_dot2 * dt)
    ys2[i + 1] = ys2[i] + (y_dot2 * dt)
    zs2[i + 1] = zs2[i] + (z_dot2 * dt)
    
N = 100000
data = np.dstack((xs,ys,zs)).squeeze().T
data2 = np.dstack((xs2,ys2,zs2)).squeeze().T
line, = ax.plot(data[0, 0:1], data[1, 0:1], data[2, 0:1],'r-')
line2, = ax.plot(data2[0, 0:1], data2[1, 0:1], data2[2, 0:1],'b-')

ax.set_xlim3d([-20, 20])
#ax.set_xlabel('X')

ax.set_ylim3d([-30, 30])
#ax.set_ylabel('Y')

ax.set_zlim3d([5, 40])
#ax.set_zlabel('Z')

ani = []
ani.append(animation.FuncAnimation(fig, update, N, fargs=(data, line), interval=1, blit=False))
ani.append(animation.FuncAnimation(fig, update, N, fargs=(data2, line2), interval=1, blit=False))
#ani.save('lorenz.gif', writer='imagemagick', fps=30)
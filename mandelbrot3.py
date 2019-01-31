# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 12:21:00 2019

@author: toabi
"""

import numpy as np
from numba import jit
from matplotlib import pyplot as plt
from matplotlib import colors
from matplotlib.widgets import Slider
 
image_counter = 0

@jit
def mandelbrot(z,maxiter,horizon,log_horizon):
    c = z
    for n in range(maxiter):
        az = abs(z)
        if az > horizon:
            return n - np.log(np.log(az))/np.log(2) + log_horizon
        z = z*z + c
    return 0

@jit
def mandelbrot_set(xmin,xmax,ymin,ymax,width,height,maxiter):
    horizon = 2.0 ** 40
    log_horizon = np.log(np.log(horizon))/np.log(2)
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width,height))
    for i in range(width):
        for j in range(height):
            n3[i,j] = mandelbrot(r1[i] + 1j*r2[j],maxiter,horizon, log_horizon)
    return (r1,r2,n3)

def mandelbrot_image(xmin,xmax,ymin,ymax,width=20,height=20,\
                     maxiter=1024,cmap='jet',gamma=0.3):
    dpi = 72
    img_width = dpi * width
    img_height = dpi * height
    x,y,z = mandelbrot_set(xmin,xmax,ymin,ymax,img_width,img_height,maxiter)
    fig, ax = plt.subplots(figsize=(width, height),dpi=72)
    plt.axis("off")
    norm = colors.PowerNorm(gamma)
    ax.imshow(z.T,cmap=cmap,origin='lower',norm=norm)  
    
    save_image(fig)
    
def save_image(fig):
    global image_counter
    filename = "mandelbrodt_%d.png" % image_counter
    image_counter += 1
    fig.savefig(filename,bbox_inches = 'tight')
    
mandelbrot_image(-2.0,0.5,-1.25,1.25,cmap='viridis')
#mandelbrot_image(0.3,0.4,-0.125,0,cmap='jet')
#mandelbrot_image(-0.77,-0.76,0.09,0.1,cmap='jet')
#mandelbrot_image(0.25,0.5,0.25,0.5,cmap='jet')
#mandelbrot_image(0.35,0.45,0.3,0.4,cmap='jet')
#mandelbrot_image(0.44,0.445,0.3725,0.3775,cmap='jet')

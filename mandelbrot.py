# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 11:46:05 2019

@author: toabi
"""

from PIL import Image

w = 1920
h = 1080
zoom = 2

image = Image.new("RGB",(w,h))
pixel = image.load()

cx,cy = 0.1015,-0.633
maxIter = 50

for x in range(w):
    for y in range(h):
        zx = 1.5*(x - w/2)/(0.5*zoom*w) 
        zy = 1.0*(y - h/2)/(0.5*zoom*h)
        z = zx + zy * 1j
        c = z
        for i in range(maxIter):
            if abs(z) > 2:
                break
            z = z * z + c
            
        pixel[x,y] = (i << 21) + (i << 10) + i*8

image.save('mandelbrot.png')
image.show()
        
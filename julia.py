# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 11:46:05 2019

@author: toabi
"""
from PIL import Image

w = 1920
h = 1080
zoom = 6

image = Image.new("RGB",(w,h))

cx,cy = -0.7269,0.1889
maxIter = 255

for x in range(w):
    for y in range(h):
        zx = 1.5*(x - w/2)/(0.5*zoom*w) 
        zy = 1.0*(y - h/2)/(0.5*zoom*h)
        i = 0
        while zx*zx + zy*zy < 4 and i < maxIter:
            temp = zx*zx - zy*zy
            zy = 2.0 * zx * zy + cy
            zx = temp + cx
            i+=1
            
        image.putpixel((x, y), (i << 21, i << 10, i * 8))

#image.save('julia.png')
image.show()
        
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 17:45:28 2019

@author: toabi
"""
from PIL import Image

xa = -2.0
xb = 1.0
ya = -1.5
yb = 1.5
  
maxIt = 255 
  
imgx = 10000
imgy = 10000
image = Image.new("RGB", (imgx, imgy)) 
  
for y in range(imgy): 
    for x in range(imgx): 
        zy = y * (yb - ya) / (imgy - 1)  + ya 
        zx = x * (xb - xa) / (imgx - 1)  + xa 
        z = zx + zy * 1j
        c = z 
        for i in range(maxIt): 
            if abs(z) > 2.0: break
            z = z * z + c 
        image.putpixel((x, y), (i % 4 * 64, i % 8 * 32, i % 16 * 16)) 
  
image.save('mandelbrot2.png')    
image.show() 
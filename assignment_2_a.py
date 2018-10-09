# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 16:06:13 2018

@author: Max Marder
"""
import random as rand

i_range = 100

count = 0 
  
for i in range(i_range):
    
    x = rand.uniform(0.0, 1.0)
    ##TEST
    print("\nx =", x)
    y = rand.uniform(0.0, 1.0)
    ##TEST
    print("y =", y)
    z = rand.uniform(0.0, 1.0)
    ##TEST
    print("z =", z)
    
    a = x < 1/3 or y < 1/3 or z < 1/3
    b = (x >= 1/3 and x < 2/3) or (y >= 1/3 and y < 2/3) or (z >= 1/3 and z < 2/3)
    c = x > 2/3 or y > 2/3 or z > 2/3
    
    # if x,y,z occupy each third respectively increment count
    if (a and b and c):
        count += 1
        
    ## TEST
    print("\niteration =", i)
    print("count =", count)

        
print("\n", 100.0 * count / i_range, sep = "")
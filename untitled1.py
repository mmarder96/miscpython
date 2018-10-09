# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 16:34:10 2018

@author: Max Marder
"""
import random as rand

n = 5

count = 0

for i in range(n):
    x1 = 3*rand.uniform(0.0, 1.0)
    ## TEST
    print("x1 =", x1)
    
    x2 = 3*rand.uniform(0.0, 1.0)
    ## TEST
    print("x2 =", x2)
    
    y2 = x1 - 1.5
    ## TEST
    print("y2 =", y2)
    
    z2 = x2 - 1.5
    ## TEST
    print("z2 =", z2)
    
    m = y2*y2;
    ## TEST
    print("m =", m)
    
    if (m + z2*z2 < 2.25):
      count += 1

    print(count/n)
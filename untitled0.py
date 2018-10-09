# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 16:06:13 2018

@author: Max Marder
"""
import random as rand

n = 5

count = 0 
  
for i in range(n):
    
    x1 = rand.uniform(0.0, 1.0)
    x2 = rand.uniform(0.0, 1.0)
    x3 = rand.uniform(0.0, 1.0)
    
    print(count)
    
    if (x1 < 1/3 and x2 >= 1/3 and x2 < 2/3 and x3 > 2/3):
        count += 1
        
    elif (x2 < 1/3 and x1 >= 1/3 and x1 < 2/3 and x3 > 2/3):
        count += 1
        
    elif (x3 < 1/3 and x2 >= 1/3 and x2 <=2/3 and x1 > 2/3):
        count += 1
        
    elif (x1 < 1/3 and x3 >= 1/3 and x3 < 2/3 and x2 > 2/3):
        count += 1
        
    elif (x2 < 1/3 and x3 >= 1/3 and x3 < 2/3 and x1 > 2/3):
        count += 1
        
    elif (x3 < 1/3 and x1 >= 1/3 and x1 < 2/3 and x2 > 2/3):
        count += 1
        
    print(100.0 * count / n)
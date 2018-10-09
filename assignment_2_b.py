# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 16:34:10 2018

@author: Max Marder
"""
import random as rand

i_range = 100

count = 0

for i in range(i_range):
    
    ## TEST print iteration
    print("\niteration =", i+1)
    ## TEST print count
    print("count =", count)
    
    # generate a random number between 3.0 and -1.5
    y = 3*rand.uniform(0.0, 1.0) - 1.5
    ## TEST
    print("\ny =", y)
    
    # generate a random number between 3.0 and -1.5
    z = 3*rand.uniform(0.0, 1.0) - 1.5
    ## TEST
    print("z =", z)
    
    # square the random number y
    m = y**2
    ## TEST
    print("\nm =", m)
    
    # square the random number z
    n = z**2
    ## TEST
    print("n =", n)
    
    if (m + n < 2.25):
      count += 1
    ## TEST
    print("\nm + n =", m + n)    
    
    # print percent m + n < 2.25 as a decimal
    print("\npercent: ", count/i_range, sep = "")
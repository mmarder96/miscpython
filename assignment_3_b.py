# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 16:34:10 2018

@author: Max Marder
"""
import random as rand

def zesty_test(i_range):
    
    # count number of successes
    count = 0
    
    for i in range(i_range):
        
        # generate a random number between 3.0 and -1.5
        y = 3*rand.uniform(0.0, 1.0) - 1.5
        
        # generate a random number between 3.0 and -1.5
        z = 3*rand.uniform(0.0, 1.0) - 1.5
        
        # square the random number y
        m = y**2
        
        # square the random number z
        n = z**2
        
        if (m + n < 2.25):
          count += 1   
        
    # print percent m + n < 2.25 as a decimal
    print("\npercent: ", count/i_range * 100, sep = "")

zesty_test(10000)
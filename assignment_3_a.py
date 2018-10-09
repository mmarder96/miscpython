# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 16:24:48 2018

@author: Max Marder
"""
import random as rand
import math

def bucket(n, i_range):
        
    # count number of succeses
    count = 0

    for i in range(i_range):
        # frequerncy list of size n
        freq = [0] * n
        for j in range(n):
            freq[math.floor(rand.uniform(0.0, 1.0) * n)] += 1
        if all(p == 1 for p in freq):
            count += 1 
    
    print("percent:", count/i_range * 100)

bucket(3, 10000)
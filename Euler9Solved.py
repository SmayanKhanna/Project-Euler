#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 14:52:41 2021

@author: Smayan
"""

import math
import random


def Is_Triplet(a,b):
    
    c = math.sqrt(a**2 + b**2)
    
    if c - int(c) == 0:
        return True
    else:
        return False 

def TripletFinder(tot):

    a = list(range(10000))
    b = list(range(10000))
    
    random.shuffle(a)
    random.shuffle(b)
    for i in a:
        for x in b:
            if Is_Triplet(i, x) == True:
                c = math.sqrt(i**2 + x**2)
                if i + x + c == tot:
                    print(i*x*c)
                else:
                    continue
            else:
                continue
        
TripletFinder(1000)
    
    
    
    
    
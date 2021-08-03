#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 22:34:45 2021

@author: Smayan
"""

def SumSquared(n):
    
    list_1 = [n]
    
    while n > 1:
            
        n = n - 1
        list_1.append(n)
       
    list_1.reverse()
    
    answer = sum(list_1) ** 2
    return answer

def SquaredSum(n):
    
    list_2 = [n**2]
    
    while n > 1:
        
        n = n - 1
        square = n ** 2
        list_2.append(square)
        
    answer = sum(list_2)
    return answer 
    
print(SumSquared(100) - SquaredSum(100))




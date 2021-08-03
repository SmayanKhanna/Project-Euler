#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 19:09:31 2021

@author: Smayan
"""

def is_prime(n):
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def Sum(n):
    sum_prime = 0
    for i in range(2,n):
        if is_prime(i) == True:
            sum_prime += i
            
    return sum_prime

print(Sum(2000000))
            
        

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 16:57:35 2021

@author: Smayan
"""
def Finder(num):
    
    list_1 = [num]
    
    div_all = False 
    
    divcheck = 1
    
    value = 1
    
    n = 1
    
    while num > 1:
            
        num = num - 1
        list_1.append(num)
       
    list_1.reverse()
     
    while div_all == False:
        
        for i in list_1[0:n]:
            
            if n > len(list_1):
                break 
            
            if value % i == 0:
                n += 1
                divcheck += 1
                value += 1
            else:
                divcheck -= 1
                n += 1
            
        if divcheck == num:
            div_all = True
            return value 
           
print(Finder(4))
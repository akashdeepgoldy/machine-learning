# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 13:37:12 2019

@author: Akash
"""
list = [64,25,12,22,11]
a = len(list)
for i in range(a):
    for j in range(1, a-i-1):
        if list[j] > list[j+1]:          
            
            list[j], list[j+1] = list[j+1], list[j]
            
    print("%d" %list[i])
    
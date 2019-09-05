# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 12:33:30 2019

@author: Akash
"""

list = [64,25,12,22,11]
a = len(list)
#print(list[4])   
for i in range(a):
    key = list[i]
    #print(key)
    for j in range(i+1,a):
        if key > list[j]:
            key = list[j]
            index = j
    print(key, index)
    
    var = list[i]
    list[i] = list[index]
    list[index] = var 
    
print(list)
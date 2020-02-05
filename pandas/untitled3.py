# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 18:19:43 2020

@author: Harry
"""

def sortedSquares(A):
        new_list = []
        for num in A:
            num_list = num**2
            
            new_list.append(num_list)
            
        new_list.sort()
        
        return new_list
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 15:56:11 2020

@author: Harry
"""

# 1 储存数据
import json
numbers = [2,3,5,7,11,13]

filename = 'numbers.json'
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)
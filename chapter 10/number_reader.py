# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 15:59:10 2020

@author: Harry
"""

import json
filename= 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)
    #使用函数json.load()加载储存在numbers.json中的信息
print(numbers)
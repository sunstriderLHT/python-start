# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 18:52:11 2019

@author: Administrator
"""

#元组——不可变的列表使用圆括号而不是方括号
dimensions = (200,50)
for dimension in  dimensions:
    print(dimension)
#修改元组可以通过重新定义整个元组
dimensions = (400,100)
for dimension in dimensions:
    print(dimension)
print("\n")

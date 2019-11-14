# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 17:33:35 2019

@author: Administrator
"""
#使用sort()方法对列表进行永久性排序
cars = ['bmw','audi','toyota','subaru']
cars.sort()#正向字母排序
print(cars)

cars.sort(reverse = True)#反向字母排列
print(cars)

#使用sorted()对列表进行临时排序
cars = ['bmw','audi','toyota','subaru']
print("Here is the original list:")
print(cars)

print("Here is the sorted list:")
print(sorted(cars))

print("Here is the original list again:")
print(cars)
# 调用sorted()函数后原始列表并没有改变

#倒着打印,reverse 是永久修改列表
cars.reverse()
print(cars)

#确定列表的长度,计数时从1开始
print(len(cars))


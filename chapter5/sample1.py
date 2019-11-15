# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 18:58:57 2019

@author: Administrator
"""
#检查多个条件使用and 和or
print("and")
age_0 =22
age_1 = 18
print(age_0 >=21 and age_1>=21) #and 左右两端都为True时整体为True否则为False

age_1= 21
print(age_0 >=21 and age_1>=21)
print('\n')

print('or')
age_0 =22
age_1 = 18
print(age_0>=21 or age_1>=21)#or 左右两端都为False时整体为False否则为True
age_0=18
print(age_0>=21 or age_1>=21)
print('\n')

#检查特定值是否在列表中
requested_toppings = ['mushrooms','onions','pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)



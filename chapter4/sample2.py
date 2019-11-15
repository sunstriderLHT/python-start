# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 18:12:47 2019

@author: Administrator
"""

#4-3
print("4-3")
for i in range(1,21):
    print(i,end = ' ')
print("\n") 
#4-4~4-5
print("4-4~4-5")

number1_1000 = list(range(0,1001))
print(min(number1_1000),end = ' ')
print(max(number1_1000),end = ' ')
print(sum(number1_1000),end = ' ')
print("\n") 
#4-6 range()第三个参数间隔几个数字
print("4-6")
numbers = list(range(1,20,2))
print(numbers)
print("\n") 
#4-7 
print("4-7")
numbers3 =[x for x in range(3,31) if x%3 ==0]
print(numbers3)
print("\n") 
#4-8~4-9
print('4-8~4-9')
numbers_3 = [x**3 for x in range(1,11)]
print(numbers_3)
print("\n") 


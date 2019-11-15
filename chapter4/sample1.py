# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 17:48:17 2019

@author: Administrator
"""

#遍历整个列表
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician.title()+ ", that was a great trick!")
    print("I can't wait to see your next trick,"+magician.title()+".\n")
    
print("Thank you, everyone. That was a great magic show!")

#使用函数range() 从第一个指定值开始数，到第二个数字之前停止
for value in range(1,5):
    print(value)
    
#用range()创建数字列表
numbers = list(range(1,11))
print(numbers)

#列表生成器
squres = [x**2 for x in range(1,11) ]
print(squres)

#对数字列表执行简单的统计计算
print(min(numbers))
print(max(numbers))
print(sum(numbers))

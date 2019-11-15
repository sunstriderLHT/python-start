# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 19:11:03 2019

@author: Administrator
"""

#如果只想执行一个代码块那么用if-elif-else结构 因为只要有一个测试通过就会跳过剩下的测试，
#如果要运行多个代码块，就使用一系列独立的if语句

#5-3~5-5
print('5-3')
alien_color = 'Green'
if alien_color == 'Green':
    print('You have got 5 points')
elif alien_color == 'Yellow':
    print('You have got 10 points')
else:
    print('You have got 15 points')

print('\n')

#使用if处理列表
#确定列表不是空的
requested_toppings= []
if requested_toppings:#在列表至少包含一个元素时返回True否则返回False
    for requested_topping in requested_toppings:
        print("Adding "+requested_topping+'.')
    print('\nFinished making your pizza!')
else:
    print("Are you sure you want a plain pizza?")
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 18:25:09 2019

@author: Administrator
"""

#切片
players = ['charles','martina','michael','florence','eli']
print(players[0:3])#从第一个数字开始取，停止在第二个数字之前
print(players[:4])#没有第一个数字，默认从第一个开始
print(players[2:])#没有第二个数字，默认取到最后
print(players[-3:])#取最后三个人
print("\n")
#复制列表,如果不通过切片无法得到两个列表
my_food = ['pizza','falafel','carrot cake']
friend_food = my_food
my_food.append('cannoli')
friend_food.append('ice cream')
print(friend_food)
print(my_food)
print('\n')
my_food = ['pizza','falafel','carrot cake']
friend_food = my_food[:]
my_food.append('cannoli')
friend_food.append('ice cream')
print("My favorite foods are:",end=' ')
print(my_food)
print("My friend's favorite foods are:", end= ' ')
print(friend_food)


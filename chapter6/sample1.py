# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 19:44:46 2019

@author: Administrator
"""
#字典——一系列 键——值对，与键相关联的值可以是数字、字符串、列表乃至字典
alien_0 = {'color':'green','points':5}

print(alien_0['color'])
print(alien_0['points'])

#字典是一种动态结构，可随时添加键值对
#python 不关心字典内键值对的顺序，其排列顺序和添加顺序不同

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#修改字典中的值
alien_0['color'] = 'yellow'
print('after change',end = ' ')
print(alien_0)

#删除键值对
del alien_0['points']
print('after delete',end = ' ')
print(alien_0)

#遍历字典中的所有键
print('all attributes:',end = ' ')
for name in alien_0.keys():
    print(name.title(),end = ' ')
#按顺序遍历字典的所有键
print('\nall attributes sorted:',end = ' ')    
for name in sorted(alien_0.keys()):
    print(name.title(),end = ' ')

#遍历字典所有的值
print('\nall values:',end = ' ')
for value in alien_0.values():
    print(value,end = ' ')

#遍历字典中的非重复值,使用set()集合，集合类似于指点但是每个元素必须是独一无二的
print('\nall values unique:',end = ' ')    
for value in set(alien_0.values()):
    print(value,end = ' ')
    
    
    
    
    
    
    
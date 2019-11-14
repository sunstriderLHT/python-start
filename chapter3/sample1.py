# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 21:41:32 2019

@author: Administrator
"""

bicycles =['trek','cannondale','redline','specialized']
#调取列表的第一个元素
print(bicycles[0].title())
#调取列表的最后一个元素
print(bicycles[-1].title())

print(bicycles)
#修改，添加和删除列表元素
bicycles[0] = 'ducati'
print(bicycles)
#在列表的末尾添加元素
bicycles.append('honda')
print(bicycles)

#在列表中插入元素
bicycles.insert(0,'suzuki')
print(bicycles)

#在列表中删除元素
del bicycles[0] #删除指定位置的元素
print(bicycles)

poped_bicycle = bicycles.pop()  #弹出最后的元素并将元素存放在一个变量中
print(bicycles)
print(poped_bicycle)

bicycles.pop(1) #弹出第二个元素
print(bicycles)

bicycles.remove('ducati')   #根据值删除元素
# remove()只删除第一个指定的值，如果要删除的值在列表中多次出现，这需要循环来实现


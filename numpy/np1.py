# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 11:05:22 2020

@author: Harry
"""

import numpy as np 
'''
array = np.array([[1,2,3],
                  [2,3,4]])

print(array)
print('number of dim: ',array.ndim) #数组维数
print('shape: ',array.shape)  #数组形状 行，列
print('size: ',array.size)  #数组大小
print()

#创建array
a = np.array([[2,3,4],
              [3,4,5]],dtype=np.int)
print(a)
print()

a = np.zeros((3,4))
print(a)
print()

a = np.empty((3,4))
print(a)
print()

a = np.arange(10,20,2)
print(a)
print()

a = np.arange(12).reshape((3,4))
print(a)
print()

a = np.linspace(1,10,6).reshape((2,3))
print(a)
print('*'*40)
#np 的基础运算
a = np.array([10,20,30,40])
b = np.arange(4)

print(a,b)

c = 10*np.tan(a)
print(c)
print(b<3)#判断b中元素的数量关系
print('*'*40)
'''
a = np.array([[1,1],
             [0,1]])
b = np.arange(4).reshape((2,2))
print(a)
print(b)
c = a*b
c_dot = np.dot(a,b)
c_dot_2 = a.dot(b)
print(c)
print(c_dot)
print(c_dot_2)

print('*'*40)
a = np.random.random((2,4))
print(a)
print(np.sum(a,axis=1))#求每一行的和
print(np.min(a,axis=0))#求每一列的最小值
print(np.max(a,axis=1))#求每一行的最大值























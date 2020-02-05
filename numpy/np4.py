# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 12:28:50 2020

@author: Harry
"""
import numpy as np

#np合并

A = np.array([1,1,1])
B = np.array([2,2,2])
C = np.vstack((A,B))#vertical stack
print(A.shape,C.shape)
D = np.hstack((A,B))#horizontal stack
print(D,D.shape)


print('*'*40)
print(A[:,np.newaxis])#改变A的维度

A = np.array([1,1,1])[:,np.newaxis]
B = np.array([2,2,2])[:,np.newaxis]
E = np.hstack((A,B))
print(E,E.shape)

F = np.concatenate((A,B,B,A),axis = 1)
print(F)
print('*'*40)


#分割array
A = np.arange(12).reshape((3,4))
print(A)
print(np.split(A,2,axis=1))#分割成两部分 每行都被平分
print(np.split(A,3,axis=0))#对列进行分割，分为三部分
print(np.array_split(A,3,axis=1))

print('*'*40)
#np 的 copy
a = np.arange(4)
b=a #此处a,b,c,d全部都是完全一样的东西
c=a
d=b
a[0] = 11#a,b,c,d同步改变
print(a,b)
b = a.copy() #deep copy 把a的值赋给b但是不关联这两个量
a[1:3] = 22,33
print(a,b)
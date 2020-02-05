# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 12:19:18 2020

@author: Harry
"""
import numpy as np

#np索引
A = np.arange(3,15)
print(A)
print(A[3])
A = np.arange(3,15).reshape((3,4))
print(A)
print()
print(A[2])
print(A[2,:])

print(A[1][1])
print(A[1,1])
print(A[1,1:3])
print('*'*40)



for row in A:#默认迭代每一行
    print(row)
    
print()
for column in A.T:
    print(column)

print()
print(A.flatten())#将A变为一个列表
for item in A.flat:
    print(item)
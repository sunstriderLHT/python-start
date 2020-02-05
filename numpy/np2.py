# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 11:55:54 2020

@author: Harry
"""
import numpy as np
#np 基础运算2
A = np.arange(14,2,-1).reshape((3,4))
print(A)
print(np.argmin(A))#最大元素索引
print(np.argmax(A))#最小元素索引

print(np.mean(A))#输出平均值
print(A.mean())
print(np.average(A))

print(np.median(A))#输出中位数

print(np.cumsum(A).reshape((3,4)))#累加并记录每次结果
print(np.diff(A))#记录每两个数之间的差
print(np.nonzero(A))#输出所有不为零的元素的行列下标

print(np.sort(A))#对每一行进行排序

print(np.transpose(A))#矩阵转向
print(A.T)#矩阵转向
print((A.T).dot(A))

print(np.clip(A,5,9))#让矩阵中所有大于9的数变为9，小于5的变为5

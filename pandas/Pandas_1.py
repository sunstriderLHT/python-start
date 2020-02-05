# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 17:44:50 2020

@author: Harry
"""

import pandas as pd 
import numpy as np

s = pd.Series([1,3,6,np.nan,44,1])

dates = pd.date_range('20200130',periods=6)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns = ['a','b','c','d']) #np.random.randn()  随机生成呈现正态分布的数据 括号内是各维度的数据量 例子中是二维元素数量6*4
df1 = pd.DataFrame(np.arange(12).reshape((3,4)))
df2 = pd.DataFrame({'A' : 1.,
                    'B' : pd.Timestamp('20130102'),
                    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D' : np.array([3] * 4,dtype='int32'),
                    'E' : pd.Categorical(["test","train","test","train"]),
                    'F' : 'foo'}) 

print(df2.dtypes)#输出行类型
print()
print(df2.index) #输出行标签
print()
print(df2.columns)#输出列标签
print()
print(df2.values)#输出所有df2的值
print()
print(df2.describe())#输出数据的总结
print()
print(df2.T)#翻转数据
print()
print(df2.sort_index(axis=1,ascending=False))#对数据的index进行排序并输出
print()
print(df2.sort_values(by='E'))#对数据值进行排序
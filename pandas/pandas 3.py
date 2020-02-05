# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 10:21:14 2020

@author: Harry
"""

import pandas as pd 
import numpy as np

df1 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
df2 = pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index=[2,3,4])
# join = {'inner','outer'}
res  =pd.concat([df1,df2], axis=0, ignore_index = True)#默认join为outer,原始dataframe中没有的东西用nan填充
print(res)
res1 = pd.concat([df1,df2],join = 'inner',ignore_index=True)# join为inner 合并相同部分 忽略序号
print(res1)
res2 = pd.concat([df1,df2],axis=1,join_axes=[df1.index])#左右合并 按照df1的 index
print(res2)
 
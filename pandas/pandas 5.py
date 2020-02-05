# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 15:54:11 2020

@author: Harry
"""
import pandas as pd
#merging two df by keys

left = pd.DataFrame({'key':['K0','K1','K2','K3'],
                     'A':['A0','A1','A2','A3'],
                     'B':['B0','B1','B2','B3']})
right = pd.DataFrame({'key':['K0','K1','K2','K3'],
                     'C':['C0','C1','C2','C3'],
                     'D':['D0','D1','D2','D3']})

res = pd.merge(left,right,on='key')
print(res)

print('*'*40)
left2 = pd.DataFrame({'key1':['K0','K0','K1','K2'],
                      'key2':['K0','K1','K0','K1'],
                     'A':['A0','A1','A2','A3'],
                     'B':['B0','B1','B2','B3']})
right2 = pd.DataFrame({'key1':['K0','K1','K1','K2'],
                      'key2':['K0','K0','K0','K0'],
                     'C':['C0','C1','C2','C3'],
                     'D':['D0','D1','D2','D3']})
#how = ['left','right','inner','outer']
res2 = pd.merge(left2,right2,on =['key1','key2'])#默认为inner key1 key2 相同时合并
print(res2) 
res3 =pd.merge(left2,right2,on=['key1','key2'], how = 'outer')# 合并dataframe没有的数据用nan填充
print(res3)
res4 =pd.merge(left2,right2,on=['key1','key2'], how = 'right')# 基于right的key来合并 ,left 如果没有这个key就用nan填充
print(res4) 

print('*'*40)
df1 =pd.DataFrame({'col1':[0,1],'col_left':['a','b']})
df2 =pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})
print(df1)
print(df2)
res = pd.merge(df1,df2,on='col1',how='outer',indicator='indicator_column') #显示如何进行merge 默认为indicator=False
#give the indicator a custom name 
print(res)

print('*'*40)
left3 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                     index=['K0', 'K1', 'K2'])
right3 = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']},
                     index=['K0', 'K2', 'K3'])
print(left3)
print(right3)
res5 = pd.merge(left3, right3 , left_index = True, right_index = True,how='outer')# 考虑两个dataframe的index合并
res6 = pd.merge(left3, right3 , left_index = True, right_index = True,how='inner')# 考虑两个dataframe的index合并

print(res5)
print(res6)
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 16:43:32 2020

@author: Harry
"""
import pandas as pd



boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})
print(boys)
print(girls)
res = pd.merge(boys,girls, on='k',suffixes=['_boys','_girls'],how = 'inner')
print(res)

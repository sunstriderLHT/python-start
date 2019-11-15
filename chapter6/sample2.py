# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 20:11:00 2019

@author: Administrator
"""

favorite_languages = {
        'jen':'python',
        'sarah':'c',
        'edward':'ruby',
        'phil':'python',
        }

namelist =['jen','sarah','edward','john','max','mida','sam']

for name in namelist:
    if name in favorite_languages.keys():
        print("Thank you "+name+' for join us')
    else:
        print("We want to invite you to join us, "+name)
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 21:15:42 2019

@author: Administrator
"""
message = "ada lovelace"
#每个单词大写首字母
print(message.title())
#将字符串全部大写
print(message.upper())
#将字符串全部小写
print(message.lower())


#合并字符串
first_name = "ada"
last_name= "lovelace"
full_name=first_name+" "+last_name
print(full_name.title())

#制表符或换行符添加空白
print("\tpython")

print("languages: \n\tPython\n\tC\n\tJavascript")

#删除空白
favorite_language = 'Python   '
print(favorite_language)
print(favorite_language.rstrip())
#其实此刻favorite_language仍然是有空白的，要想消除必须将结果存入favorite_language
#类似的 lstrip()消除左侧的空白  strip()同时消除两侧空白


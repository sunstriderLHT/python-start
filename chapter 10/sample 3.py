# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 15:21:58 2020

@author: Harry
"""
# 1 加法运算
def add():
    Flag = True
    while Flag:    
        num1 = input("Please input a number: ") 
        num2 = input("Please input another number: ")
        try:
            result = eval(num1)+eval(num2)
        except NameError:
            msg = "you should input a number"
            print(msg)
            continue
        else:
            print(result)
            Flag = False
print()

# 2 猫和狗
filename1 = 'cats.txt'
filename2 = 'dogs.txt'
try:
    with open(filename1) as file_obj:
        contents1 = file_obj.read()
        print(contents1)
except FileNotFoundError:
    msg = "sorry we cannot find the file"
    print(msg)
try:
    with open(filename2) as file_obj:
        contents2 = file_obj.read()
        print(contents2)
except FileNotFoundError:
    msg = "sorry we cannot find the file"
    print(msg)
    
# 3 单词出现数量
with open('alice.txt') as file_obj:
    contents=file_obj.read()
    times=contents.lower().count('alice')
    print(times)
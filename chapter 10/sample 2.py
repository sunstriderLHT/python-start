# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 12:36:52 2020

@author: Harry
"""

# 1 异常--使用try-except代码块处理ZeroDivisionError异常
try:
    print(5/0)
except ZeroDivisionError:
    print("you can't divide by zero")
print()

# 2 使用异常避免崩溃 使用try-except-else代码块
print("Give me two numbers, and I'll divide them.")  
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number =='q':
        break
    second_number = input("\nSecond number: ")
    if second_number =='q':
        break
    try: 
        answer = int(first_number) /int(second_number)
    except ZeroDivisionError:
        print("you can't divide by 0!")
    else:
        print(answer)
#Python尝试执行try 代码块中的代码；只有可能引发异常的代码才需要放在try 语句中。
#有时候，有一些仅在try 代码块成功 执行时才需要运行的代码；这些代码应放在else 代码块中。
#except 代码块告诉Python，如果它尝试运行try 代码块中的代码时引发了指定的异常，该怎么办
        
print()
# 3 处理FileNotFoundError异常
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents=f_obj.read()
except FileNotFoundError:
    msg = 'Sorry, the file '+ filename+' does not exit'
    print(msg)    
    
print()
# 4 分析文本
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = 'Sorry, the file '+ filename + ' does not exist.'
    print(msg)
else:
    words = contents.split()
    #使用split()构建一个列表
    
    num_words = len(words)
    #确定列表的长度
    
    print("the file "+ filename + " has about " + str(num_words) + " words. ")
    
# 5 将上述代码装换为函数方便随时调用
def count_words(filename):
    try: 
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
            msg = 'Sorry, the file ' + filename + ' does not exist. '
            print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file "+ filename + " has about "+str(num_words)+ " words.")
filename = 'alice.txt'
count_words(filename)
filename = 'siddhartha.txt' 
count_words(filename)

print()


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 16:02:52 2020

@author: Harry
"""
# 1 remeber me 
import json 
#如果以前储存了用户名，就加载它
#否则就提示用户输入用户名并储存它
filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
        print("We will remeber you when you come back, " +username + " !")
else:
    print("Welcome back, "+ username+ '!')

print()
# 2 重构
import json

def get_stored_username():
    #如果储存了用户名，就获取它
    filename = 'username1.json'
    try: 
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
    
    
def get_new_username():
    #提示用户输入用户名
    username = input("What is your name? ")
    filename = 'username1.json'
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
    return username


def greet_user():
    #问候用户，并指出其名字
    username = get_stored_username()
    if username:
        user_state = input("Are you "+ username+ "?(Y/N)")
        if user_state =='Y':
            print("welcome back "+username+ "!")
        else:
            username = get_new_username()
            print("We will remeber you when you come back, "+ username+ '!')
    else:
        username = get_new_username()
        print("We will remeber you when you come back, "+ username+ '!')
greet_user()
            
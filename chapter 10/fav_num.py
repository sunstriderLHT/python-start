# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 16:37:45 2020

@author: Harry
"""
import json
def get_fav_num():
    filename = 'favNum.json'
    try:
        with open(filename) as f_obj:
            fav_number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return fav_number

def add_fav_num():
    filename='favNum.json'
    fav_number = input("Please input your favorite number: ")
    with open(filename,'w') as f_obj:
        json.dump(fav_number,f_obj)
    return fav_number

def u_fav_num():
    fav_number = get_fav_num()
    if fav_number:
        print("I know your favorite number! It's "+ fav_number)      
    else:
        fav_number = add_fav_num()
        print("Now we know your favorite number and you can ask me next time!")
        
u_fav_num()
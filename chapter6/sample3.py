# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 20:16:01 2019

@author: Administrator
"""

#嵌套——将一系列字典储存在列表中，或将列表作为值储存在字典中

#字典列表,在列表中每个字典都存放了特定对象的众多信息
print("在列表中存放字典")
alien_0 = {'color':'green', 'points':5}
alien_1 = {'color':'yellow', 'points':10}
alien_2 = {'color':'red', 'points':15}
aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)
    
print('\n')
aliens = [] #创建一个用于储存外星人信息的列表
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print("The total number of aliens is:%d"%len(aliens))
print('\n')

#在字典中存储列表，在字典中的列表可以存放特定特征的不同可能性
print("在字典中存储列表")
#这个字典存储了pizza的两个信息，其中toppings信息是一个列表
pizza= {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
        }
print('You ordered a '+pizza['crust']+'-crust pizza '+'with the following toppings:')
for topping in pizza['toppings']:
    print(topping)

    
#在字典中也可以嵌套字典
user = {
    'aeinstein':{
        'first' : 'albert',
        'last' : 'einstein',
        'location':'priceton',
        },
    'mcurie':{
        'first':'marie',
        'last' :'curie',
        'location':'paris',
        },        
        }
for username, user_info in user.items():
    print("\nUsername: "+ username)
    full_name = user_info['first'] +' '+user_info['last']
    location = user_info['location']
    print('\tFull name: ' +full_name.title())
    print('\tlocation: '+ location.title())
    


















    
    
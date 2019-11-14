# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 17:11:55 2019

@author: Administrator
"""

# 3-4 ~ 3-7
guest_list = ['Einstein','Newton','Tesla','Shannon']

guest_cannot_come = guest_list.pop(2)

new_guest = 'Edison'
guest_list.append(new_guest)

guest_list.insert(0,'Max')
guest_list.insert(2,'Cavendish')
guest_list.append('Darwin')

for i in range(len(guest_list)):
    print('Dear Mr.'+ guest_list[i]+',\n we invite you to have dinner tonight'+'\n')

print('Mr.'+guest_cannot_come+' cannot come tonoght')
print('Mr.'+new_guest+ ' will come tonight')
print(guest_list)
i = len(guest_list)
print(i)
while i>2:
    guest_popped = guest_list.pop()
    i = i-1
    print('Mr.'+ guest_popped+',we are sorry that we cannot invite you since we donnot have enough seats.')

for i in range(len(guest_list)):
    print('Dear Mr.'+ guest_list[i]+',\n we still want to invite you to have dinner tonight'+'\n')    

del guest_list[0:]
print(guest_list)
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 19:10:50 2020

@author: Harry
"""

# 1 Polite in Japan
user_name = input("Enter your name: ")
print("Hello "+ user_name+"-san! ")

# 2 Adding 
odd_sum = 0
for num in range(1,1000000,2):
    odd_sum = odd_sum + num
print(odd_sum)

# 3 xxxCoolxxxNamexxx
user_input =  input("Please enter words: ")
user_list=user_input.split(",")

print("xxx"+user_list[0]+"xxx"+user_list[1]+"xxx"+user_list[2])

# 4
u_value = input("How much liquid do you have? ")
try:
    cups = eval(u_value)//50
    
except ValueError:
    print("Please input a number! ")
else:
    print("The liquid you have could transfer into "+ str(cups) +"cups.")

# 5
pri_invest,int_rate,num_years= eval(input("Enter the pricipal investment,annual interest rate,number of year : "))
f_amount = pri_invest*(1+int_rate/4)**(4*num_years)
print(round(f_amount))

for time in range(num_years):
    f_amount = pri_invest*(1+int_rate/4)**4
    pri_invest = f_amount
print(round(f_amount))

# 6 
fruits = ["strawberry", "cherry", "banana"]
iceCreams = fruits[:]
print("List of fruits:", fruits)
iceCreams[2] = "chocolate"
print("List of fruits:", fruits)
print("List of ice creams:", iceCreams)

# 7
user_num = eval(input("Please enter a number: "))
num_sum = 0 
for num in range(1,user_num+1):
    num_sum = num_sum+ 1/(2**num)
print(round(num_sum,2))
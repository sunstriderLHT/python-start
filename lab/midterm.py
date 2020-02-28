# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 08:55:35 2020

@author: 16132
"""
import graphics
import random
import math

# Q1---------------------------------
def league2km():
    
    try:
        leagues = eval(input("please enter the leagues you want to transfer: "))
        km = leagues*5.556
        return km
    except NameError:
        print("Invalid leagues, please enter a number")

# Q2-a-------------------------------
def hello(name):
    hello_message = "Hello "+name
    return hello_message
    

# Q2-b-------------------------------
def hello2all():
    print(hello("Ottawa"))
    print(hello("World"))
    print(hello("Neptune"))
    print(hello("Galaxy"))
    print(hello("Universe"))
    
# Q2-c-------------------------------
def count_list():
    file_name = "countries.txt"
    with open(file_name,'r')as file:
        content = file.readlines()
        count = len(content)
        return count

# Q2-d-------------------------------
def hello2coutries():
    file_name = "countries.txt"
    outfile_name = "helloword.txt"  
    with open(file_name,'r') as file:
        content = file.readlines()
    with open(outfile_name,'w') as ofile:
        for country in content:
            ofile.write(hello(country))
            
# Q3---------------------------------
def taylor():
    sum_taylor = 1
    bottom = 1
    x = eval(input("Please enter your x: "))
    n = eval(input("Please enter your n: "))
    for i in range(1,n+1):
        y = x**i/bottom
        bottom = bottom * (i+1)
        sum_taylor += y
    return sum_taylor

# Q4--------------------------------------------------------------------------------------------- 
def blood_pressure():
    try:
        s_blood_pressure = eval(input("Please input patient's Systolic Blood pressure: "))
        d_blood_pressure = eval(input("Please input patient's Diastolic Blood pressure： "))
        print("")
    except:
        print("Invalid input, please enter numbers!")
    else:    
        if s_blood_pressure < 120 and d_blood_pressure < 80:
            print("The category of this patient is normal")
            
        elif s_blood_pressure >180 or d_blood_pressure >120:
            print("The category of this patient is Hypertension crisis")
            
        elif 140 <=s_blood_pressure or 90 <= d_blood_pressure:
            print("The category of this patient is Hypertension Stage 2 ")
            
        elif 130 <=s_blood_pressure < 139 or 80 <= d_blood_pressure <= 89:
            print("The category of this patient is Hypertension Stage 1")
            
        elif 120 <= s_blood_pressure <= 129 or d_blood_pressure < 80:
            print("The category of this patient is elevated")
    
# Q5---------------------------------------------------------------------------------------------    
def get_name_color():
    name = input("Please enter your name: ")    
    color = input("Please enter your favorite color: ")
    return name,color

def draw_circle_name():
    name,color = get_name_color()
    
    win = graphics.GraphWin("circle",500, 500)
    
    circle = graphics.Circle(graphics.Point(250,250),50)
    try:
        circle.setFill(color)
        circle.draw(win)
    except:
        print("Invalid color, please use the color in the graphics library!")
    else:
        name_label = graphics.Text(graphics.Point(250,250),name)

        name_label.draw(win)
        
# Q6--------------------------------------------------------------------------------------------
def escape():
    win = graphics.GraphWin("circle",500, 500)
    win.setBackground("blue")
    
    center = graphics.Point(250,250)
    
    circle = graphics.Circle(center,100) 
    circle.setFill("white")
    
    bacterium = graphics.Circle(center,10)

    circle.draw(win)        
    bacterium.draw(win)
    
    for i in range(1800):
        
        angle = random.random()*2*math.pi
        
        bacterium.move(3*math.cos(angle),3*math.sin(angle))
    b_center = bacterium.getCenter()
    
    
    win.close()
    return center,b_center

def probability():
    count = 0
    for i in range(10):
        center, b_center = escape() 
        
        distance = math.sqrt((b_center.getX()-center.getX())**2 + (b_center.getY()-center.getY())**2)
        print(distance)
        
        
        if distance > 100:
            print("Bacterium escaped\n")
            count += 1
        else:
            print("Bacterium died\n")
    print(count/10)
    
    
    
    
    
    
    
    
    
    
    
    
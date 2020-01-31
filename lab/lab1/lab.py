# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 11:05:22 2020

@author: Harry
"""

import graphics
import math 

# Q1
win = graphics.GraphWin("Line Draw",500, 500)
    
p1 = win.getMouse()
p2 = win.getMouse()
line = graphics.Line(p1,p2)
line.draw(win)
    
slope = (p2.getY()-p1.getY())/(p2.getX()-p1.getX())
slope_label = graphics.Text(p1,abs(round(slope,2)))
slope_label.draw(win)

# Q2
'''
win = graphics.GraphWin("Flag Draw",500, 500)
win.setCoords(-6,-6,6,6)
rect1 = graphics.Rectangle(graphics.Point(-6,0), graphics.Point(6,6))
color_MS = graphics.color_rgb(0, 119, 139)
rect1.setOutline(color_MS)
rect1.setFill(color_MS)
rect1.draw(win)
rect2 = graphics.Rectangle(graphics.Point(-6,2),graphics.Point(6,4))
color_S = graphics.color_rgb(255, 199, 44)
rect2.setFill(color_S)
rect2.setOutline(color_S)
rect2.draw(win)
triangle = graphics.Polygon(graphics.Point(-6,0),graphics.Point(-6,6),graphics.Point(-0.8,3))
triangle.setFill("black")
triangle.draw(win)    
    
# Q3
win = graphics.GraphWin("Flag Draw",500, 500)
win.setCoords(0,0,50,50)
color_BG = graphics.color_rgb(101,167,404%255)
win.setBackground(color_BG)
h_grass = win.getMouse()
rect_grass = graphics.Rectangle(graphics.Point(0,0),graphics.Point(50,h_grass.getY()))
rect_grass.setFill("green")
rect_grass.draw(win)
h_water = win.getMouse()
rect_water = graphics.Rectangle(graphics.Point(0,h_grass.getY()),graphics.Point(50,h_water.getY()))
rect_water.setFill("blue")
rect_water.draw(win)
c_sun = win.getMouse()   
r_sun = win.getMouse()
d = math.sqrt((c_sun.getY()-r_sun.getY())**2+(c_sun.getX()-r_sun.getX())**2)
cir_sun = graphics.Circle(graphics.Point(c_sun.getX(),c_sun.getY()),d)
cir_sun.setFill("yellow")
cir_sun.draw(win)
'''
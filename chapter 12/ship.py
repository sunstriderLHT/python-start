# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 17:26:00 2020

@author: Harry
"""

import pygame 

class Ship():
    
    def __init__(self,screen):
        #初始化飞船并设置其初始化位置
        self.screen = screen
        
        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('ship.bmp')  #该函数返回一个表示飞船的surface储存到self.image中
        self.rect = self.image.get_rect()  #get_rect()获取相应surface的属性 rect 外接矩形
        self.screen_rect = screen.get_rect()
        
        #将每艘新飞船放在屏幕 底部中央
        self.rect.centerx = self.screen_rect.centerx #将飞船中心的x坐标设置为表示屏幕的矩形的中心x坐标也就是对齐
        
        self.rect.bottom = self.screen_rect.bottom  #将飞船下边缘的y坐标设置为表示屏幕的矩形的下边缘的y坐标
    
    def blitme(self):
        
        self.screen.blit(self.image,self.rect) #根据self.rect指定的位置将图像绘制到屏幕上
        

#在pygame中原点位于左上角
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 17:26:00 2020

@author: Harry
"""

import pygame 

class Ship():
    
    def __init__(self,ai_settings,screen):
        #初始化飞船并设置其初始化位置
        self.screen = screen
        self.ai_settings = ai_settings
        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('image/ship.bmp')  #该函数返回一个表示飞船的surface储存到self.image中
        self.rect = self.image.get_rect()  #get_rect()获取相应surface的属性 rect 外接矩形
        self.screen_rect = screen.get_rect()
        
        #将每艘新飞船放在屏幕 底部中央
        self.rect.centerx = self.screen_rect.centerx #将飞船中心的x坐标设置为表示屏幕的矩形的中心x坐标也就是对齐
        
        self.rect.bottom = self.screen_rect.bottom  #将飞船下边缘的y坐标设置为表示屏幕的矩形的下边缘的y坐标
        
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
        
        
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed_factor  
        if self.moving_up and self.rect.top >0:
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
    def blitme(self):
        
        self.screen.blit(self.image,self.rect) #根据self.rect指定的位置将图像绘制到屏幕上
        
    def center_ship(self):
        
        self.center = self.screen_rect.centerx
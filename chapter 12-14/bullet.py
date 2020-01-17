# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 14:41:49 2020

@author: Harry
"""

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    
    def __init__(self, ai_settings, screen, ship):
        
        super().__init__()
        self.screen = screen
        
        self.rect = pygame.Rect( 0, 0, ai_settings.bullet_width,ai_settings.bullet_height)
        
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        self.y = float(self.rect.y)
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        
        
    def update(self):
        #向上移动子弹
        
        #更新表示子弹的小数值
        self.y -=self.speed_factor
        #更新表示子弹的rect位置
        self.rect.y = self.y
        
    def draw_bullet(self):
        '''在屏幕上绘制rect'''
        pygame.draw.rect(self.screen,self.color,self.rect)
        
        
        
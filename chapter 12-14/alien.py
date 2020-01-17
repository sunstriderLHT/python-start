# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 16:38:47 2020

@author: Harry
"""
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    
    def __init__(self, ai_settings, screen):
        '''初始化外星人并设置其起始位置'''
        super().__init__()
        self.screen = screen 
        self.ai_settings = ai_settings
        #加载外星人图像，并获取其rect属性
        self.image = pygame.image.load('image/alien.bmp')
        self.rect = self.image.get_rect()
        #每个外星人最初都在屏幕左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x)
        
    def blitme(self):
        
        self.screen.blit(self.image, self.rect)
    
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <=0:
            return True
        
    def update(self):
        
        self.x += (self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction)
        self.rect.x = self.x
        
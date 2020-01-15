# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 16:14:03 2020

@author: Harry
"""
import sys

import pygame

from settings import Settings
from ship import Ship

def run_game():
    
    pygame.init()
    #初始化背景设置并创建一个指定大小的显示窗口
    
    ai_settings = Settings()
    
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    
    pygame.display.set_caption("Alien Invation")
   
    ship = Ship(screen)
    
    while True:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill(ai_settings.bg_color)
        #以背景色填充屏幕
        ship.blitme()
        pygame.display.flip()
        #不断更新屏幕以显示元素的新位置，让最近绘制的屏幕可见
run_game()

#每个元素都是一个surface像外星人和飞船
#display.set_mode()返回的surface 表示整个游戏窗口
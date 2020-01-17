# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 14:22:41 2020

@author: Harry
"""
import pygame
import sys
def run_game():
    
    pygame.init()
    #初始化背景设置并创建一个指定大小的显示窗口

    
    screen = pygame.display.set_mode((800,600))
    
    pygame.display.set_caption("Press")
    
    bg_color = (230,230,230)
    
    screen.fill(bg_color)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type ==pygame.KEYDOWN:
                print(event.key)
        
        
run_game()


            

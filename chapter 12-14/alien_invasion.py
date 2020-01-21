# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 16:14:03 2020

@author: Harry
"""

import pygame

from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    #初始化背景设置并创建一个指定大小的显示窗口
    pygame.init()
    #创建一个Setting实例
    ai_settings = Settings()
    #创建一个指定大小的窗口
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    #窗口的名称    
    pygame.display.set_caption("Alien Invation")
    
    play_button = Button(ai_settings,screen,"Play")
    #创建储存游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen, stats)
    
    #创建一个Ship实例
    ship = Ship(ai_settings,screen)
    #创建一个bullets群组
    bullets = Group()
    #创建一个aliens群组
    aliens = Group()
    #创建外星人
    gf.create_fleet(ai_settings,screen,ship,aliens)
    
    
    
    
    while True:
        gf.check_events(ai_settings, screen, stats,sb, play_button, ship,aliens, bullets)
        
        if stats.game_active:
            ship.update()    
            gf.check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
        filename = 'high_score'
        with open(filename,'w') as file_object:
            file_object.write(str(stats.high_score))
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button) 
        
        
run_game() 

#每个元素都是一个surface像外星人和飞船
#display.set_mode()返回的surface 表示整个游戏窗口
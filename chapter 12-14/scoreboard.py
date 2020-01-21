# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 15:42:06 2020

@author: Harry
"""

import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    
    def __init__(self,ai_settings,screen,stats):
        
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        self.read_high_score()
        #显示得分信息时使用的字体设置
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)
        #准备初始得分图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
        
    def read_high_score(self):
        filename = 'high_score'
        with open(filename,'r') as f_obj:
            self.stats.high_score = f_obj.read()

    def prep_high_score(self):
        
        high_score = int(self.stats.high_score)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str,True,self.text_color,self.ai_settings.bg_color)
        
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
        
        
    def prep_score(self):
        #将得分转换为渲染的图像
        rounded_score = int(round(self.stats.score,-1))
        #"{:,}"千位分隔符
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render("score: "+score_str,True,self.text_color,self.ai_settings.bg_color)
        
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right -20
        self.score_rect.top = 20
        
    def prep_level(self):
        
        self.level_image = self.font.render("level: "+str(self.stats.level),True,self.text_color,self.ai_settings.bg_color)
        
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
        
    def prep_ships(self):
        #创建一个空编组，用于存储飞船实例
        self.ships = Group()
        #根据玩家还有多少艘飞船运行一个循环相应的次数，在这个循环中，创建新飞船并设这起坐标使整个飞船飞船编组位于屏幕左边
        for ship_number in range(self.stats.ship_left):
            ship = Ship(self.ai_settings,self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y =10
            self.ships.add(ship)
            
        
    def show_score(self):
        
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.screen.blit(self.level_image,self.level_rect)
        
        self.ships.draw(self.screen)
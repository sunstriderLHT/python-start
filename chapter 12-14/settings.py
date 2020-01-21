# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 17:17:38 2020

@author: Harry
"""

class Settings():
    
    def __init__(self):
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        #飞船设置
        
        self.ship_limit = 3
        #子弹设置
        
        self.bullet_width = 200
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3
        #外星人设置
        
        self.fleet_drop_speed = 10
        
        #游戏节奏的加速度
        self.speedup_scale = 1.1
        #外星人点数的提高速度
        self.score_scale = 1.5
        #初始化随游戏进行而变化的设置
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        
        self.fleet_direction = 1 #fleet_direction 为1表示向右，为-1表示向左移
        self.alien_points = 50
        
    def increase_speed(self):
        
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
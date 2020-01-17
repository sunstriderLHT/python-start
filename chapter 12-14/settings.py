# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 17:17:38 2020

@author: Harry
"""

class Settings():
    
    def __init__(self):
        #初始化游戏设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        
        self.ship_speed_factor = 1
        self.ship_limit = 3
        
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 6
        
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1 #fleet_direction 为1表示向右，为-1表示向左移
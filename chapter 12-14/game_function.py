# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 16:14:03 2020

@author: Harry
"""
import sys

from time import sleep

import pygame

from bullet import Bullet
from alien import Alien

#响应按键       
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True 
    elif event.key ==pygame.K_SPACE:
        #创建一颗子弹，并将其加入到编组bullets中
        fire_bullet(ai_settings,screen,ship,bullets)
        


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False    
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

        
def check_events(ai_settings, screen, ship, bullets):
    #响应按键和鼠标
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type ==pygame.KEYDOWN:
            check_keydown_events(event,ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
            
def fire_bullet(ai_settings,screen,ship,bullets):
    if  len(bullets)<= ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)

def update_bullets(ai_settings,screen,ship,aliens,bullets):
    
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
def check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets):    
    collisions = pygame.sprite.groupcollide(bullets,aliens,False,True)
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings,screen,ship,aliens)
            
def get_number_aliens_x(ai_settings,alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width #统计可放置外星人的水平空间
    number_aliens_x = int(available_space_x / (2*alien_width)) #计算可放置外星人的数量
    return number_aliens_x

def get_number_aliens_y(ai_settings,ship_height,alien_height):
    available_space_y = ai_settings.screen_height - (3*alien_height)-ship_height
    number_rows = int(available_space_y / (2*alien_height))
    return number_rows

def create_alien(ai_settings,screen, aliens,alien_number,row_number):
    alien = Alien(ai_settings,screen)#创建一个alien对象
    alien_width = alien.rect.width #alien对象的宽度和rect的宽度相同
    alien.y = alien.rect.height + 2* alien.rect.height*row_number
    alien.x = alien_width +2*alien_width*alien_number #计算每一个alien对象的x坐标
    alien.rect.x = alien.x #将x坐标输入更新到rect.x
    alien.rect.y = alien.y
    aliens.add(alien)  #将创建的外星人对象加入到aliens 群组中
            
def create_fleet(ai_settings,screen,ship,aliens):
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_aliens_y = get_number_aliens_y(ai_settings,ship.rect.height,alien.rect.height)
    for row_number in range(number_aliens_y):
        for alien_number in range(number_aliens_x):   #创建一行外星人
            create_alien(ai_settings,screen, aliens,alien_number,row_number)
            
def check_fleet_edges(ai_settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break
        
def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings,stats,screen, ship, aliens,bullets):
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,screen, ship, aliens,bullets)
    
def update_screen(ai_settings,screen,ship,aliens,bullets):
        screen.fill(ai_settings.bg_color)  #以背景色填充屏幕
        
       
        #不断更新屏 让最近绘制的屏幕可见 以显示元素的新位置
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        ship.blitme()
        aliens.draw(screen)
        pygame.display.flip()
        
def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
    
    stats.ship_left -=1
    
    aliens.empty()
    bullets.empty()
    
    create_fleet(ai_settings,screen,ship,aliens)
    ship.center_ship()
    
    sleep(0.5)
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
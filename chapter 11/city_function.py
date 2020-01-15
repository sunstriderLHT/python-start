# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 18:21:20 2020

@author: Harry
"""

def city_country(city,country,population=''):
    if population:
        city_country = city+', '+country+' - population '+ population
        return city_country.title()
    else:
        city_country = city+', '+country
        return city_country.title()
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 18:23:18 2020

@author: Harry
"""

import unittest
from city_function import city_country

class Cities_testcase(unittest.TestCase):
    def test_city_country(self):
        city_and_country = city_country('santiago','chile')
        self.assertEqual(city_and_country,'Santiago, Chile')
    def test_city_country_population(self):
        city_and_country_population = city_country('santiago','chile','5000000')
        self.assertEqual(city_and_country_population,'Santiago, Chile - Population 5000000')
unittest.main()
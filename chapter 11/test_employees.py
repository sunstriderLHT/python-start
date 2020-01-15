# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 19:27:15 2020

@author: Harry
"""

import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.my_employee = Employee('Hantao','Liu',500000)
    def test_give_default_raise(self):
        self.my_employee.give_raise()
        result = self.my_employee.show_result()
        self.assertEqual(result,"After raise Hantao Liu's wage is: "+str(self.my_employee.wage))
        print(str(self.my_employee.wage))
    def test_give_custom_raise(self):
        self.my_employee.give_raise(10000)
        result = self.my_employee.show_result()
        self.assertEqual(result,"After raise Hantao Liu's wage is: "+str(self.my_employee.wage))
        print(str(self.my_employee.wage))
unittest.main()
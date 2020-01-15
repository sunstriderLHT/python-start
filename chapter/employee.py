# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 19:23:04 2020

@author: Harry
"""

class Employee():
    def __init__(self,f_name,l_name,wage):
        self.f_name = f_name
        self.l_name = l_name
        self.wage = wage
    def give_raise(self,wage_p=5000):
        self.wage = self.wage + wage_p
        return self.wage 
    def show_result(self):
        result="After raise "+self.f_name+" "+ self.l_name+"'s wage is: "+str(self.wage)
        return result
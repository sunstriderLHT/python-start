# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 19:05:42 2020

@author: Harry
"""

import unittest
from survey import AnonymousSurvey

class TestAnonmousSurvey(unittest.TestCase):
    
    def setUp(self):
        #创建一个调查对象和一组答案，供测试的方法使用
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English','Spanish','Mandarin']
   
    def test_store_single_response(self):
        #测试的单个答案将被妥善的保存
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)
        
    def test_store_three_response(self):
        #测试的三个答案会被妥善的保存
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)

unittest.main()
#方法setUp()做了两件事情：创建了一个调查对象self.my_survey，创建一个答案列表self.responses
#储存这两个东西的变量名包含前缀self也就是说它们存储在属性中，因此这个类中的任何地方都可以使用
#在之后的测试方法中就不用再次创建对象和列表了
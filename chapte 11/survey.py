# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 18:41:52 2020

@author: Harry
"""

class AnonymousSurvey():
    
    def __init__(self,question):
        #存储一个问题，并为存储答案做准备
        self.question = question
        self.responses = []
        
    def show_question(self):
        #展示问题
        print(self.question)
        
    def store_response(self,new_response):
        #储存答案
        self.responses.append(new_response)
    
    def show_results(self):
        #展示结果
        print("Survey results:")
        for response in self.responses:
            print('-'+response)
            

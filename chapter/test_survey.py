# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 18:53:48 2020

@author: Harry
"""

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    
    def test_store_singel_response(self):
        
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English',my_survey.responses)
    def test_store_three_response(self):
        
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses  = ['English','Chinese','Japanese']
        for response in responses:
            my_survey.store_response(response)
            self.assertIn(response,my_survey.responses)
unittest.main()
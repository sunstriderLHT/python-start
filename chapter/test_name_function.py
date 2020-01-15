# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    #测试name_function.py
    def test_first_last_name(self):
        #能够正确处理像Janis Joplin 这样的姓名么
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
        #断言方法用来核实得到的结果是否与期望的结果一致
        #将formatted_name 的值同字符串‘Janis Joplin’进行比较
    def test_first_last__middle_name(self):
        #能够正确处理像Wolfgang Amadeus Mozart这样的姓名么
        formatted_name = get_formatted_name('wolfgang','mozart','amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
unittest.main()
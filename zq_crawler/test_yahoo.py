'''
Unit Tests for yahoo.py
'''

import unittest
from .yahoo import *

# Unit test class
class TestYahooCrawler(unittest.TestCase):
    def test_extract_stock_data(self):
        response = {
                #TODO
                }
        extract_stock_data()
        exp_dict = {
                'cmd_name' : 'command',
                '-t'       : 'job_type',
                '-p'       : '{"num1":1, "num2":2, "str1":"abcd", "str2":"efgh"}'
                }
        self.assertEqual(cmd_dict, exp_dict)

if __name__ == '__main__':
    unittest.main()

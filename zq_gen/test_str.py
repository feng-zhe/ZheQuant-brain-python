'''
Unit Tests for str.py
'''

import unittest
from .str import cmd_str2dic

# Unit test class
class TestString(unittest.TestCase):
    def test_json(self):
        cmd_str  = 'command -t job_type -p {"num1":1, "num2":2, "str1":"abcd", "str2":"efgh"}'
        cmd_dict = cmd_str2dic(cmd_str)
        exp_dict = {
                'cmd_name' : 'command',
                '-t'       : 'job_type', '-p'       : '{"num1":1, "num2":2, "str1":"abcd", "str2":"efgh"}'
                }
        self.assertEqual(cmd_dict, exp_dict)

    def test_schedule_cmd(self):
        cmd_str  = 'schedule -n job name -dsc job description -t job_type -p "-d 20 -n 5"'
        cmd_dict = cmd_str2dic(cmd_str)
        exp_dict = {
                'cmd_name' : 'schedule',
                '-n'       : 'job name',
                '-dsc'     : 'job description',
                '-t'       : 'job_type',
                '-p'       : '-d 20 -n 5'
                }
        self.assertEqual(cmd_dict, exp_dict)

    def test_mv_avg_cmd(self):
        cmd_str  = '-n 5 -d 20'
        cmd_dict = cmd_str2dic(cmd_str)
        exp_dict = {
                '-n':   '5',
                '-d':   '20'
                }
        self.assertEqual(cmd_dict, exp_dict)

    def test_crawl_cmd(self):
        cmd_str  = '-s 2017-11-11 -e 2017-11-18 -c 600497.SS'
        cmd_dict = cmd_str2dic(cmd_str)
        exp_dict = {
                '-s':   '2017-11-11',
                '-e':   '2017-11-18',
                '-c':   '600497.SS'
                }
        self.assertEqual(cmd_dict, exp_dict)

if __name__ == '__main__':
    unittest.main()

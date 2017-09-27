'''
Helper functions for string related operation
'''
import unittest

def cmd_str2dic(cmd_str):
    words = cmd_str.split()
    rst = {}
    if len(words) >= 1:
        begin = 0;
        if words[0][0:1] != '-':                # the first one could be the the name of the command
            rst['cmd_name'] = words[0]
            begin = 1
        curr_word = '...'                       # default parameter
        quoted = False
        curly_braced = False
        for word in words[begin:]:
            if quoted:                          # expecting the reverse double quote
                if word.endswith('"'):
                    quoted = False
                    word = word[:-1]
            elif curly_braced:                  # expecting the reverse curly brace
                if word.endswith('}'):
                    curly_braced = False
            else:
                if word[0:1]=='-':              # a new parameter
                    curr_word = word
                    rst[curr_word] = ''
                    continue
                if word.startswith('"'):        # meet double quote
                    if word.endswith('"'):
                        word = word[1:-1]
                    else:
                        quoted = True
                        word = word[1:]
                elif word.startswith('{'):      # meet curly brace
                    if not word.endswith('}'):
                        curly_braced = True
                                                # append to current parameter
            if len(rst[curr_word]) == 0:        # first value 
                rst[curr_word] += word
            else:                               # following value, add a space
                rst[curr_word] += ' '+word
    return rst

# Unit test class
class TestString(unittest.TestCase):
    def test_json(self):
        cmd_str  = 'command -t job_type -p {"num1":1, "num2":2, "str1":"abcd", "str2":"efgh"}'
        cmd_dict = cmd_str2dic(cmd_str)
        exp_dict = {
                'cmd_name' : 'command',
                '-t'       : 'job_type',
                '-p'       : '{"num1":1, "num2":2, "str1":"abcd", "str2":"efgh"}'
                }
        self.assertEqual(cmd_dict, exp_dict)

    def test_primary_cmd(self):
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

if __name__ == '__main__':
    unittest.main()

'''
Helper functions for string related operation
'''
import unittest

def cmd_str2dic(cmd_str):
    words = cmd_str.split()
    rst = {}
    if len(words) >= 1:
        begin = 0;
        if words[0][0:1] != '-': # the first one could the the name of the command
            rst['cmd_name'] = words[0]
            begin = 1
        curr_word = ''
        for word in words[begin:]:
            if word[0:1]=='-': # a new parameter
                curr_word = word
                rst[curr_word] = ''
            elif len(rst[curr_word])==0: # first value to current parameter
                rst[curr_word] += word
            else: # following value to current parameter
                rst[curr_word] += ' '+word
    return rst

# Unit test class
class TestString(unittest.TestCase):
    def test_primary_cmd(self):
        cmd_str = 'schedule -n JOB_NAME -dsc JOB_DESC JOB_DESC2 -t JOB_TYPE -p JOB_PARAMETERS'
        cmd_dict = cmd_str2dic(cmd_str)
        exp_dict = {
                'cmd_name': 'schedule',
                '-n':       'JOB_NAME',
                '-dsc':     'JOB_DESC JOB_DESC2',
                '-t':       'JOB_TYPE',
                '-p':       'JOB_PARAMETERS'
                }
        self.assertEqual(cmd_dict, exp_dict)

    def test_mv_avg_cmd(self):
        cmd_str = '-n 5 -d 20'
        cmd_dict = cmd_str2dic(cmd_str)
        exp_dict = {
                '-n':   '5',
                '-d':   '20'
                }
        self.assertEqual(cmd_dict, exp_dict)

if __name__ == '__main__':
    unittest.main()

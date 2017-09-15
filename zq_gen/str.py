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
        for word in words[begin:]:
            if quoted:                          # currently expecting the reverse double quote
                if word.endswith('"'):
                    quoted = False
                    word = word[:-1]
            else:
                if word[0:1]=='-':              # a new parameter
                    curr_word = word
                    rst[curr_word] = ''
                    continue
                if word.startswith('"'):
                    quoted = True
                    word = word[1:]
                                                # append to current parameter
            if len(rst[curr_word]) == 0:        # first value 
                rst[curr_word] += word
            else:                               # following value, add a space
                rst[curr_word] += ' '+word
    return rst

# Unit test class
class TestString(unittest.TestCase):
    def test_primary_cmd(self):
        cmd_str = 'schedule -n job name -dsc job description -t job_type -p "-d 20 -n 5"'
        cmd_dict = cmd_str2dic(cmd_str)
        exp_dict = {
                'cmd_name': 'schedule',
                '-n':       'job name',
                '-dsc':     'job description',
                '-t':       'job_type',
                '-p':       '-d 20 -n 5'
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

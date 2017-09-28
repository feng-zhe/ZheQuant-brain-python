'''
Helper functions for string related operation
'''

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

'''
Helper functions
'''

def cmd_str2dic(cmd_str):
    words = cmd_str.split()
    count = len(a)
    rst = {}
    if count>=1:
        rst['cmd_name'] = words[0]
        i = 1
        while i+1<count:
            rst[words[i]] = words[i+1]
    return rst

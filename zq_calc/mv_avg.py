'''
Module for Moving Average Calculator
'''

import zq_db.mongodb as zq_mgdb
import zq_gen.str as zq_genstr

def mv_avg(cmd_str):
    '''Calculate the top stocks ranked by moving average

    Args:
        cmd_str:    The command string
                    -d: days range used when calculating moving average
                    -n: number of the stocks returned
                    e.g: "-d 20 -n 5"
    Returns:
        A list of dicts representing the top n stocks ranked by moving average

    Raises:
       N/A
    '''
    days, num = _parse_params(cmd_str)
    rst = []
    # the data is a list of lists each of which represents docs of one stock
    data = zq_mgdb.get_recent_stock_data(days)
    for docs in data:
        code = docs[0]['code']
        prices = [doc['close'] for doc in docs]
        diff = _diff_avg(prices)
        rst.append({'code': code, 'diff': diff})
    rst = sorted(rst, key=lambda k: k['diff'], reverse=True)
    return rst[0:num]

def _parse_params(cmd):
    '''
    Extract parameters from command string

    Args:
        cmd:    The command string

    Returns:
        A tuple (days, number)

    Raises:
        N/A
    '''
    cmd_dict = zq_genstr.cmd_str2dic(cmd)
    days = int(cmd_dict['-d'])
    num = int(cmd_dict['-n'])
    return (days, num)

def _diff_avg(data):
    '''
    Calculate the current

    Args:
        data:   A list of float numbers

    Returns:
        The result of average value minus first value
        If there is error, it returns string 'N/A'
    '''
    if not data:
        return 'N/A'
    first = data[0]
    avg = sum(data)/len(data)
    return round(avg - first, 2)

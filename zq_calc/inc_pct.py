'''
This module contains calculator to calculate the increased percentage
'''

import json
import datetime
import pytz
import zq_gen.str as zq_str
import zq_db.mongodb as zq_mgdb

key_err_msg = 'Missing parameter in command string'
val_err_msg = 'Error in parsing the command string'

def inc_pct(cmd_str):
    '''
    Calculate the increasement by percentage

    Args:
        cmd_str:    A string of parameters
                    -c: The json of stock composition
                        e.g.
                        {
                            "test_code1": 200,
                            "test_code2": 300,
                            ...
                        }
                    -b: A string shows the begin date in format YYYYMMDD
                    -e: A string shows the end date in format YYYYMMDD

    Returns:
        A number with four decimals indicating the increasement percentage if succeed.
            e.g. return 0.0111 means 1.11%
        Otherwise returns a string indicating the problem.

    Raises:
        N/A
    '''
    try:
        compo, begin, end = _parse_cmd(cmd_str)
    except KeyError:
        return key_err_msg
    except ValueError:
        return val_err_msg
    begin_value = 0
    end_value = 0
    for code, num in compo.items():
        begin_doc = zq_mgdb.get_single_stock_data(code, begin)
        end_doc = zq_mgdb.get_single_stock_data(code, end)
        if not begin_doc or not end_doc:
            return 'No records in specified date'
        begin_value += begin_doc['close'] * num
        end_value += end_doc['close'] * num
    if not begin_value:
        return 'Begin value is zero, cannot calculate'
    return round((end_value - begin_value) / begin_value, 4)

def _parse_cmd(cmd_str):
    '''
    Parse the command string to get arguments

    Args:
        cmd_str:    A string of parameters

    Returns:
        A tuple (compo, begin, end) in which:
        The compo is the dictionary containing composition info.
        The begin is the datetime object for begin date.
        The end is the datatime object for end date.

    Raises:
        KeyError:       Thrown when there is missing parameters in command string
        ValueError:     Thrown when the input date string is not correct
    '''
    cmd_dict    = zq_str.cmd_str2dic(cmd_str)
    compo_str   = cmd_dict['-c']
    begin_str   = cmd_dict['-b']
    end_str     = cmd_dict['-e']
    begin_year  = int(begin_str[0:4])
    begin_month = int(begin_str[4:6])
    begin_day   = int(begin_str[6:])
    end_year    = int(end_str[0:4])
    end_month   = int(end_str[4:6])
    end_day     = int(end_str[6:])
    tzinfo = pytz.timezone('Asia/Shanghai')
    begin = datetime.datetime(begin_year, begin_month, begin_day, tzinfo=tzinfo)
    end = datetime.datetime(end_year, end_month, end_day, tzinfo=tzinfo)
    compo = json.loads(compo_str)
    return compo, begin, end


'''
Calculation Manager

It is the interface used by upper layer to 
determine which calcuator should be used
'''

import zq_calc.mv_avg as zq_ma
import zq_calc.inc_pct as zq_ip

MOVING_AVERAGE_STR = 'mv_avg'
INC_PERCENT_STR = 'inc_pct'
UNKNOWN_STR = 'not supported calculation'

def calc_mgr(cmd_dict, callback):
    rst = ''
    calc_type = cmd_dict['-t']
    param = cmd_dict['-p']
    if  calc_type == MOVING_AVERAGE_STR:
        print(' [x] Identified calculation for mv_avg(moving average)')
        rst = zq_ma.mv_avg(param)
    elif calc_type == INC_PERCENT_STR:
        print(' [x] Identified calculation for inc_pct(increasement by percentage)')
        rst = zq_ip.inc_pct(param)
    else:
        print(' [!] Unkown calculation type %s, skipped' % calc_type)
        rst = UNKNOWN_STR
    print(' [x] Calculation done')
    callback(rst)

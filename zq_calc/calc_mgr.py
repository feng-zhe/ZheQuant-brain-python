from zq_calc.mv_avg import mv_avg
from zq_calc.inc_pct import inc_pct

def calc_mgr(cmd_dict, cb):
    MOVING_AVERAGE_STR = 'mv_avg'                                       # moving average
    INC_PERCENT_STR = 'inc_pct'                                         # increasement by percentage
    rst = ''
    calc_type = cmd_dict['-t']
    param = cmd_dict['-p']
    if  calc_type == MOVING_AVERAGE_STR:
        print(' [x] Identified calculation for mv_avg(moving average)')
        rst = mv_avg(param) 
    elif calc_type == INC_PERCENT_STR:
        print(' [x] Identified calculation for inc_pct(increasement by percentage)')
        rst = inc_pct(param)
    else:
        print(' [!]Unkown calculation type %s, skipped' % calc_type)
        rst = 'not supported calculation'
    print(' [x] Calculation done')
    cb(rst)

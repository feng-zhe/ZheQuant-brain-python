from mv_avg import mv_avg

def calc_mgr(cmd_dict, cb):
    MOVING_AVERAGE_STR = 'mv_avg' # moving average
    INC_PERCENT_STR = 'inc_pct' # increasement by percentage
    rst = ''
    calc_type = cmd_dict['t']
    if  calc_type == MOVING_AVERAGE_STR:
        print('[x] Identify calculation for moving average')
        rst = mv_avg(cmd_dict)
        cb(rst)
    elif calc_type == MOVING_AVERAGE_STR:
        # TODO
        pass
    else:
        print(' [!]Unkown calculation type %s, skipped' % calc_type)
    cb(rst)
from zq_db.mongodb import get_recent_stock_data
from zq_gen.helper import cmd_str2dic

def mv_avg(cmd_str):
    '''Calculate the top stocks ranked by moving average

    Args:
        cmd_str:    The command string
                    -d: days range used when calculating moving average
                    -n: number of the stocks returned
    Returns:
        A list of dicts representing the top n stocks ranked by moving average

    Raises:
       N/A 
    '''
    cmd_dict = cmd_str2dic(cmd_str)
    days = int(cmd_dict['-d'])
    num = int(cmd_dict['-n'])
    data = get_recent_stock_data(days, num)
    pass # TODO

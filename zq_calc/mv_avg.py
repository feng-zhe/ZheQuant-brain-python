from zq_db.mongodb import get_recent_stock_data
from zq_gen.str import cmd_str2dic

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
    cmd_dict = cmd_str2dic(cmd_str)
    days = int(cmd_dict['-d'])
    num = int(cmd_dict['-n'])
    rst = []
    data = get_recent_stock_data(days)                                      # the data is a list of lists each of which represents docs of one stock
    for docs in data:
        price_now = docs[0]['close']
        code = docs[0]['code']
        sum = 0
        for doc in docs:                                                    # average price calculation includes the current price
            sum += doc['close']
        avg = sum/len(docs)
        diff = avg - price_now                                              # currently use average minus current price
        rst.append({'code': code, 'diff': diff})
    rst = sorted(rst, key=lambda k: k['diff'], reverse=True)
    return rst[0:num]

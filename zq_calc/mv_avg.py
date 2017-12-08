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
    cmd_dict = zq_genstr.cmd_str2dic(cmd_str)
    days = int(cmd_dict['-d'])
    num = int(cmd_dict['-n'])
    rst = []
    data = zq_mgdb.get_recent_stock_data(days)              # the data is a list of lists each of which represents docs of one stock
    for docs in data:
        price_now = docs[0]['close']
        code = docs[0]['code']
        sum = 0
        for doc in docs:                                    # average price calculation includes the current price
            sum += doc['close']
        avg = sum/len(docs)
        diff = round(avg-price_now, 2)                      # currently use average minus current price
        rst.append({'code': code, 'diff': diff})
    rst = sorted(rst, key=lambda k: k['diff'], reverse=True)
    return rst[0:num]

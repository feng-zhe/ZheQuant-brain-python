'''
The crawler to extract stock data from finance.yahoo.com
'''

import sys
import json
from datetime import datetime
import pytz
import requests
from zq_gen.str import cmd_str2dic

def request_data(start, end, code=None, interval='1d'):
    '''
    Send requests to yahoo to get data

    Args:
        start:      the start datetime
        end:        the end datetime
        code:       the code of the stock

    Returns:
        A string representing response if response status code is 200.
        Otherwise None if error.

    Raises:
        N/A
    '''

    url = 'https://query1.finance.yahoo.com/v8/finance/chart/' + code
    params = {
        'symbol'         : code,
        'period1'        : int(start.timestamp()),
        'period2'        : int(end.timestamp()),
        'interval'       : interval,
        'includePrePost' : 'true',
        'events'         : 'div|split|earn',
        'corsDomain'     : 'finance.yahoo.com'
    }

    rst = requests.get(url, params)
    if rst.status_code!=200:
        return None
    return rst.text

def validate_response(response):
    '''
    validate the response to make sure its structure is as expected

    Args:
        response:    a string representing the response

    Returns:
        True if validated successfully, False otherwise.

    Raises:
        None
    '''
    try:
        rsp = json.loads(response)
        code = rsp['chart']['result'][0]['meta']['symbol']
        timestamps = rsp['chart']['result'][0]['timestamp']
        volumes = rsp['chart']['result'][0]['indicators']['quote'][0]['volume']
        opens = rsp['chart']['result'][0]['indicators']['quote'][0]['open']
        closes = rsp['chart']['result'][0]['indicators']['quote'][0]['close']
        highs = rsp['chart']['result'][0]['indicators']['quote'][0]['high']
        lows = rsp['chart']['result'][0]['indicators']['quote'][0]['low']
        tzname = rsp['chart']['result'][0]['meta']['exchangeTimezoneName']
        if not code or not timestamps or not volumes or not opens\
            or not closes or not highs or not lows or not tzname:
            print('[!] one of the fileds in response is None')
            return False
        if not len(timestamps) == len(volumes) == len(closes) == len(highs) == len(lows):
            print('[!] fields in response are not consistent')
            return False
    except Exception as e:
        print('[!] exception raised during extraction:{0}'.format(e))
        return False
    except:
        print('[!] unknow exception/error raised during extraction:{0}'.format(sys.exc_info()[0]))
        return False
    else:
        return True

def extract_stock_data(response):
    '''
    Parse the returned dictionary object

    Args:
        response:    a string representing the response return by request

    Returns:
        A list of dicts as the stock data

    Raises:
        RuntimeError
    '''
    
    if not validate_response(response):
        raise RuntimeError('response validation failed')

    rsp = json.loads(response)
    code = rsp['chart']['result'][0]['meta']['symbol']
    timestamps = rsp['chart']['result'][0]['timestamp']
    volumes = rsp['chart']['result'][0]['indicators']['quote'][0]['volume']
    opens = rsp['chart']['result'][0]['indicators']['quote'][0]['open']
    closes = rsp['chart']['result'][0]['indicators']['quote'][0]['close']
    highs = rsp['chart']['result'][0]['indicators']['quote'][0]['high']
    lows = rsp['chart']['result'][0]['indicators']['quote'][0]['low']
    tzname = rsp['chart']['result'][0]['meta']['exchangeTimezoneName']
    lens = len(timestamps)

    tzinfo = pytz.timezone(tzname)

    return [
        {
            'code'   : code,
            'date'   : datetime.fromtimestamp(timestamps[i], tz=tzinfo)\
                                .replace(hour=15, minute=0, second=0, microsecond=0),
            'volume' : volumes[i],
            'open'   : round(opens[i], 2),
            'close'  : round(closes[i], 2),
            'high'   : round(highs[i], 2),
            'low'    : round(lows[i], 2)
        } for i in range(0, lens) if volumes[i]]

def crawl(cmd):
    '''
    Main function to parse the command and then start crawling

    Args:
        cmd:    The command string.
                "-s" for start date. "-e" for end date.
                "-c" for stock code.
                e.g.: -s YYYY-MM-DD -e YYYY-MM-DD -c XXXXXX.SS

    Returns:
        True if no exception occurred.
        Otherwise False

    Raises:
        N/A
    '''
    #TODO
    opts = cmd_str2dic(cmd)
    try:
        opt_s = opts['-s']
        opt_e = opts['-e']
        code = opts['-c']
        syear = int(opt_s[0:4])
        smonth = int(opt_s[5:7])
        sday = int(opt_s[8:10])
        eyear = int(opt_e[0:4])
        emonth = int(opt_e[5:7])
        eday = int(opt_e[8:10])
    except Exception as e:
        print('[!] Error during parsing the command (crawl)')
        return False
    except:
        print('[!] Unkown error (crawl)')
        return False
    else:
        tzinfo = pytz.timezone('Asia/Shanghai')
        start = datetime(syear, smonth, sday, tzinfo=tzinfo)
        end = datetime(eyear, emonth, eday, tzinfo=tzinfo)
        rsp = request_data(start, end, code)
        docs = extract_stock_data(rsp)
        print('[+] Crawled {0} records'.format(len(docs)))
        if insert_stock_data(docs):
            print('[+] Insert to db successfully')
            return True
        else:
            print('[!] Failed to insert to db')
            return False

def insert_stock_data(docs):
    '''
    Insert document into database

    Args:
        docs:    the documents to be inserted

    Returns:
        True for success, False otherwise.

    Raises:
        N/A
    '''
    #TODO
    pass

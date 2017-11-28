'''
The crawler to extract stock data from finance.yahoo.com
'''

import requests
import pytz
from datetime import datetime

def request_data(start, end, code=None):
    '''
    Send requests to yahoo to get data

    Args:
        start:      the start datetime
        end:        the end datetime
        code:       the code of the stock

    Returns:
        A dictionary representing the json in response.
        Otherwise None if error.

    Raises:
        N/A
    ''' #TODO
    pass

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

def extract_stock_data(rsp):
    '''
    Parse the returned dictionary object

    Args:
        rsp:    a dictionary representing the response return by request

    Returns:
        A list of dicts as the stock data

    Raises:
        KeyError, TypeError, IndexError, RuntimeError
    '''
    code       = rsp['chart']['result'][0]['meta']['symbol']
    timestamps = rsp['chart']['result'][0]['timestamp']
    volumes    = rsp['chart']['result'][0]['indicators']['quote'][0]['volume']
    closes     = rsp['chart']['result'][0]['indicators']['quote'][0]['close']
    highs      = rsp['chart']['result'][0]['indicators']['quote'][0]['high']
    lows       = rsp['chart']['result'][0]['indicators']['quote'][0]['low']
    lens       = len(timestamps)

    if not len(timestamps)==len(volumes)==len(closes)==len(highs)==len(lows):
        raise RunetimeError('Length of data fields is not consistent')

    tz = pytz.timezone('Asia/Shanghai')
    return [{
            'code'   : code,
            'date'   : datetime.fromtimestamp(timestamps[i],tz=tz).replace(hour=15,minute=0,second=0,microsecond=0),
            'volume' : volumes[i],
            'close'  : round(closes[i],2),
            'high'   : round(highs[i],2),
            'low'    : round(lows[i],2)
            } for i in range(0,lens) if(volumes[i])]

def crawl(cmd):
    '''
    Main function

    Args:
        cmd:    The command string

    Returns:
        None

    Raises:
        N/A
    '''
    #TODO
    pass

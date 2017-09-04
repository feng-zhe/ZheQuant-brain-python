'''
This file contains the functions to read data from mongodb
'''

from pymongo import MongoClient
import datetime

def get_db_client():
    ''' get the db client or None if error '''
    client = MongoClient('db', 27017)
    try: # this is because of change in pymongo 3.0, we have to do this
        client.admin.command('ismaster') # The ismaster command is cheap and does not require auth.
        return client
    except errors.ConnectionFailure:
        print("Server not available")
        return None

def get_stock_data(stock_dict):
    '''Get the data of the stock specified by the input

    This function retreives data of ONLY one stock.

    Args:
        stock_dict: A dict mapping information about the stock 
            to be queried. For example:
            {
                'code': 'XXXXXX',
                'start_date': datatime.datatime(YYYY,MM,DD,tzinfo=timezone.utc)
                'end_date': datatime.datatime(YYYY,MM,DD,tzinfo=timezone.utc)
            }
    Returns:
        A list of dicts each contains the data of this stock of one day.
        And it is sorted descending by date.
        For example:
        [
            {
                'date': datatime.datatime(YYYY,MM,DD,tzinfo=timezone.utc)
                'open_price': xx.xx,
                'close_price': xx.xx
            },
            ...
        ]
    '''
    client = get_db_client()
    if not client:
        return False
    db = client.fin
    filter_dict = {
            'code':stock_dict['code'],
            'date':{
                '$gte':stock_dict['start_date'],
                '$lte':stock_dict['end_date']
                }
            }
    proj_dict = {
            'date': True,
            'open_price': True,
            'close_price': True
            }
    sort_list = [('date':pymongo.DESCENDING)]
    cursor = db.find(filter=filter_dict, projection=proj_dict, sort=sort_list)
    return list(cursor)

'''
This file contains the functions to read data from mongodb
'''

import pymongo
import datetime

def get_db_client():
    ''' Get the db client or None if error 
    
    Returns:
        The database object for later usage if succeeded, None otherwise.
        
    Raises:
        N/A
    '''
    client = pymongo.MongoClient('db', 27017)
    try: # this is because of change in pymongo 3.0, we have to do this
        client.admin.command('ismaster') # The ismaster command is cheap and does not require auth.
        return client
    except errors.ConnectionFailure:
        print("Server not available")
        return None

def get_recent_stock_data(days, code=None):
    '''Get the data of the stock specified by the input

    This function retreives data of ONLY one stock.

    Args:
        days:   The length of the days
        code:   (Optional) the code of the stock. If omited,
                it will retreive data of all stock codes
    Returns:
        If called with one stock code, it returns a list of dicts 
        each contains the data of this stock of one day.
        If called with no stock code, it returns a list of lists of dicts
        No matter which way it is called, the result is sorted descending by date.
    
    Raises:
        N/A
    '''
    client = get_db_client()
    if not client:
        return False
    db = client.fin
    if code:
        filter_dict = { 'code': code }
        proj_dict = {
                '_id'   : False,
                'code'  : True,
                'date'  : True,
                'open'  : True,
                'close' : True,
                'high'  : True,
                'low'   : True
                }
        sort_list = [('date',pymongo.DESCENDING)]
        cursor = db.stocks.find(filter=filter_dict, projection=proj_dict, sort=sort_list, limit=days)
        return list(cursor)
    else:
        codes = get_code_list()
        return [get_recent_stock_data(days,x) for x in codes]

def get_code_list():
    ''' Get a list of stock codes 
    
    Returns:
        A list of stock codes.
    
    Raises:
        N/A
    '''
    client = get_db_client()
    if not client:
        return False
    db = client.fin
    pipeline = [ { '$group': {'_id':'$code'} } ]
    cursor = db.stocks.aggregate(pipeline)
    return [doc['_id'] for doc in list(cursor)]

def get_single_stock_data(code, dt):
    '''Get data of the stock on the specified date
    
    This function retrieves one data of the stock and date specified

    Args:
        code : A string which is the code of the stock
        dt   : A datetime object which is the date of the record

    Returns:
        A dictionary which contains transcation information 
        of the specified stock on the specified date

    Raises:
        N/A
    '''
    client = get_db_client()
    if not client:
        return {}
    db = client.fin
    find_filter = { 
            'code': code, 
            'date': dt 
            }
    return db.stocks.find_one(filter=find_filter)
    


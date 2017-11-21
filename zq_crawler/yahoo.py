'''
The crawler to extract stock data from finance.yahoo.com
'''

import requests

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
    '''
    #TODO
    pass

def insert_data(docs):
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

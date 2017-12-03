'''
Unit Tests for yahoo.py
'''

import unittest
import json
import random
from datetime import datetime
from datetime import timedelta
import pytz
from zq_crawler.yahoo import *

# Unit test class
class TestYahooCrawler(unittest.TestCase):
    '''
    Test case for yahoo crawler
    '''
    # test response string
    _rsp_str = '{"chart":{"result":[{"meta":{"currency":"CNY","symbol":"600497.SS",\
                "exchangeName":"SHH","instrumentType":"EQUITY","firstTradeDate":1082424600,\
                "gmtoffset":28800,"timezone":"CST","exchangeTimezoneName":"Asia/Shanghai",\
                "currentTradingPeriod":{"pre":{"timezone":"CST","end":1511746200,"start":1511746200,\
                "gmtoffset":28800},"regular":{"timezone":"CST","end":1511766000,"start":1511746200,\
                "gmtoffset":28800},"post":{"timezone":"CST","end":1511766000,"start":1511766000,\
                "gmtoffset":28800}},"dataGranularity":"1d","validRanges":["1d","5d","1mo","3mo",\
                "6mo","1y","2y","5y","10y","ytd","max"]},"timestamp":[1510709400,1510795800,\
                1510882200,1511141400,1511227800,1511314200,1511400600,1511487000,1511746200],\
                "indicators":{"quote":[{"low":[null,6.489999771118164,6.099999904632568,6.03000020980835,\
                6.119999885559082,6.170000076293945,6.230000019073486,6.190000057220459,6.449999809265137],\
                "volume":[null,34039227,53016969,28656684,39235021,41324595,63648648,52108224,54005417],\
                "close":[null,6.510000228881836,6.199999809265137,6.239999771118164,6.179999828338623,\
                6.269999980926514,6.309999942779541,6.5,6.510000228881836],"open":[null,6.650000095367432,\
                6.46999979019165,6.199999809265137,6.210000038146973,6.269999980926514,6.289999961853027,\
                6.25,6.489999771118164],"high":[null,6.679999828338623,6.539999961853027,6.260000228881836,\
                6.260000228881836,6.28000020980835,6.480000019073486,6.519999980926514,6.670000076293945]}],\
                "unadjclose":[{"unadjclose":[null,6.510000228881836,6.199999809265137,6.239999771118164,\
                6.179999828338623,6.269999980926514,6.309999942779541,6.5,6.510000228881836]}],\
                "adjclose":[{"adjclose":[null,6.510000228881836,6.199999809265137,6.239999771118164,\
                6.179999828338623,6.269999980926514,6.309999942779541,6.5,6.510000228881836]}]}}],\
                "error":null}}'

    def test_validate_response(self):
        '''
        Test response validation
        '''
        self.assertTrue(validate_response(self._rsp_str))

    def test_extract_stock_data(self):
        '''
        Test extracting data from response
        '''
        act_docs = extract_stock_data(self._rsp_str)
        tzinfo = pytz.timezone('Asia/Shanghai')
        exp_docs = [
            {
                'code'   : '600497.SS',
                # set to close time because we use close time
                'date'   : datetime.fromtimestamp(1510795800, tz=tzinfo)\
                                    .replace(hour=15, minute=0, second=0, microsecond=0),
                'volume' : 34039227,
                'open'   : 6.65,
                'close'  : 6.51,
                'low'    : 6.49,
                'high'   : 6.68
            },
            {
                'code'   : '600497.SS',
                'date'   : datetime.fromtimestamp(1510882200, tz=tzinfo)\
                                    .replace(hour=15, minute=0, second=0, microsecond=0),
                'volume' : 53016969,
                'open'   : 6.47,
                'close'  : 6.20,
                'low'    : 6.10,
                'high'   : 6.54
            },
            {
                'code'   : '600497.SS',
                'date'   : datetime.fromtimestamp(1511141400, tz=tzinfo)\
                                    .replace(hour=15, minute=0, second=0, microsecond=0),
                'volume' : 28656684,
                'open'   : 6.20,
                'close'  : 6.24,
                'low'    : 6.03,
                'high'   : 6.26
            },
            {
                'code'   : '600497.SS',
                'date'   : datetime.fromtimestamp(1511227800, tz=tzinfo)\
                                    .replace(hour=15, minute=0, second=0, microsecond=0),
                'volume' : 39235021,
                'open'   : 6.21,
                'close'  : 6.18,
                'low'    : 6.12,
                'high'   : 6.26
            },
            {
                'code'   : '600497.SS',
                'date'   : datetime.fromtimestamp(1511314200, tz=tzinfo)\
                                    .replace(hour=15, minute=0, second=0, microsecond=0),
                'volume' : 41324595,
                'open'   : 6.27,
                'close'  : 6.27,
                'low'    : 6.17,
                'high'   : 6.28
            },
            {
                'code'   : '600497.SS',
                'date'   : datetime.fromtimestamp(1511400600, tz=tzinfo)\
                                    .replace(hour=15, minute=0, second=0, microsecond=0),
                'volume' : 63648648,
                'open'   : 6.29,
                'close'  : 6.31,
                'low'    : 6.23,
                'high'   : 6.48
            },
            {
                'code'   : '600497.SS',
                'date'   : datetime.fromtimestamp(1511487000, tz=tzinfo)\
                                    .replace(hour=15, minute=0, second=0, microsecond=0),
                'volume' : 52108224,
                'open'   : 6.25,
                'close'  : 6.50,
                'low'    : 6.19,
                'high'   : 6.52
            },
            {
                'code'   : '600497.SS',
                'date'   : datetime.fromtimestamp(1511746200, tz=tzinfo)\
                                    .replace(hour=15, minute=0, second=0, microsecond=0),
                'volume' : 54005417,
                'open'   : 6.49,
                'close'  : 6.51,
                'low'    : 6.45,
                'high'   : 6.67
            }
            ]
        self.assertEqual(act_docs, exp_docs)

    def test_request_data(self):
        '''
        Test request data from internet. 
        
        The internet connection must be correct. So as the response format.
        '''
        tzinfo = pytz.timezone('Asia/Shanghai')
        start = datetime(2017, 11, 18, tzinfo=tzinfo)
        end = datetime(2017, 11, 22, tzinfo=tzinfo)
        rsp = request_data(start, end, '600497.SS')
        self.assertIsNotNone(rsp)
        self.assertTrue(validate_response(rsp))

    def test_one_attempt(self):
        '''
        Go through one attempt to crawl data

        Aassuming there is no 15-day continuous vacation
        Otherwise the test may fail
        '''
        tzinfo = pytz.timezone('Asia/Shanghai')
        month = random.randint(1, 11)
        day = random.randint(1, 20)
        start = datetime(2017, month, day, tzinfo=tzinfo)
        end = start + timedelta(days=15)            
        rsp = request_data(start, end, '600497.SS')
        self.assertIsNotNone(rsp)
        self.assertTrue(validate_response(rsp))
        docs = extract_stock_data(rsp)
        self.assertNotEqual(len(docs), 0)

if __name__ == '__main__':
    unittest.main()

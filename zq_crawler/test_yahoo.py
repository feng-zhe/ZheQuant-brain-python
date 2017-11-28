'''
Unit Tests for yahoo.py
'''

import unittest
import json
import pytz
from datetime import datetime
from .yahoo import *

# Unit test class
class TestYahooCrawler(unittest.TestCase):
    def test_extract_stock_data(self):
        rsp_str = '{"chart":{"result":[{"meta":{"currency":"CNY","symbol":"600497.SS","exchangeName":"SHH","instrumentType":"EQUITY","firstTradeDate":1082424600,"gmtoffset":28800,"timezone":"CST","exchangeTimezoneName":"Asia/Shanghai","currentTradingPeriod":{"pre":{"timezone":"CST","end":1511746200,"start":1511746200,"gmtoffset":28800},"regular":{"timezone":"CST","end":1511766000,"start":1511746200,"gmtoffset":28800},"post":{"timezone":"CST","end":1511766000,"start":1511766000,"gmtoffset":28800}},"dataGranularity":"1d","validRanges":["1d","5d","1mo","3mo","6mo","1y","2y","5y","10y","ytd","max"]},"timestamp":[1510709400,1510795800,1510882200,1511141400,1511227800,1511314200,1511400600,1511487000,1511766003],"indicators":{"quote":[{"low":[null,6.489999771118164,6.099999904632568,6.03000020980835,6.119999885559082,6.170000076293945,6.230000019073486,6.190000057220459,6.449999809265137],"volume":[null,34039227,53016969,28656684,39235021,41324595,63648648,52108224,54005417],"close":[null,6.510000228881836,6.199999809265137,6.239999771118164,6.179999828338623,6.269999980926514,6.309999942779541,6.5,6.510000228881836],"open":[null,6.650000095367432,6.46999979019165,6.199999809265137,6.210000038146973,6.269999980926514,6.289999961853027,6.25,6.489999771118164],"high":[null,6.679999828338623,6.539999961853027,6.260000228881836,6.260000228881836,6.28000020980835,6.480000019073486,6.519999980926514,6.670000076293945]}],"unadjclose":[{"unadjclose":[null,6.510000228881836,6.199999809265137,6.239999771118164,6.179999828338623,6.269999980926514,6.309999942779541,6.5,6.510000228881836]}],"adjclose":[{"adjclose":[null,6.510000228881836,6.199999809265137,6.239999771118164,6.179999828338623,6.269999980926514,6.309999942779541,6.5,6.510000228881836]}]}}],"error":null}}'
        response = json.loads(rsp_str)
        act_docs = extract_stock_data(response)
        tz = pytz.timezone('Asia/Shanghai')
        exp_docs = [
                {
                    'code'   : '600497.SS',
                    'date'   : datetime.fromtimestamp(1510795800, tz=tz).replace(hour=15, minute=0, second=0, microsecond=0),    # set to close time because we use close time
                    'volume' : 34039227,
                    'close'  : 6.51,
                    'low'    : 6.49,
                    'high'   : 6.68
                },
                {
                    'code'   : '600497.SS',
                    'date'   : datetime.fromtimestamp(1510882200, tz=tz).replace(hour=15, minute=0, second=0, microsecond=0),
                    'volume' : 53016969,
                    'close'  : 6.20,
                    'low'    : 6.10,
                    'high'   : 6.54
                },
                {
                    'code'   : '600497.SS',
                    'date'   : datetime.fromtimestamp(1511141400, tz=tz).replace(hour=15, minute=0, second=0, microsecond=0),
                    'volume' : 28656684,
                    'close'  : 6.24,
                    'low'    : 6.03,
                    'high'   : 6.26
                },
                {
                    'code'   : '600497.SS',
                    'date'   : datetime.fromtimestamp(1511227800, tz=tz).replace(hour=15, minute=0, second=0, microsecond=0),
                    'volume' : 39235021,
                    'close'  : 6.18,
                    'low'    : 6.12,
                    'high'   : 6.26
                },
                {
                    'code'   : '600497.SS',
                    'date'   : datetime.fromtimestamp(1511314200, tz=tz).replace(hour=15, minute=0, second=0, microsecond=0),
                    'volume' : 41324595,
                    'close'  : 6.27,
                    'low'    : 6.17,
                    'high'   : 6.28
                },
                {
                    'code'   : '600497.SS',
                    'date'   : datetime.fromtimestamp(1511400600, tz=tz).replace(hour=15, minute=0, second=0, microsecond=0),
                    'volume' : 63648648,
                    'close'  : 6.31,
                    'low'    : 6.23,
                    'high'   : 6.48
                },
                {
                    'code'   : '600497.SS',
                    'date'   : datetime.fromtimestamp(1511487000, tz=tz).replace(hour=15, minute=0, second=0, microsecond=0),
                    'volume' : 52108224,
                    'close'  : 6.50,
                    'low'    : 6.19,
                    'high'   : 6.52
                },
                {
                    'code'   : '600497.SS',
                    'date'   : datetime.fromtimestamp(1511766003, tz=tz).replace(hour=15, minute=0, second=0, microsecond=0),
                    'volume' : 54005417,
                    'close'  : 6.51,
                    'low'    : 6.45,
                    'high'   : 6.67
                }
                ]
        self.assertEqual(act_docs, exp_docs)

if __name__ == '__main__':
    unittest.main()

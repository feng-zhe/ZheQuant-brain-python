import unittest
import unittest.mock as mock
from datetime import datetime
import pytz
import zq_calc.inc_pct as zq_inc_pct

tzinfo = pytz.timezone('Asia/Shanghai')

def mock_db_func(code, date):
    mock_data = [
        {
            'code'  : 'test_code_1',
            'date'  : datetime(2017,12,11,tzinfo=tzinfo),
            'close' : 11.36
        },
        {
            'code'  : 'test_code_1',
            'date'  : datetime(2017,12,15,tzinfo=tzinfo),
            'close' : 13.13
        },
        {
            'code'  : 'test_code_2',
            'date'  : datetime(2017,12,11,tzinfo=tzinfo),
            'close' : 6.10
        },
        {
            'code'  : 'test_code_2',
            'date'  : datetime(2017,12,15,tzinfo=tzinfo),
            'close' : 5.83
        }
        ]
    for item in mock_data:
        if item['code']==code and item['date']==date:
            return item

class TestIncreasingPercentage(unittest.TestCase):
    '''
    Test increasing percentage module
    '''
    @mock.patch('zq_db.mongodb.get_single_stock_data')
    def test_inc_pct(self, mocked_func):
        mocked_func.side_effect = mock_db_func
        cmd_str = '-c {"test_code_1":100, "test_code_2":200} -b 20171211 -e 20171215'
        act_rst = zq_inc_pct.inc_pct(cmd_str)
        exp_rst = 0.0522
        self.assertEqual(act_rst, exp_rst)

    def test_parse_cmd(self):
        # normal case
        cmd_str = '-c {"test_code_1":100, "test_code_2":200} -b 20171211 -e 20171215'
        act_rst = zq_inc_pct._parse_cmd(cmd_str)
        exp_rst = (
                {'test_code_1':100,'test_code_2':200},
                datetime(2017, 12, 11, tzinfo=tzinfo),
                datetime(2017, 12, 15, tzinfo=tzinfo)
                )
        self.assertEqual(act_rst, exp_rst)
        # KeyError case
        cmd_str = '-c {"test_code_1":100, "test_code_2":200} -b 20171211'
        with self.assertRaises(KeyError):
            zq_inc_pct._parse_cmd(cmd_str)
        # ValueError case
        cmd_str = '-c {"test_code_1":100, "test_code_2":200} -b 201712aa -e 201712bb'
        with self.assertRaises(ValueError):
            zq_inc_pct._parse_cmd(cmd_str)

if __name__ == '__main__':
    unittest.main()

import unittest
import unittest.mock as mock
import zq_calc.inc_pct as zq_inc_pct

class TestIncreasingPercentage(unittest.TestCase):
    '''
    Test increasing percentage module
    '''
    @mock.patch('zq_db.mongodb.get_single_stock_data')
    def test_inc_pct(self, mocked_db_func):
        mocked_db_func.side_effect = [
                {'code':'test_code_1','close':11.36},
                {'code':'test_code_1','close':13.13}]
        cmd_str = '-c {"test_code_1":100} -b 20171211 -e 20171215'
        act_rst = zq_inc_pct.inc_pct(cmd_str)
        exp_rst = 0.1558
        self.assertEqual(act_rst, exp_rst)

if __name__ == '__main__':
    unittest.main()

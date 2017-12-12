import unittest
import unittest.mock as mock
import zq_calc.mv_avg as zq_calc_ma

class TestMovingAverage(unittest.TestCase):
    '''
    Test Moving Average Calculator
    '''
    _example_stock_data = [
            [   
                {'code':'test_code_1','close':1},
                {'code':'test_code_1','close':2},
                {'code':'test_code_1','close':3},
                {'code':'test_code_1','close':4},
                {'code':'test_code_1','close':5},
            ],
            [   
                {'code':'test_code_2','close':1.11},
                {'code':'test_code_2','close':2.22},
                {'code':'test_code_2','close':3.33},
                {'code':'test_code_2','close':4.44},
                {'code':'test_code_2','close':5.55},
            ],
            [   
                {'code':'test_code_3','close':1.22},
                {'code':'test_code_3','close':2.33},
                {'code':'test_code_3','close':3.44},
                {'code':'test_code_3','close':4.55},
                {'code':'test_code_3','close':5.66},
            ],
            [   
                {'code':'test_code_4','close':1.33},
                {'code':'test_code_4','close':2.44},
                {'code':'test_code_4','close':3.55},
                {'code':'test_code_4','close':5.66},
                {'code':'test_code_4','close':6.77},
            ],
            [   
                {'code':'test_code_5','close':3.54},
                {'code':'test_code_5','close':2.33},
                {'code':'test_code_5','close':6.48},
                {'code':'test_code_5','close':7.85},
                {'code':'test_code_5','close':3.22},
            ],
            [   
                {'code':'test_code_6','close':8.93},
                {'code':'test_code_6','close':7.01},
                {'code':'test_code_6','close':6.98},
                {'code':'test_code_6','close':7.20},
                {'code':'test_code_6','close':7.83},
            ]
        ]

    def test_parse_params(self):
        '''
        Test extract parameters from command lines
        '''
        cmd = '-d 20 -n 5'
        act_rst = zq_calc_ma._parse_params(cmd)
        exp_rst = (20, 5)
        self.assertEqual(act_rst, exp_rst)

    def test_diff_avg(self):
        '''
        Test the math function to calculate difference
        '''
        data = []
        act_rst = zq_calc_ma._diff_avg(data)
        exp_rst = 'N/A'
        self.assertEqual(act_rst, exp_rst)
        data = [1.09, 2.57, 3.79, 4.77, 5.33, 6.23]
        act_rst = zq_calc_ma._diff_avg(data)
        exp_rst = 2.87
        self.assertEqual(act_rst, exp_rst)

    @mock.patch('zq_db.mongodb.get_recent_stock_data')
    def test_mv_avg(self, mocked_func):
        '''
        Test the mv_avg
        '''
        # assign the test data
        mocked_func.return_value = self._example_stock_data
        act_rst = zq_calc_ma.mv_avg('-d 5 -n 5')
        exp_rst = [
                {'code': 'test_code_4', 'diff': 2.62}, 
                {'code': 'test_code_2', 'diff': 2.22}, 
                {'code': 'test_code_3', 'diff': 2.22},
                {'code': 'test_code_1', 'diff': 2.0},
                {'code': 'test_code_5', 'diff': 1.14}
            ]
        self.assertEqual(act_rst, exp_rst)

if __name__ == '__main__':
    unittest.main()

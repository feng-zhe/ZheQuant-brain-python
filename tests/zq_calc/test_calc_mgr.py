'''
This module contains test cases for calculation manager
'''

import unittest
import unittest.mock as mock
import zq_calc.calc_mgr as zq_cm

class TestCalculationManager(unittest.TestCase):
    '''
    Test Cases for calculation mamager
    '''
    @mock.patch('zq_calc.mv_avg.mv_avg')
    @mock.patch('zq_calc.inc_pct.inc_pct')
    def test_call_mv_avg(self, mocked_inc_pct, mocked_mv_avg):
        '''
        Invoke moving average calculator
        '''
        mv_avg_rst = 'moving average'
        mocked_mv_avg.return_value = mv_avg_rst
        cmd_dict = {
                '-t':   zq_cm.MOVING_AVERAGE_STR,
                '-p':   '<test parameters>'
                }
        callback = mock.MagicMock()
        zq_cm.calc_mgr(cmd_dict, callback)
        self.assertTrue(mocked_mv_avg.called)
        callback.assert_called_with(mv_avg_rst)
        self.assertFalse(mocked_inc_pct.called)
    
    @mock.patch('zq_calc.mv_avg.mv_avg')
    @mock.patch('zq_calc.inc_pct.inc_pct')
    def test_call_inc_pct(self, mocked_inc_pct, mocked_mv_avg):
        '''
        Invoke increasing percentage
        '''
        inc_pct_rst = 'increasing percentage'
        mocked_inc_pct.return_value = inc_pct_rst
        cmd_dict = {
                '-t':   zq_cm.INC_PERCENT_STR,
                '-p':   '<test parameters>'
                }
        callback = mock.MagicMock()
        zq_cm.calc_mgr(cmd_dict, callback)
        self.assertFalse(mocked_mv_avg.called)
        self.assertTrue(mocked_inc_pct.called)
        callback.assert_called_with(inc_pct_rst)

    @mock.patch('zq_calc.mv_avg.mv_avg')
    @mock.patch('zq_calc.inc_pct.inc_pct')
    def test_unknown_type(self, mocked_inc_pct, mocked_mv_avg):
        '''
        Invoke with unknown calculator type
        '''
        cmd_dict = {
                '-t':   'unkOwn',
                '-p':   '<test parameters>'
                }
        callback = mock.MagicMock()
        zq_cm.calc_mgr(cmd_dict, callback)
        self.assertFalse(mocked_mv_avg.called)
        self.assertFalse(mocked_inc_pct.called)
        callback.assert_called_with(zq_cm.UNKNOWN_STR)

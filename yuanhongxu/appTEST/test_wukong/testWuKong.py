# coding:utf-8
import unittest
from appium import webdriver
import time
from wukong_element import WuKong
from . import config


class MyTestCase(unittest.TestCase):

    def setUp(cls):
        desired_caps = {}
        desired_caps["platformName"] = config.platformName
        desired_caps["platformVersion"] = config.platformVersion
        desired_caps["deviceName"] = config.deviceName
        desired_caps["appPackage"] = config.appPackage
        desired_caps["appActivity"] = config.appActivity
        # desired_caps["automationName"] = config.automationName
        desired_caps["unicodeKeyboard"] = config.unicodeKeyboard
        desired_caps["resetKeyboard"] = config.resetKeyboard
        desired_caps["noReset"] = config.noReset
        url = 'http://%s:%s/wd/hub' % (config.ip, config.port)
        cls.driver = webdriver.Remote(url, desired_caps)
        # time.sleep(10)

        cls.wk = WuKong(cls.driver)

    def test_case01(self):
        self.wk.ele_db_bt.click()
        self.wk.ele_dshhk.click()
        self.wk.ele_dshhk_first.click()
        act_result = self.wk.ele_hkxqzt.get_attribute('contentDescription')
        exp_result = u"待审核"
        self.assertEqual(act_result, exp_result)

    def test_case02(self):
        self.wk.ele_db_bt.click()
        self.wk.ele_dshhk.click()
        self.wk.ele_dsh_xlk.click()
        self.wk.ele_ysh_xlk.click()
        self.wk.ele_dshhk_yjj.click()
        act_result = self.wk.ele_hkxqzt_shjj.get_attribute('contentDescription')
        exp_result = u"审核拒绝"
        self.assertEqual(act_result, exp_result)

    def test_case03(self):
        self.wk.ele_sj.click()
        self.wk.ele_xzsj.click()
        self.wk.ele_sjmc.send_keys(u"学习")
        self.wk.ele_khmc.click()
        self.wk.ele_choose_kh.click()
        self.wk.ele_return.click()
        self.wk.ele_sjzzt.click()
        self.wk.ele_choose_sjz.click()
        self.wk.ele_return.click()
        self.wk.ele_sjjd.click()
        self.wk.ele_choose_sjjd.click()
        self.wk.ele_return.click()
        self.wk.ele_sjje.send_keys(145)
        self.wk.ele_bc.click()
        time.sleep(1)
        act_result = self.wk.ele_sjnr.get_attribute('contentDescription')
        exp_result = u"学习"
        self.assertEqual(act_result, exp_result)

    def test_case04(self):
        self.wk.ele_sj.click()
        self.wk.ele_xzsj.click()
        self.wk.ele_sjmc.send_keys(u"aaa")
        self.wk.ele_khmc.click()
        self.wk.ele_choose_kh.click()
        self.wk.ele_return.click()
        self.wk.ele_sjzzt.click()
        self.wk.ele_choose_sjz.click()
        self.wk.ele_return.click()
        self.wk.ele_sjjd.click()
        self.wk.ele_choose_sjjd.click()
        self.wk.ele_return.click()
        self.wk.ele_sjje.send_keys(145)
        self.wk.ele_bc.click()
        act_result = self.wk.ele_sj_sjje.get_attribute('contentDescription')
        exp_result = u"145.00"
        self.assertEqual(act_result, exp_result)

    def test_case05(self):
        self.wk.ele_sj.click()
        self.wk.ele_xzsj.click()
        self.wk.ele_sjmc.send_keys(u"996")
        self.wk.ele_khmc.click()
        self.wk.ele_choose_kh.click()
        self.wk.ele_return.click()
        self.wk.ele_sjzzt.click()
        self.wk.ele_choose_sjz.click()
        self.wk.ele_return.click()
        self.wk.ele_sjjd.click()
        self.wk.ele_choose_tpsh.click()
        self.wk.ele_return.click()
        self.wk.ele_sjje.send_keys(146)
        self.wk.ele_bc.click()
        act_result = self.wk.ele_sj_sjjd.get_attribute('contentDescription')
        exp_result = u"谈判审核"
        self.assertEqual(exp_result, act_result)

    def test_case06(self):
        self.wk.ele_wd.click()
        act_result = self.wk.ele_wd_yh.get_attribute('contentDescription')
        exp_result = u"管理员"
        self.assertEqual(exp_result, act_result)

    def test_case07(self):
        self.wk.ele_wd.click()
        self.wk.ele_wd_sddrz.click()
        act_result = self.wk.ele_wd_rz.get_attribute('contentDescription')
        exp_result = u"我收到的"
        self.assertEqual(exp_result, act_result)

    def test_case08(self):
        self.wk.ele_wd.click()
        self.wk.ele_wd_dwsp.click()
        act_result = self.wk.ele_wd_dwspd.get_attribute('contentDescription')
        exp_result = u"待我审批的"
        self.assertEqual(exp_result, act_result)

    def test_case09(self):
        self.wk.ele_bg.click()
        act_result = self.wk.ele_bg_sp.get_attribute('contentDescription')
        exp_result = u"审批"
        self.assertEqual(exp_result, act_result)

    def test_case10(self):
        self.wk.ele_bg.click()
        self.wk.ele_bg_sptb.click()
        act_result = self.wk.ele_bg_sp_wsp.get_attribute('contentDescription')
        exp_result = u"我审批的"
        self.assertEqual(exp_result, act_result)

    def test_case11(self):
        self.wk.ele_bg.click()
        self.wk.ele_bg_sp.click()
        self.wk.ele_bg_sp_wsp.click()
        act_result = self.wk.ele_wd_dwspd.get_attribute('contentDescription')
        exp_result = u"待我审批的"
        self.assertEqual(exp_result, act_result)

    def test_case12(self):
        self.wk.ele_bg.click()
        self.wk.ele_bg_sp.click()
        self.wk.ele_bg_sp_jbsp.click()
        act_result = self.wk.ele_bg_sp_jbyy.get_attribute('contentDescription')
        exp_result = u"加班原因"
        self.assertEqual(exp_result, act_result)

    def test_case13(self):
        self.wk.ele_bg.click()
        self.wk.ele_bg_sp.click()
        self.wk.ele_bg_sp_lcbx.click()
        act_result = self.wk.ele_bg_sp_lcsy.get_attribute('contentDescription')
        exp_result = u"差旅事由"
        self.assertEqual(exp_result, act_result)

    def test_case14(self):
        self.wk.ele_bg.click()
        self.wk.ele_bg_sp.click()
        self.wk.ele_bg_sp_jksq.click()
        act_result = self.wk.ele_bg_sp_jksy.get_attribute('contentDescription')
        exp_result = u"借款事由"
        self.assertEqual(exp_result, act_result)

    def test_case15(self):
        self.wk.ele_bg.click()
        self.wk.ele_bg_sp.click()
        self.wk.ele_bg_sp_jbsp.click()
        self.wk.ele_bc.click()
        act_result = self.wk.ele_bg_sp_yyts.get_attribute('contentDescription')
        exp_result = u"加班原因不能为空！"
        self.assertEqual(exp_result, act_result)

    def test_case16(self):
        self.wk.ele_bg.click()
        self.wk.ele_bg_sp.click()
        self.wk.ele_bg_sp_jbsp.click()
        self.wk.ele_bg_sp_jbyy_input.send_keys(u"加班学习")
        # self.wk.ele_bg_sp_jbzts_input.send_keys(2)
        # self.wk.ele_bg_sp_spr.click()
        # self.wk.ele_bg_sp_spr_choose.click()
        # self.wk.ele_return.click()
        self.wk.ele_bc.click()
        act_result = self.wk.ele_bg_sp_ts.get_attribute('contentDescription')
        exp_result = u"加班总天数不能为空！"
        self.assertEqual(exp_result, act_result)

if __name__ == '__main__':
    unittest.main()

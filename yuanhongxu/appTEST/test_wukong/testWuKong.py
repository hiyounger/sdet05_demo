#coding:utf-8
import unittest
from appium import webdriver
import time
from wukong_element import WuKong

class MyTestCase(unittest.TestCase):

    def setUp(cls):
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        desired_caps["platformVersion"] = "6.0.1"
        desired_caps["deviceName"] = "816a68b87d74"
        desired_caps["appPackage"] = "com.kakarote.crm9"
        desired_caps["appActivity"] = ".MainActivity"
        # desired_caps["automationName"] = "uiautomator2"
        desired_caps["unicodeKeyboard"] = True
        desired_caps["resetKeyboard"] = True
        desired_caps["noReset"] = True
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(10)

        cls.wk=WuKong(cls.driver)

    def test_case01(self):
        self.wk.ele_db_bt.click()
        time.sleep(5)
        self.wk.ele_dshhk.click()
        self.wk.ele_dshhk_first.click()
        act_result=self.wk.ele_hkxqzt.get_attribute('contentDescription')
        exp_result=u"待审核"
        self.assertEqual(act_result, exp_result)

    def test_case02(self):
        self.wk.ele_db_bt.click()
        time.sleep(5)
        self.wk.ele_dshhk.click()
        time.sleep(1)
        self.wk.ele_dsh_xlk.click()
        self.wk.ele_ysh_xlk.click()
        time.sleep(1)
        self.wk.ele_dshhk_yjj.click()
        time.sleep(1)
        act_result=self.wk.ele_hkxqzt_shjj.get_attribute('contentDescription')
        exp_result=u"审核拒绝"
        self.assertEqual(act_result, exp_result)

    def test_case03(self):
        self.wk.ele_sj.click()
        time.sleep(1)
        self.wk.ele_xzsj.click()
        time.sleep(1)
        self.wk.ele_sjmc.send_keys(u"学习")
        self.wk.ele_khmc.click()
        self.wk.ele_choose_kh.click()
        self.wk.ele_return.click()
        time.sleep(1)
        self.wk.ele_sjzzt.click()
        self.wk.ele_choose_sjz.click()
        self.wk.ele_return.click()
        time.sleep(1)
        self.wk.ele_sjjd.click()
        self.wk.ele_choose_sjjd.click()
        self.wk.ele_return.click()
        time.sleep(1)
        self.wk.ele_sjje.send_keys(145)
        self.wk.ele_bc.click()
        time.sleep(1)
        act_result = self.wk.ele_sjnr.get_attribute('contentDescription')
        exp_result = u"学习"
        self.assertEqual(act_result, exp_result)


        # exp_result=""
        # self.assertEqual(act_result, exp_result)


if __name__ == '__main__':
    unittest.main()

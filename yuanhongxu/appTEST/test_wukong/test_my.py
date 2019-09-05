import unittest
from appium import webdriver
import time
from . import config
from APP_CRM.crm_demo import Crm

class Testcrm(unittest.TestCase):
    @classmethod
    def setUp(cls):
        desired_caps = {}
        desired_caps['platformName'] =config.platformName
        desired_caps['platformVersion'] = config.platformVersion
        desired_caps['deviceName'] = config.deviceName
        desired_caps['appPackage'] = config.appPackage
        desired_caps['appActivity'] = config.appActivity
        # desired_caps['automationName'] =config.automationName
        desired_caps['unicodeKeyboard'] = config.unicodeKeyboard
        desired_caps['resetKeyboard'] = config.resetKeyboard
        desired_caps['noReset'] = config.noReset
        start='http://%s:%s/wd/hub'%(config.ip,config.port)
        cls.driver = webdriver.Remote(start, desired_caps)
        cls.crm = Crm(cls.driver)
        time.sleep(10)

    def test_case01_my(self):
        self.crm.wode.click()
        time.sleep(3)
        act_result = self.crm.wode_result.get_attribute('contentDescription')
        exp_result = u'我的'
        self.assertEqual(exp_result, act_result)

    def test_case02_my(self):
        self.crm.wode.click()
        time.sleep(3)
        self.crm.guanliyuan.click()
        time.sleep(3)
        act_result = self.crm.guanliyuan_result.get_attribute('contentDescription')
        exp_result = u'个人信息'
        self.assertEqual(exp_result, act_result)

    def test_case03_my(self):
        self.crm.wode.click()
        time.sleep(3)
        self.crm.guanliyuan.click()
        time.sleep(3)
        self.crm.back3.click()
        time.sleep(3)
        act_result = self.crm.back3_result.get_attribute('contentDescription')
        exp_result = u'我的'
        self.assertEqual(exp_result, act_result)

    def test_case04_my(self):
        self.crm.wode.click()
        time.sleep(3)
        self.crm.tel.click()
        time.sleep(3)
        act_result = self.crm.tel_result.get_attribute('contentDescription')
        exp_result = u'公司通讯录'
        self.assertEqual(exp_result, act_result)

    def test_case05_my(self):
        self.crm.wode.click()
        time.sleep(3)
        self.crm.guanliyuan.click()
        time.sleep(3)
        self.crm.back4.click()
        time.sleep(3)
        act_result = self.crm.back3_result.get_attribute('contentDescription')
        exp_result = u'我的'
        self.assertEqual(exp_result, act_result)


if __name__ == '__main__':
    unittest.main()

import unittest
from appium import webdriver
import time
from . import config
from APP_CRM.crm_demo import Crm

class Testoa(unittest.TestCase):
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

    def test_case01_bangong(self):
        self.crm.bangong.click()
        time.sleep(3)
        act_result = self.crm.bangong_result.get_attribute('contentDescription')
        exp_result = u'办公'
        self.assertEqual(exp_result, act_result)

    def test_case02_banggong(self):
        self.crm.bangong.click()
        time.sleep(3)
        self.crm.shenpi.click()
        time.sleep(3)
        act_result = self.crm.shenpi_result.get_attribute('contentDescription')
        exp_result = u'审批'
        self.assertEqual(exp_result, act_result)

    def test_case03_putongshenpi(self):
        self.crm.bangong.click()
        time.sleep(3)
        self.crm.shenpi.click()
        time.sleep(3)
        self.crm.putongshenpi.click()
        time.sleep(5)
        act_result = self.crm.putongshenpi_result.get_attribute('contentDescription')
        exp_result = u'新建普通审批'
        self.assertEqual(exp_result, act_result)

    def test_case04_qingjiashenpi(self):
        self.crm.bangong.click()
        time.sleep(3)
        self.crm.shenpi.click()
        time.sleep(3)
        self.crm.qingjiashenpi.click()
        time.sleep(5)
        act_result = self.crm.qingjiashenpi_result.get_attribute('contentDescription')
        exp_result = u'新建请假审批'
        self.assertEqual(exp_result, act_result)

    def test_case05_chucahishenpi(self):
        self.crm.bangong.click()
        time.sleep(3)
        self.crm.shenpi.click()
        time.sleep(3)
        self.crm.chuchaishenpi.click()
        time.sleep(5)
        act_result = self.crm.chuchaishenpi_result.get_attribute('contentDescription')
        exp_result = u'新建出差审批'
        self.assertEqual(exp_result, act_result)

    def test_case06_chucahishenpi(self):
        self.crm.bangong.click()
        time.sleep(3)
        self.crm.shenpi.click()
        time.sleep(3)
        self.crm.wOfaqide.click()
        time.sleep(3)
        act_result = self.crm.wofaqide_result.get_attribute('contentDescription')
        exp_result = u'我发起的'
        self.assertEqual(exp_result, act_result)


if __name__ == '__main__':
    unittest.main()

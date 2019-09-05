import unittest
from appium import webdriver
import time
from . import config
from crm_demo import Crm

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

    def test_case01_crm(self):
        act_result = self.crm.cr_info.get_attribute("contentDescription")
        exp_result = '悟空CRM'
        self.assertEqual(exp_result, act_result)

    def test_case02_crm(self):
        self.crm.xiansuo_info.click()
        time.sleep(3)
        self.crm.xinjian_info.click()
        time.sleep(5)
        self.crm.xinjinan_input.click()
        name=self.crm.xinjinan_input.send_keys(u"2344")
        time.sleep(10)
        self.crm.save.click()
        time.sleep(1)
        act_result=self.crm.tishi.get_attribute('contentDescription')
        exp_result=u'线索名称已经存在,不能重复添加'
        self.assertEqual(exp_result, act_result)

    def test_case03_crm(self):
        self.crm.xiansuo_info.click()
        time.sleep(3)
        self.crm.xinjian_info.click()
        time.sleep(3)
        self.crm.xinjinan_input.send_keys(u"123453")
        time.sleep(5)
        self.crm.save.click()
        time.sleep(5)
        act_result=self.crm.add_success.get_attribute('contentDescription')
        exp_result=u"123453"
        self.assertEqual(exp_result, act_result)

    def test_case04_crm(self):
        self.crm.xiansuo_info.click()
        time.sleep(1)
        self.crm.de_xiansuosetp1.click()
        time.sleep(5)
        self.crm.de_xiansuostep2.click()
        time.sleep(3)
        self.crm.de_xiansuostep3.click()
        time.sleep(3)
        self.crm.de_xiansuostep4.click()
        time.sleep(5)
        act_result=self.crm.delete_success.get_attribute('contentDescription')
        exp_result=u'删除成功'
        self.assertEqual(exp_result, act_result)

    def test_case05_crm(self):
        self.crm.xiansuo_info.click()
        time.sleep(3)
        self.crm.update_step1.click()
        time.sleep(3)
        self.crm.update_step2.click()
        time.sleep(5)
        self.crm.upadte_step3.send_keys(u'13302580374')
        self.crm.save.click()
        time.sleep(5)
        act_result=self.crm.update_success.get_attribute('contentDescription')
        exp_result=u'编辑成功'
        self.assertEqual(exp_result, act_result)


if __name__ == '__main__':
    unittest.main()

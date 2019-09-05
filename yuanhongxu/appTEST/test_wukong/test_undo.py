import unittest
from appium import webdriver
import time
from . import config
from APP_CRM.crm_demo import Crm
class Testundo(unittest.TestCase):
    @classmethod
    def setUp(cls):
        desired_caps = {}
        desired_caps['platformName'] = config.platformName
        desired_caps['platformVersion'] = config.platformVersion
        desired_caps['deviceName'] = config.deviceName
        desired_caps['appPackage'] = config.appPackage
        desired_caps['appActivity'] = config.appActivity
        # desired_caps['automationName'] =config.automationName
        desired_caps['unicodeKeyboard'] = config.unicodeKeyboard
        desired_caps['resetKeyboard'] = config.resetKeyboard
        desired_caps['noReset'] = config.noReset
        start = 'http://%s:%s/wd/hub' % (config.ip, config.port)
        cls.driver = webdriver.Remote(start, desired_caps)
        cls.crm = Crm(cls.driver)
        time.sleep(10)

    def test_case01_undo(self):
        self.crm.daiban_button.click()
        time.sleep(1)
        act_result = self.crm.vertify_result.get_attribute("contentDescription")
        exp_result = u'待办事项'
        self.assertEqual(exp_result, act_result)

    def test_case02_undo(self):
        self.crm.daiban_button.click()
        time.sleep(1)
        self.crm.contact_client_button.click()
        time.sleep(3)
        act_result = self.crm.vertify_clienttitle.get_attribute('contentDescription')
        exp_result = u'今日需联系客户'
        self.assertEqual(exp_result, act_result)

    def test_case03_undo(self):
        self.crm.daiban_button.click()
        time.sleep(1)
        self.crm.contact_client_button.click()
        time.sleep(3)
        self.crm.contact_button.click()
        self.crm.outdate_button.click()
        time.sleep(10)
        act_result = self.crm.vertify_contact.get_attribute('contentDescription')
        exp_result = u'兔兔我我 管理员 最后跟进时间：2019-08-09'
        self.assertEqual(exp_result, act_result)

    def test_case04_undo(self):
        self.crm.daiban_button.click()
        time.sleep(1)
        self.crm.fenpeixians.click()
        time.sleep(3)
        act_result = self.crm.fenpeixians_result.get_attribute('contentDescription')
        exp_result = u'分配给我的线索'
        self.assertEqual(exp_result, act_result)


if __name__ == '__main__':
    unittest.main()

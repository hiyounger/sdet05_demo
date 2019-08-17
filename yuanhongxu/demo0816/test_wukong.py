#coding:utf-8
import unittest
from appium import webdriver
import time

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        desired_caps["platformVersion"] = "6.0.1"
        desired_caps["deviceName"] = "816a68b87d74"
        desired_caps["appPackage"] = "com.kakarote.crm9"
        desired_caps["appActivity"] = ".MainActivity"
        # desired_caps["automationName"] = "uiautomator2"
        desired_caps["unicodeKeyboard"] = True
        desired_caps["resetKeyboard"] = True
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(2)

    def test_login(self):
        ele_pass=self.driver.find_element_by_id("android:id/button1")
        ele_pass.click()
        time.sleep(5)
        ele_ty=self.driver.find_element_by_xpath('//android.view.View[@content-desc="立即体验"]')
        ele_ty.click()
        ele_denglu=self.driver.find_element_by_xpath('//android.webkit.WebView[@content-desc="crm_app"]/android.view.View/android.view.View/android.view.View[4]/android.view.View[1]/android.widget.EditText')
        ele_denglu.send_keys("15623219550")
        ele_password=self.driver.find_element_by_xpath('//android.webkit.WebView[@content-desc="crm_app"]/android.view.View/android.view.View/android.view.View[4]/android.view.View[2]/android.widget.EditText')
        ele_password.send_keys("yuan123")
        ele_login=self.driver.find_element_by_xpath('//android.view.View[@content-desc="登录"]')
        ele_login.click()
        # self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()

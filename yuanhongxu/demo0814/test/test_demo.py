# coding:utf-8
import unittest
from appium import webdriver
import time

from calculator import calculator_bt


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        desired_caps["platformVersion"] = "6.0.1"
        desired_caps["deviceName"] = "816a68b87d74"
        desired_caps["appPackage"] = "com.miui.calculator"
        desired_caps["appActivity"] = ".cal.CalculatorActivity"
        desired_caps["automationName"] = "uiautomator2"
        desired_caps["unicodeKeyboard"] = True
        desired_caps["resetKeyboard"] = True
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(2)

        cls.calc=calculator_bt(cls.driver)

    def tearDown(self):
        # ele = self.driver.find_element_by_id("com.miui.calculator:id/btn_c_s")
        # ele.click()
        self.calc.bt_c.click()

    def test_case01(self):
        # ele1 = self.driver.find_element_by_id("com.miui.calculator:id/btn_2_s")
        # ele2 = self.driver.find_element_by_id("com.miui.calculator:id/btn_plus_s")
        # ele3 = self.driver.find_element_by_id("com.miui.calculator:id/btn_3_s")
        # ele4 = self.driver.find_element_by_id("com.miui.calculator:id/btn_equal_s")
        #
        # ele1.click()
        # ele3.click()
        # ele3.click()
        # ele1.click()
        # ele2.click()
        # ele3.click()
        # ele1.click()
        # ele1.click()
        # ele4.click()
        # time.sleep(15)
        # ele5 = self.driver.find_element_by_xpath(
        #     "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/miui.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.HorizontalScrollView[3]/android.widget.LinearLayout/android.widget.TextView[2]")
        # act_result = ele5.text
        # exp_result=u"2,654"
        # self.assertEqual(act_result, exp_result)
        self.calc.bt1.click()
        self.calc.bt2.click()
        self.calc.bt3.click()
        self.calc.bt4.click()
        self.calc.bt_plus.click()
        self.calc.bt5.click()
        self.calc.bt6.click()
        self.calc.bt7.click()
        self.calc.bt8.click()
        self.calc.bt_equal.click()
        time.sleep(12)
        act_result = self.calc.bt_result.text
        exp_result = u"6,912"
        self.assertEqual(act_result, exp_result)

    def test_case02(self):
        # ele1 = self.driver.find_element_by_id("com.miui.calculator:id/btn_2_s")
        # ele2 = self.driver.find_element_by_id("com.miui.calculator:id/btn_minus_s")
        # ele3 = self.driver.find_element_by_id("com.miui.calculator:id/btn_3_s")
        # ele4 = self.driver.find_element_by_id("com.miui.calculator:id/btn_equal_s")
        #
        # ele1.click()
        # ele3.click()
        # ele3.click()
        # ele1.click()
        # ele2.click()
        # ele3.click()
        # ele1.click()
        # ele1.click()
        # ele4.click()
        # ele5 = self.driver.find_element_by_xpath(
        #     "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/miui.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.HorizontalScrollView[3]/android.widget.LinearLayout/android.widget.TextView[2]")
        # act_result = ele5.text
        # exp_result = u"2,010"
        # self.assertEqual(act_result, exp_result)


        self.calc.bt5.click()
        self.calc.bt6.click()
        self.calc.bt7.click()
        self.calc.bt8.click()
        self.calc.bt_minus.click()
        self.calc.bt1.click()
        self.calc.bt2.click()
        self.calc.bt3.click()
        self.calc.bt4.click()
        self.calc.bt_equal.click()
        act_result = self.calc.bt_result.text
        exp_result = u"4,444"
        self.assertEqual(act_result, exp_result)

    def test_case03(self):
        # ele1 = self.driver.find_element_by_id("com.miui.calculator:id/btn_2_s")
        # ele2 = self.driver.find_element_by_id("com.miui.calculator:id/btn_mul_s")
        # ele3 = self.driver.find_element_by_id("com.miui.calculator:id/btn_3_s")
        # ele4 = self.driver.find_element_by_id("com.miui.calculator:id/btn_equal_s")
        #
        # ele1.click()
        # ele1.click()
        # ele3.click()
        # ele1.click()
        # ele2.click()
        # ele3.click()
        # ele1.click()
        # ele1.click()
        # ele4.click()
        # ele5 = self.driver.find_element_by_xpath(
        #     "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/miui.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.HorizontalScrollView[3]/android.widget.LinearLayout/android.widget.TextView[2]")
        # act_result = ele5.text
        # exp_result = u"718,704"
        # self.assertEqual(act_result, exp_result)
        self.calc.bt5.click()
        self.calc.bt6.click()
        self.calc.bt7.click()
        self.calc.bt8.click()
        self.calc.bt_mul.click()
        self.calc.bt1.click()
        self.calc.bt2.click()
        self.calc.bt3.click()
        self.calc.bt4.click()
        self.calc.bt_equal.click()
        act_result = self.calc.bt_result.text
        exp_result = u"7,006,652"
        self.assertEqual(act_result, exp_result)

    def test_case04(self):
        # ele1 = self.driver.find_element_by_id("com.miui.calculator:id/btn_2_s")
        # ele2 = self.driver.find_element_by_id("com.miui.calculator:id/btn_div_s")
        # ele3 = self.driver.find_element_by_id("com.miui.calculator:id/btn_3_s")
        # ele4 = self.driver.find_element_by_id("com.miui.calculator:id/btn_equal_s")
        #
        # ele1.click()
        # ele3.click()
        # ele3.click()
        # ele1.click()
        # ele2.click()
        # ele1.click()
        # ele4.click()
        # ele5 = self.driver.find_element_by_xpath(
        #     "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/miui.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.HorizontalScrollView[3]/android.widget.LinearLayout/android.widget.TextView[2]")
        # act_result = ele5.text
        # exp_result = u"1,166"
        # self.assertEqual(act_result, exp_result)

        self.calc.bt5.click()
        self.calc.bt6.click()
        self.calc.bt7.click()
        self.calc.bt8.click()
        self.calc.bt_div.click()
        self.calc.bt3.click()
        self.calc.bt_equal.click()
        act_result = self.calc.bt_result.text
        exp_result = u"1,892.66667"
        self.assertEqual(act_result, exp_result)


if __name__ == '__main__':
    unittest.main()

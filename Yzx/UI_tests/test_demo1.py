#encoding:utf-8
import unittest
from selenium import  webdriver
import json


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
    def setUp(self):
        url = "http://47.92.220.226/webdriver/location.html"
        self.driver.get(url)

    def test_something(self):
        # 定位
        input_name = self.driver.find_element_by_id(u'username')
        input_email = self.driver.find_element_by_name(u'email')
        input_password = self.driver.find_element_by_id(u'password')
        input_twopwd = self.driver.find_element_by_css_selector(u'#confirm_password')
        denglu = self.driver.find_element_by_xpath(u'//td[@colspan]/input[1]')
        # 赋值
        input_name.send_keys(u'yanzhenxing')
        input_email.send_keys(u'1234@qq.com')
        input_password.send_keys(u'1233')
        input_twopwd.send_keys(u'1233')
        # 点击
        denglu.click()
        # 获得返回值
        ele_regmsg = self.driver.find_element_by_id(u"regmsg")
        regmsg_text = ele_regmsg.text
        regmsg_json = json.loads(regmsg_text.split(u"成功:")[-1], encoding='utf-8')
        print  regmsg_json



if __name__ == '__main__':
    unittest.main()

# encoding:utf-8
import unittest
from selenium import webdriver
import json
from config import LOCATION_PAGE_URL


class TestHomework01(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get(LOCATION_PAGE_URL)

    def test_case01_registerSuccess(self):
        # 定位
        input_name = self.driver.find_element_by_id(u'username')
        input_email = self.driver.find_element_by_name(u'email')
        input_password = self.driver.find_element_by_id(u'password')
        input_twopwd = self.driver.find_element_by_css_selector(u'#confirm_password')
        denglu = self.driver.find_element_by_xpath(u'//td[@colspan]/input[1]')
        # 赋值{u'username': u'yanzhenxing', u'password': u'1233', u'uid': 0, u'email': u'1234@qq.com'}
        data = {
            'username': u'yanzhenxing',
            'email': u'1234@qq.com',
            'password': u'1233',
        }
        input_name.send_keys(data['username'])
        input_email.send_keys(data['email'])
        input_password.send_keys(data['password'])
        input_twopwd.send_keys(data['password'])
        # 点击
        denglu.click()
        # 获得返回值
        ele_regmsg = self.driver.find_element_by_id(u"regmsg")
        regmsg_text = ele_regmsg.text
        regmsg_json = json.loads(regmsg_text.split(u"成功:")[-1], encoding='utf-8')
        self.assertDictContainsSubset(data, regmsg_json)

    def test_case02_registerPasswordNotEqual(self):
        # 定位
        input_name = self.driver.find_element_by_id(u'username')
        input_email = self.driver.find_element_by_name(u'email')
        input_password = self.driver.find_element_by_id(u'password')
        input_twopwd = self.driver.find_element_by_css_selector(u'#confirm_password')
        denglu = self.driver.find_element_by_xpath(u'//td[@colspan]/input[1]')
        # 赋值{u'username': u'yanzhenxing', u'password': u'1233', u'uid': 0, u'email': u'1234@qq.com'}
        data = {
            'username': u'yanzhenxing',
            'email': u'1234@qq.com',
            'password': u'1233',
        }
        input_name.send_keys(data['username'])
        input_email.send_keys(data['email'])
        input_password.send_keys(data['password'])
        input_twopwd.send_keys(u'12')
        # 点击
        denglu.click()
        # 获得返回值
        ele_regmsg = self.driver.find_element_by_id(u"regmsg")
        regmsg_text = ele_regmsg.text
        self.assertEqual(u'两次输入的密码不一致', regmsg_text)


if __name__ == '__main__':
    unittest.main()

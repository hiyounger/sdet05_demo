# encoding:utf-8
import unittest
from selenium import webdriver
from config import LOCATION_PAGE_URL
from utils.loginpage import LoginPageUtils
import json


class TestSearchUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get(LOCATION_PAGE_URL)
        LoginPageUtils.register(self.driver)

    def test_case01(self):
        # 获得期望值
        ele_regmsg = self.driver.find_element_by_id(u"regmsg")
        regmsg_text = ele_regmsg.text
        regmsg_json = json.loads(regmsg_text.split(u"成功:")[-1], encoding='utf-8')
        elems = self.driver.find_element_by_id(u'search_uid')
        elems.send_keys(regmsg_json[u'uid'])
        ele_search_id = self.driver.find_element_by_xpath(u'/html/body/div[2]/div[1]/input[2]')
        ele_search_id.click()
        seacher = self.driver.find_element_by_id(u'search_msg')
        seacher_text_uid = seacher.text
        ret_json = json.loads(seacher_text_uid)
        self.assertDictEqual(regmsg_json, ret_json)

    def test_case02(self):
        # 获得期望值
        ele_regmsg = self.driver.find_element_by_id(u"regmsg")
        regmsg_text = ele_regmsg.text
        regmsg_json = json.loads(regmsg_text.split(u"成功:")[-1], encoding='utf-8')

        elems = self.driver.find_element_by_id(u'search_uname')
        elems.send_keys(regmsg_json[u'username'])
        ele_search_name = self.driver.find_element_by_xpath(u'/html/body/div[2]/div[2]/input[2]')
        ele_search_name.click()
        seacher_name = self.driver.find_element_by_id(u'search_msg')
        seacher_name_text = seacher_name.text
        seacher_text_name_json = json.loads(seacher_name_text)
        self.assertEqual(regmsg_json, seacher_text_name_json)

    def test_case03(self):
        # 获得期望值
        ele_regmsg = self.driver.find_element_by_id(u"regmsg")
        regmsg_text = ele_regmsg.text
        regmsg_json = json.loads(regmsg_text.split(u"成功:")[-1], encoding='utf-8')

        elems = self.driver.find_element_by_id(u'search_email')
        elems.send_keys(regmsg_json[u'email'])
        ele_search_email = self.driver.find_element_by_xpath(u'/html/body/div[2]/div[3]/input[2]')
        ele_search_email.click()
        seacher_text_email = self.driver.find_element_by_id(u'search_msg')
        seacher_text_email_text = seacher_text_email.text
        seacher_text_email_text_json = json.loads(seacher_text_email_text)
        self.assertEqual(regmsg_json, seacher_text_email_text_json)


if __name__ == '__main__':
    unittest.main()

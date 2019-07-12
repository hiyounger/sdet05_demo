# -*- encoding:utf-8 -*-

import unittest
from selenium import webdriver
import json
from webdrive_demo.location_page import locationPage


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    def setUp(self):
        self.locationPage = locationPage(self.driver)
        self.locationPage.open()

    def test_case01(self):
        register_data = {
            "username": "yuan",
            "email": "yuan@qq.com",
            "password": "yuan",
            "cpassword": "yuan"
        }
        self.locationPage.register(register_data)
        return_msg = json.loads(self.locationPage.ele_regmsg.text.split(u"成功:")[-1])
        exp_result = {u"username": u"yuan", u"password": u"yuan", u"email": u"yuan@qq.com"}
        file_list = []
        for key in exp_result.keys():
            try:
                if exp_result[key] != return_msg[key]:
                    file_list.append(key)
            except:
                file_list.append(key)

        self.assertEqual(0, len(file_list))

    def test_case02(self):
        register_data = {
            "username": "yuan",
            "email": "yuan@qq.com",
            "password": "yuan",
            "cpassword": "yua"
        }
        self.locationPage.register(register_data)
        act_result = self.locationPage.ele_regmsg.text
        exp_result = u"两次输入的密码不一致"

        self.assertEqual(act_result, exp_result)

    def test_case03(self):
        register_data = {
            "username": "yuan",
            "email": "yuan@qq.com",
            "password": "yuan",
            "cpassword": "yuan"
        }
        self.locationPage.register(register_data)

        ele_search_uid = self.driver.find_element_by_id(u"search_uid")
        ele_search_uid.send_keys(0)
        ele_search = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/input[2]")
        ele_search.click()
        ele_search_msg = self.driver.find_element_by_id(u"search_msg")
        act_result = json.loads(ele_search_msg.text)
        exp_result = {"uid": 0, "username": "yuan", "password": "yuan", "email": "yuan@qq.com"}

        self.assertEqual(act_result, exp_result)

    def test_case04(self):
        register_data = {
            "username": "yuan",
            "email": "yuan@qq.com",
            "password": "yuan",
            "cpassword": "yuan"
        }
        self.locationPage.register(register_data)

        ele_search_uname = self.driver.find_element_by_id(u"search_uname")
        ele_search_uname.send_keys(u"yuan")
        ele_search1 = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/input[2]")
        ele_search1.click()
        ele_search_msg = self.driver.find_element_by_id(u"search_msg")
        act_result = json.loads(ele_search_msg.text)
        exp_result = {"uid": 0, "username": "yuan", "password": "yuan", "email": "yuan@qq.com"}

        self.assertEqual(act_result, exp_result)

    def test_case05(self):
        register_data = {
            "username": "yuan",
            "email": "yuan@qq.com",
            "password": "yuan",
            "cpassword": "yuan"
        }
        self.locationPage.register(register_data)

        ele_search_email = self.driver.find_element_by_id(u"search_email")
        ele_search_email.send_keys(u"yuan@qq.com")
        ele_search2 = self.driver.find_element_by_xpath("/html/body/div[2]/div[3]/input[2]")
        ele_search2.click()
        ele_search_msg = self.driver.find_element_by_id(u"search_msg")
        act_result = json.loads(ele_search_msg.text)
        exp_result = {"uid": 0, "username": "yuan", "password": "yuan", "email": "yuan@qq.com"}

        self.assertEqual(act_result, exp_result)


if __name__ == '__main__':
    unittest.main()

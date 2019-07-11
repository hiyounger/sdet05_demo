# -*- encoding:utf-8 -*-

import unittest
from selenium import webdriver
import json


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    def setUp(self):
        url = "http://47.92.220.226/webdriver/location.html"
        self.driver.get(url)

    def test_case01(self):
        ele_username = self.driver.find_element_by_id("username")
        ele_email = self.driver.find_element_by_id("email")
        ele_password = self.driver.find_element_by_id("password")
        ele_confirm_password = self.driver.find_element_by_id("confirm_password")
        ele_submit = self.driver.find_element_by_xpath("//tbody/tr[5]/td/input[1]")
        ele_regmsg = self.driver.find_element_by_id("regmsg")

        __username = "yuan"
        __email = "yuan@qq.com"
        __password = "yuan"
        __cpassword = "yuan"

        ele_username.send_keys(__username)
        ele_email.send_keys(__email)
        ele_password.send_keys(__password)
        ele_confirm_password.send_keys(__cpassword)
        ele_submit.click()
        return_msg = json.loads(ele_regmsg.text.split(u"成功:")[-1])
        print return_msg
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
        ele_username = self.driver.find_element_by_id("username")
        ele_email = self.driver.find_element_by_id("email")
        ele_password = self.driver.find_element_by_id("password")
        ele_confirm_password = self.driver.find_element_by_id("confirm_password")
        ele_submit = self.driver.find_element_by_xpath("//tbody/tr[5]/td/input[1]")
        ele_regmsg = self.driver.find_element_by_id("regmsg")

        __username = "yuan"
        __email = "yuan@qq.com"
        __password = "yuan"
        __cpassword = "yua"

        ele_username.send_keys(__username)
        ele_email.send_keys(__email)
        ele_password.send_keys(__password)
        ele_confirm_password.send_keys(__cpassword)
        ele_submit.click()
        act_result = ele_regmsg.text
        exp_result = u"两次输入的密码不一致"

        self.assertEqual(act_result, exp_result)

    def test_case03(self):
        ele_username = self.driver.find_element_by_id("username")
        ele_email = self.driver.find_element_by_id("email")
        ele_password = self.driver.find_element_by_id("password")
        ele_confirm_password = self.driver.find_element_by_id("confirm_password")
        ele_submit = self.driver.find_element_by_xpath("//tbody/tr[5]/td/input[1]")

        __username = "yuan"
        __email = "yuan@qq.com"
        __password = "yuan"
        __cpassword = "yuan"

        ele_username.send_keys(__username)
        ele_email.send_keys(__email)
        ele_password.send_keys(__password)
        ele_confirm_password.send_keys(__cpassword)
        ele_submit.click()

        ele_search_uid = self.driver.find_element_by_id(u"search_uid")
        ele_search_uid.send_keys(0)
        ele_search = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/input[2]")
        ele_search.click()
        ele_search_msg = self.driver.find_element_by_id(u"search_msg")
        act_result = json.loads(ele_search_msg.text)
        exp_result = {"uid": 0, "username": "yuan", "password": "yuan", "email": "yuan@qq.com"}

        self.assertEqual(act_result, exp_result)

    def test_case04(self):
        ele_username = self.driver.find_element_by_id("username")
        ele_email = self.driver.find_element_by_id("email")
        ele_password = self.driver.find_element_by_id("password")
        ele_confirm_password = self.driver.find_element_by_id("confirm_password")
        ele_submit = self.driver.find_element_by_xpath("//tbody/tr[5]/td/input[1]")

        __username = "yuan"
        __email = "yuan@qq.com"
        __password = "yuan"
        __cpassword = "yuan"

        ele_username.send_keys(__username)
        ele_email.send_keys(__email)
        ele_password.send_keys(__password)
        ele_confirm_password.send_keys(__cpassword)
        ele_submit.click()

        ele_search_uname = self.driver.find_element_by_id(u"search_uname")
        ele_search_uname.send_keys(u"yuan")
        ele_search1 = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/input[2]")
        ele_search1.click()
        ele_search_msg = self.driver.find_element_by_id(u"search_msg")
        act_result = json.loads(ele_search_msg.text)
        exp_result = {"uid": 0, "username": "yuan", "password": "yuan", "email": "yuan@qq.com"}

        self.assertEqual(act_result, exp_result)

    def test_case05(self):
        ele_username = self.driver.find_element_by_id("username")
        ele_email = self.driver.find_element_by_id("email")
        ele_password = self.driver.find_element_by_id("password")
        ele_confirm_password = self.driver.find_element_by_id("confirm_password")
        ele_submit = self.driver.find_element_by_xpath("//tbody/tr[5]/td/input[1]")

        __username = "yuan"
        __email = "yuan@qq.com"
        __password = "yuan"
        __cpassword = "yuan"

        ele_username.send_keys(__username)
        ele_email.send_keys(__email)
        ele_password.send_keys(__password)
        ele_confirm_password.send_keys(__cpassword)
        ele_submit.click()

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

# encoding:utf-8

import unittest
from selenium import webdriver
import json

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    def setUp(self):
        url = "http://47.92.220.226:8000/webdriver/location.html"
        self.driver.get(url)

    def test_regiser01(self):
        ele_username = self.driver.find_element_by_id(u"username")
        ele_email = self.driver.find_element_by_id(u"email")
        ele_password = self.driver.find_element_by_id(u"password")
        ele_cpassword = self.driver.find_element_by_id(u"confirm_password")
        ele_regbt = self.driver.find_element_by_xpath("//tbody/tr[5]/td/input[1]")
        ele_regmsg = self.driver.find_element_by_id(u"regmsg")

        __username = u"chenguanxi"
        __email = u"1286060621@qq.com"
        __password = u"123456"
        __cpassword = u"123456"

        ele_username.send_keys(__username)
        ele_email.send_keys(__email)
        ele_password.send_keys(__password)
        ele_cpassword.send_keys(__cpassword)
        ele_regbt.click()
        ret_dic = json.loads(ele_regmsg.text.split(u"成功:")[-1],encoding="utf-8")


        exp_result = {u'username': u'chenguanxi', u'password': u'123456', u'uid': 0, u'email': u'1286060621@qq.com'}
        act_result = ret_dic
        self.assertEqual(act_result,exp_result)
    def test_regiser02(self):
        ele_username = self.driver.find_element_by_id(u"username")
        ele_email = self.driver.find_element_by_id(u"email")
        ele_password = self.driver.find_element_by_id(u"password")
        ele_cpassword = self.driver.find_element_by_id(u"confirm_password")
        ele_regbt = self.driver.find_element_by_xpath("//tbody/tr[5]/td/input[1]")
        ele_regmsg = self.driver.find_element_by_id(u"regmsg")

        __username = u"chenguanxi"
        __email = u"1286060621@qq.com"
        __password = u"123455"
        __cpassword = u"123456"

        ele_username.send_keys(__username)
        ele_email.send_keys(__email)
        ele_password.send_keys(__password)
        ele_cpassword.send_keys(__cpassword)
        ele_regbt.click()
        ret_dic = ele_regmsg
        exp_result = u"两次输入的密码不一致"
        act_result = ret_dic.text
        self.assertEqual(act_result, exp_result)


    def test_regiser03(self):
        ele_username = self.driver.find_element_by_id(u"username")
        ele_email = self.driver.find_element_by_id(u"email")
        ele_password = self.driver.find_element_by_id(u"password")
        ele_cpassword = self.driver.find_element_by_id(u"confirm_password")
        ele_regbt = self.driver.find_element_by_xpath("//tbody/tr[5]/td/input[1]")

        __username = u"chenguanxi"
        __email = u"1286060621@qq.com"
        __password = u"123456"
        __cpassword = u"123456"

        ele_username.send_keys(__username)
        ele_email.send_keys(__email)
        ele_password.send_keys(__password)
        ele_cpassword.send_keys(__cpassword)
        ele_regbt.click()
        self.driver.find_element_by_id(u"search_uid").send_keys("0")
        ele_select = self.driver.find_element_by_xpath('//body/div[2]/div[1]/input[2]')
        ele_select.click()
        ele_msg = self.driver.find_element_by_id(u'search_msg')
        act_result=json.loads(ele_msg.text)
        exp_result = {"uid":0,"username":"chenguanxi","password":"123456","email":"1286060621@qq.com"}
        self.assertEqual(exp_result,act_result)

    def test_regiser04(self):
        ele_username = self.driver.find_element_by_id(u"username")
        ele_email = self.driver.find_element_by_id(u"email")
        ele_password = self.driver.find_element_by_id(u"password")
        ele_cpassword = self.driver.find_element_by_id(u"confirm_password")
        ele_regbt = self.driver.find_element_by_xpath("//tbody/tr[5]/td/input[1]")

        __username = u"chenguanxi"
        __email = u"1286060621@qq.com"
        __password = u"123456"
        __cpassword = u"123456"

        ele_username.send_keys(__username)
        ele_email.send_keys(__email)
        ele_password.send_keys(__password)
        ele_cpassword.send_keys(__cpassword)
        ele_regbt.click()
        self.driver.find_element_by_id(u"search_uname").send_keys("chenguanxi")
        ele_select = self.driver.find_element_by_xpath('//body/div[2]/div[2]/input[2]')
        ele_select.click()
        ele_msg = self.driver.find_element_by_id(u'search_msg')
        act_result=json.loads(ele_msg.text)
        exp_result = {"uid":0,"username":"chenguanxi","password":"123456","email":"1286060621@qq.com"}
        self.assertEqual(exp_result,act_result)

    def test_regiser05(self):
        ele_username = self.driver.find_element_by_id(u"username")
        ele_email = self.driver.find_element_by_id(u"email")
        ele_password = self.driver.find_element_by_id(u"password")
        ele_cpassword = self.driver.find_element_by_id(u"confirm_password")
        ele_regbt = self.driver.find_element_by_xpath("//tbody/tr[5]/td/input[1]")

        __username = u"chenguanxi"
        __email = u"1286060621@qq.com"
        __password = u"123456"
        __cpassword = u"123456"

        ele_username.send_keys(__username)
        ele_email.send_keys(__email)
        ele_password.send_keys(__password)
        ele_cpassword.send_keys(__cpassword)
        ele_regbt.click()
        self.driver.find_element_by_id(u"search_email").send_keys("1286060621@qq.com")
        ele_select = self.driver.find_element_by_xpath('//body/div[2]/div[3]/input[2]')
        ele_select.click()
        ele_msg = self.driver.find_element_by_id(u'search_msg')
        act_result = json.loads(ele_msg.text)
        exp_result = {"uid": 0, "username": "chenguanxi", "password": "123456", "email": "1286060621@qq.com"}
        self.assertEqual(exp_result, act_result)


if __name__ == '__main__':
    unittest.main()

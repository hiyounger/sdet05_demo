# encoding:utf-8
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

    def test_register(self):
        ele_username = self.driver.find_element_by_id(u"username")
        ele_email  = self.driver.find_element_by_id(u"email")
        ele_password = self.driver.find_element_by_id(u"password")
        ele_cpassword = self.driver.find_element_by_id(u"confirm_password")
        ele_regbt = self.driver.find_element_by_xpath(u"//tbody/tr[5]/td/input[1]")
        ele_regmsg = self.driver.find_element_by_id(u"regmsg")

        __username = u"chenyao"
        __email  =   u"947072026@qq.com"
        __password = u"123456"
        __cpassword= u"1234567"

        exp_user_data = {u'username': u'chenyao', u'password': u'123456', u'email': u'947072026@qq.com'}

        ele_username.send_keys(exp_user_data[u"username"])
        ele_email.send_keys(exp_user_data[u"email"])
        ele_password.send_keys(exp_user_data[u"password"])
        ele_cpassword.send_keys(__cpassword)
        ele_regbt.click()

        act_msg_dic = json.loads(ele_regmsg.text.split(u"成功:")[-1],encoding="utf-8")
        print(act_msg_dic)
        self.assertDictContainsSubset(exp_user_data,act_msg_dic)



if __name__ == '__main__':
    unittest.main()
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

        ele_sch = self.driver.find_element_by_id(u"search_uid")
        ele_schmsg = self.driver.find_element_by_xpath(u"//div[2]/div[1]/input[2]")
        ele_retmsg = self.driver.find_element_by_id(u"search_msg")

        __username = u"chenyao"
        __email  =   u"947072026@qq.com"
        __password = u"123456"
        __cpassword= u"123456"
        __sch =u"0"

        exp_user_data = {u'username': u'chenyao', u'password': u'123456', u'email': u'947072026@qq.com'}

        ele_username.send_keys(exp_user_data[u"username"])
        ele_email.send_keys(exp_user_data[u"email"])
        ele_password.send_keys(exp_user_data[u"password"])
        ele_cpassword.send_keys(exp_user_data[u"password"])
        ele_sch.send_keys(__sch)

        ele_regbt.click()
        ele_schmsg.click()


        act_msg_dic = json.loads(ele_regmsg.text.split(u"成功:")[-1],encoding="utf-8")
        act_ret_dic = json.loads(ele_retmsg.text,encoding='utf-8')
        print(act_msg_dic)
        self.assertDictContainsSubset(act_msg_dic,act_ret_dic)



if __name__ == '__main__':
    unittest.main()
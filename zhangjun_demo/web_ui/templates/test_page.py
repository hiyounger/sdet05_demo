#encoding:utf-8
import unittest
import json
from selenium import webdriver
import time


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()

    def setUp(self):
        self.driver.get("http://47.92.220.226/webdriver/location.html")

    def test_resiger_case01(self):
        username=self.driver.find_element_by_id(u"username")
        email=self.driver.find_element_by_id(u"email")
        password=self.driver.find_element_by_id(u"password")
        confirm=self.driver.find_element_by_id(u"confirm_password")
        register=self.driver.find_element_by_xpath(u"//tbody/tr[5]/td/input[1]")
        regmsg=self.driver.find_element_by_id(u"regmsg")

        exp={u'username': u'zhangjun', u'password': u'123456',u'email': u'487296792@qq.com'}
        username.send_keys(exp[u'username'])
        email.send_keys(exp[u'email'])
        password.send_keys(exp[u'password'])
        confirm.send_keys(exp[u'password'])

        register.click()

        regmsg_text = regmsg.text

        regmsg_json=json.loads(regmsg_text.split(u'成功:')[-1],encoding='utf-8')
        act_ret_dic=regmsg_json
        print regmsg_json
        self.assertDictContainsSubset(exp,act_ret_dic)

    def test_resiger_case02(self):
        username = self.driver.find_element_by_id(u"username")
        email = self.driver.find_element_by_id(u"email")
        password = self.driver.find_element_by_id(u"password")
        confirm = self.driver.find_element_by_id(u"confirm_password")
        register = self.driver.find_element_by_xpath(u"//tbody/tr[5]/td/input[1]")
        regmsg = self.driver.find_element_by_id(u"regmsg")

        exp = {u'username': u'zhangjun', u'password': u'123456', u'email': u'487296792@qq.com',u'confirm_password': u'12345678'}
        username.send_keys(exp[u'username'])
        email.send_keys(exp[u'email'])
        password.send_keys(exp[u'password'])
        confirm.send_keys(exp[u'confirm_password'])
        exp_ret=u"两次输入的密码不一致"


        register.click()

        act_ret = regmsg.text
        self.assertEqual(exp_ret,act_ret)


    # #根据id查询
    def test_serch_case03(self):
        username = self.driver.find_element_by_id(u"username")
        email = self.driver.find_element_by_id(u"email")
        password = self.driver.find_element_by_id(u"password")
        confirm = self.driver.find_element_by_id(u"confirm_password")
        register = self.driver.find_element_by_xpath(u"//tbody/tr[5]/td/input[1]")

        exp = {u'username': u'zhangjun', u'password': u'123456', u'email': u'487296792@qq.com'}
        username.send_keys(exp[u'username'])
        email.send_keys(exp[u'email'])
        password.send_keys(exp[u'password'])
        confirm.send_keys(exp[u'password'])
        register.click()
        serch=self.driver.find_element_by_xpath(u'//*[@id="search_uid"]')
        serch.send_keys(u"0")
        serch_bt=self.driver.find_element_by_xpath(u"//div[2]/div[1]/input[2]")
        serch_bt.click()
        search_msg=self.driver.find_element_by_id(u'search_msg')
        search_msg_text=search_msg.text
        search_msg_json=json.loads(search_msg_text,encoding='utf-8')

        exp_ret={u'username': u'zhangjun', u'password': u'123456',u'uid': 0, u'email': u'487296792@qq.com'}
        act_ret=search_msg_json
        self.assertEqual(exp_ret,act_ret)

    def test_serch_case04(self):
        #根据用户名查询
        username = self.driver.find_element_by_id(u"username")
        email = self.driver.find_element_by_id(u"email")
        password = self.driver.find_element_by_id(u"password")
        confirm = self.driver.find_element_by_id(u"confirm_password")
        register = self.driver.find_element_by_xpath(u"//tbody/tr[5]/td/input[1]")

        exp = {u'username': u'zhangjun', u'password': u'123456', u'email': u'487296792@qq.com'}
        username.send_keys(exp[u'username'])
        email.send_keys(exp[u'email'])
        password.send_keys(exp[u'password'])
        confirm.send_keys(exp[u'password'])
        register.click()

        serch=self.driver.find_element_by_xpath(u'//*[@id="search_uname"]')
        serch.send_keys(u"zhangjun")
        serch_bt1=self.driver.find_element_by_xpath(u"//div[2]/div[2]/input[2]")
        serch_bt1.click()
        search_msg=self.driver.find_element_by_id(u'search_msg')
        search_msg_text=search_msg.text
        search_msg_json=json.loads(search_msg_text,encoding='utf-8')

        exp_ret = {u'username': u'zhangjun', u'password': u'123456', u'uid': 0, u'email': u'487296792@qq.com'}
        act_ret = search_msg_json
        self.assertEqual(exp_ret, act_ret)

    #
    def test_serch_case05(self):
    #     #根据邮箱查询
        username = self.driver.find_element_by_id(u"username")
        email = self.driver.find_element_by_id(u"email")
        password = self.driver.find_element_by_id(u"password")
        confirm = self.driver.find_element_by_id(u"confirm_password")
        register = self.driver.find_element_by_xpath(u"//tbody/tr[5]/td/input[1]")

        exp = {u'username': u'zhangjun', u'password': u'123456', u'email': u'487296792@qq.com'}
        username.send_keys(exp[u'username'])
        email.send_keys(exp[u'email'])
        password.send_keys(exp[u'password'])
        confirm.send_keys(exp[u'password'])
        register.click()


        serch=self.driver.find_element_by_xpath(u'//*[@id="search_email"]')
        serch.send_keys(u"487296792@qq.com")
        serch_bt2=self.driver.find_element_by_xpath(u"//div[2]/div[3]/input[2]")
        serch_bt2.click()
        search_msg=self.driver.find_element_by_id(u'search_msg')
        search_msg_text=search_msg.text
        search_msg_json=json.loads(search_msg_text,encoding='utf-8')

        exp_ret = {u'username': u'zhangjun', u'password': u'123456', u'uid': 0, u'email': u'487296792@qq.com'}
        act_ret = search_msg_json
        self.assertEqual(exp_ret, act_ret)



if __name__ == '__main__':
    unittest.main()

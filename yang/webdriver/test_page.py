#encoding:utf-8

import unittest
from selenium import webdriver
import json



class myCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    def setUp(self):
        url = "http://47.92.220.226/webdriver/location.html"
        self.driver.get(url)

    def test_regiser(self):
        ele_username = self.driver.find_element_by_id(u"username")
        ele_email = self.driver.find_element_by_id(u"email")
        ele_password = self.driver.find_element_by_id(u"password")
        ele_cpassword = self.driver.find_element_by_id(u"confirm_password")
        ele_regbt = self.driver.find_element_by_xpath(u"//tbody/tr[5]/td/input[1]")
        ele_regmsg = self.driver.find_element_by_id(u"regmsg")

        __username = u"yangjun"
        __email = u"yang@qq.com"
        __password = u"123"
        __cpassword = u"123"

        ele_username.send_keys(__username)
        ele_email.send_keys(__email)
        ele_password.send_keys(__password)
        ele_cpassword.send_keys(__cpassword)
        ele_regbt.click()
        regmsg_text = ele_regmsg.text

        act_msg_dic = json.loads(regmsg_text.split(u"成功:")[-1],encoding="utf-8")
        print(act_msg_dic)
        # act = act_msg_dic
        # exp = {u'username': u'yangjun', u'password': u'123', u'uid': 0, u'email': u'yang@qq.com'}
        #
        #
        # self.assertDictContainsSubset(exp,act)

        #两次输入的密码不一致
        # print(regmsg_text)
        # act =  regmsg_text
        # exp = u"两次输入的密码不一致"
        # self.assertEqual(exp,act)

    # def test_case03(self):

        instert_spon = self.driver.find_element_by_id("search_uid")
        instert_but = self.driver.find_element_by_xpath("//div[1]/input[2]")
        # ele_search_regmsg = self.driver.find_element_by_id("search_msg")

        __spon = u"0"

        instert_spon.send_keys(__spon)
        instert_but.click()
        # search_regmsg_text = ele_search_regmsg.text
        # print (search_regmsg_text)



        instert_username1 = self.driver.find_element_by_id("search_uname")
        instert_butt = self.driver.find_element_by_xpath("//div[2]/input[2]")
        # ele_search_regmsg = self.driver.find_element_by_id("search_msg")

        username = u"yangjun"

        instert_username1.send_keys(username)
        instert_butt.click()
        # search_regmsg_text = ele_search_regmsg.text
        # print (search_regmsg_text)



        instert_email = self.driver.find_element_by_id("search_email")
        instert_butte = self.driver.find_element_by_xpath("//div[3]/input[2]")
        ele_search_regmsg = self.driver.find_element_by_id("search_msg")

        email = u"yang@qq.com"

        instert_email.send_keys(email)
        instert_butte.click()
        search_regmsg_text = ele_search_regmsg.text

        print (search_regmsg_text)





if __name__ == '__main__':
    unittest.main()

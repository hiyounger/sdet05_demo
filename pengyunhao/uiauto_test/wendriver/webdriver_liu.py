#encoding:utf-8
import unittest
import json
from selenium import webdriver
#from pengyunhao.uiauto_test.webdriver.localpage import BasePage

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    def setUp(self):
        self.location_page=BasePage(self.driver)
        self.location_page.open()

    def test_register_case01(self):
        registerData={"username" : u'qsong',
            "email" : u'qsong.vip@qq.com',
            "password" : u'hiyoung888',
            "cpassword" : u'hiyoung888'}
        # 1获取所要操作的控件
        self.location_page.registerData(registerData)

        ele_register_bt = self.location_page.elememt__registerbt_input
        ele_retmsg = self.driver.find_element_by_id(u'regmsg')

        ele_register_bt.click()
        retmsg_text = ele_retmsg.text
        retmsg_json = json.loads(retmsg_text.split(u'成功:')[-1])
        print(retmsg_json)

        act = retmsg_json
        exp = {"uid":0,"username":"qsong","password":"hiyoung888","email":"qsong.vip@qq.com"}
        self.assertDictContainsSubset(exp,act)

    def test_register_case02(self):
        registerData = {"username": u'qsong',
                        "email": u'qsong.vip@qq.com',
                        "password": u'hiyoung888',
                        "cpassword": u'hiyoung889'}
        # 1获取所要操作的控件
        self.location_page.registerData(registerData)

        ele_register_bt = self.driver.find_element_by_xpath(u"//td[@colspan='2']/input[1]")
        ele_retmsg = self.driver.find_element_by_id(u'regmsg')

        ele_register_bt.click()
        retmsg_text = ele_retmsg.text
        print(retmsg_text)

        act = retmsg_text
        exp = u'两次输入的密码不一致'
        self.assertEqual(exp,act)

    def test_search_case03(self):
        registerData = {"username": u'qsong',
                        "email": u'qsong.vip@qq.com',
                        "password": u'hiyoung888',
                        "cpassword": u'hiyoung888'}
        # 1获取所要操作的控件
        self.location_page.registerData(registerData)
        ele_register_bt = self.driver.find_element_by_xpath(u"//td[@colspan='2']/input[1]")




        ele_register_bt.click()

        ele_insert_id = self.driver.find_element_by_xpath(u'//*[@id="search_uid"]')
        ele_insert_id.send_keys(u'0')
        ele_query_id = self.driver.find_element_by_xpath(u'//div[1]/input[2]')
        ele_query_id.click()
        ele_seamsg = self.driver.find_element_by_id(u'search_msg')
        seamsg_text = ele_seamsg.text
        seamsg_json = json.loads(seamsg_text)
        print(seamsg_json)
        act = seamsg_json
        exp = {"uid": 0, "username": "qsong", "password": "hiyoung888", "email": "qsong.vip@qq.com"}
        self.assertDictContainsSubset(exp, act)

    def test_search_case04(self):
        registerData = {"username": u'qsong',
                        "email": u'qsong.vip@qq.com',
                        "password": u'hiyoung888',
                        "cpassword": u'hiyoung888'}
        # 1获取所要操作的控件
        self.location_page.registerData(registerData)
        ele_register_bt = self.driver.find_element_by_xpath(u"//td[@colspan='2']/input[1]")

        ele_register_bt.click()

        ele_insert_name = self.driver.find_element_by_xpath(u'//*[@id="search_uname"]')
        ele_insert_name.send_keys(u'qsong')
        ele_query_name = self.driver.find_element_by_xpath(u'//div[2]/input[2]')
        ele_query_name.click()
        ele_seamsg = self.driver.find_element_by_id(u'search_msg')
        seamsg_text = ele_seamsg.text
        seamsg_json = json.loads(seamsg_text)
        print(seamsg_json)
        act = seamsg_json
        exp = {"uid": 0, "username": "qsong", "password": "hiyoung888", "email": "qsong.vip@qq.com"}
        self.assertDictContainsSubset(exp, act)

    def test_search_case05(self):
        registerData = {"username": u'qsong',
                        "email": u'qsong.vip@qq.com',
                        "password": u'hiyoung888',
                        "cpassword": u'hiyoung888'}
        # 1获取所要操作的控件
        self.location_page.registerData(registerData)
        ele_register_bt = self.driver.find_element_by_xpath(u"//td[@colspan='2']/input[1]")

        ele_register_bt.click()

        ele_insert_email = self.driver.find_element_by_xpath(u'//*[@id="search_email"]')
        ele_insert_email.send_keys(u'qsong.vip@qq.com')
        ele_query_email = self.driver.find_element_by_xpath(u'//div[3]/input[2]')
        ele_query_email.click()
        ele_seamsg = self.driver.find_element_by_id(u'search_msg')
        seamsg_text = ele_seamsg.text
        seamsg_json = json.loads(seamsg_text)
        print(seamsg_json)
        act = seamsg_json
        exp = {"uid": 0, "username": "qsong", "password": "hiyoung888", "email": "qsong.vip@qq.com"}
        self.assertDictContainsSubset(exp, act)



if __name__ == '__main__':
    unittest.main()

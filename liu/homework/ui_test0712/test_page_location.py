#encoding:utf-8
import unittest
import json
from selenium import webdriver
from liu.homework.ui_test0712.locationpage import LocationPage

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    def setUp(self):
        # url_indexPage = "http://47.92.220.226:8000/webdriver/index.html"
        # self.driver.get(url_indexPage)
        # eles_locationTest = self.driver.find_element_by_xpath('//ul/li[1]/a')
        # eles_locationTest.click()
        self.location_page = LocationPage(self.driver)
        self.location_page.open()


    def test_register_case01(self):
        register_data={
            'username' : u'qsong',
            'email' : u'qsong.vip@qq.com',
            'password' : u'hiyoung888',
            'cpassword' : u'hiyoung888'
            }

        self.location_page.register(register_data)

        retmsg_text = self.location_page.element_retmsg_label.text
        retmsg_json = json.loads(retmsg_text.split(u'成功:')[-1])
        print(retmsg_json)

        act = retmsg_json
        exp = {"uid":0,"username":"qsong","password":"hiyoung888","email":"qsong.vip@qq.com"}
        self.assertDictContainsSubset(exp,act)

    def test_register_case02(self):
        # 1获取所要操作的控件

        register_data = {
            'username': u'qsong',
            'email': u'qsong.vip@qq.com',
            'password': u'hiyoung888',
            'cpassword': u'hiyoung889'
        }

        self.location_page.register(register_data)

        retmsg_text = self.location_page.element_retmsg_label.text
        print(retmsg_text)

        act = retmsg_text
        exp = u'两次输入的密码不一致'
        self.assertNotEqual(exp,act)

    def test_search_case03(self):

        register_data = {
            'username': u'qsong',
            'email': u'qsong.vip@qq.com',
            'password': u'hiyoung888',
            'cpassword': u'hiyoung888'
        }

        self.location_page.register(register_data)

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
        self.assertDictEqual(exp, act)

    def test_search_case04(self):

        register_data = {
            'username': u'qsong',
            'email': u'qsong.vip@qq.com',
            'password': u'hiyoung888',
            'cpassword': u'hiyoung888'
        }

        self.location_page.register(register_data)

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
        self.assertDictEqual(exp, act)

    def test_search_case05(self):

        register_data = {
            'username': u'qsong',
            'email': u'qsong.vip@qq.com',
            'password': u'hiyoung888',
            'cpassword': u'hiyoung888'
        }

        self.location_page.register(register_data)

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

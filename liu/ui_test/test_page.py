#encoding:utf-8
import unittest
import json
from selenium import webdriver


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    def setUp(self):
        url_indexPage = "http://47.92.220.226/webdriver/index.html"
        self.driver.get(url_indexPage)
        eles_locationTest = self.driver.find_element_by_xpath('//ul/li[1]/a')
        eles_locationTest.click()
    def test_register_case01(self):
        # 1获取所要操作的控件
        ele_username = self.driver.find_element_by_id(u'username')
        ele_email = self.driver.find_element_by_name(u'email')
        ele_password = self.driver.find_element_by_id(u'password')
        ele_confirm_pwd = self.driver.find_element_by_css_selector(u'#confirm_password')
        ele_register_bt = self.driver.find_element_by_xpath(u"//td[@colspan='2']/input[1]")
        ele_retmsg = self.driver.find_element_by_id(u'regmsg')

        __username = u'qsong'
        __email = u'qsong.vip@qq.com'
        __password = u'hiyoung888'
        __cpassword = u'hiyoung888'

        ele_username.send_keys(__username)
        ele_email.send_keys(__email)
        ele_password.send_keys(__password)
        ele_confirm_pwd.send_keys(__cpassword)
        ele_register_bt.click()
        retmsg_text = ele_retmsg.text
        retmsg_json = json.loads(retmsg_text.split(u'成功:')[-1])
        print(retmsg_json)

        act = retmsg_json
        exp = {"uid":0,"username":"qsong","password":"hiyoung888","email":"qsong.vip@qq.com"}
        self.assertDictContainsSubset(exp,act)

    def test_register_case02(self):
        # 1获取所要操作的控件
        ele_username = self.driver.find_element_by_id(u'username')
        ele_email = self.driver.find_element_by_name(u'email')
        ele_password = self.driver.find_element_by_id(u'password')
        ele_confirm_pwd = self.driver.find_element_by_css_selector(u'#confirm_password')
        ele_register_bt = self.driver.find_element_by_xpath(u"//td[@colspan='2']/input[1]")
        ele_retmsg = self.driver.find_element_by_id(u'regmsg')

        __username = u'qsong'
        __email = u'qsong.vip@qq.com'
        __password = u'hiyoung888'
        __cpassword = u'hiyoung889'

        ele_username.send_keys(__username)
        ele_email.send_keys(__email)
        ele_password.send_keys(__password)
        ele_confirm_pwd.send_keys(__cpassword)
        ele_register_bt.click()
        retmsg_text = ele_retmsg.text
        print(retmsg_text)

        act = retmsg_text
        exp = u'两次输入的密码不一致'
        self.assertEqual(exp,act)

    def test_search_case03(self):
        ele_username = self.driver.find_element_by_id(u'username')
        ele_email = self.driver.find_element_by_name(u'email')
        ele_password = self.driver.find_element_by_id(u'password')
        ele_confirm_pwd = self.driver.find_element_by_css_selector(u'#confirm_password')
        ele_register_bt = self.driver.find_element_by_xpath(u"//td[@colspan='2']/input[1]")

        __username = u'qsong'
        __email = u'qsong.vip@qq.com'
        __password = u'hiyoung888'
        __cpassword = u'hiyoung888'

        ele_username.send_keys(__username)
        ele_email.send_keys(__email)
        ele_password.send_keys(__password)
        ele_confirm_pwd.send_keys(__cpassword)
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
        ele_username = self.driver.find_element_by_id(u'username')
        ele_email = self.driver.find_element_by_name(u'email')
        ele_password = self.driver.find_element_by_id(u'password')
        ele_confirm_pwd = self.driver.find_element_by_css_selector(u'#confirm_password')
        ele_register_bt = self.driver.find_element_by_xpath(u"//td[@colspan='2']/input[1]")

        __username = u'qsong'
        __email = u'qsong.vip@qq.com'
        __password = u'hiyoung888'
        __cpassword = u'hiyoung888'

        ele_username.send_keys(__username)
        ele_email.send_keys(__email)
        ele_password.send_keys(__password)
        ele_confirm_pwd.send_keys(__cpassword)
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
        ele_username = self.driver.find_element_by_id(u'username')
        ele_email = self.driver.find_element_by_name(u'email')
        ele_password = self.driver.find_element_by_id(u'password')
        ele_confirm_pwd = self.driver.find_element_by_css_selector(u'#confirm_password')
        ele_register_bt = self.driver.find_element_by_xpath(u"//td[@colspan='2']/input[1]")

        __username = u'qsong'
        __email = u'qsong.vip@qq.com'
        __password = u'hiyoung888'
        __cpassword = u'hiyoung888'

        ele_username.send_keys(__username)
        ele_email.send_keys(__email)
        ele_password.send_keys(__password)
        ele_confirm_pwd.send_keys(__cpassword)
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

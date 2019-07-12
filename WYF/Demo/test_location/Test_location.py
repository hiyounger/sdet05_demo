#  coding:utf-8
import json
import unittest
from selenium import webdriver



class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()

    def setUp(self):
        url='http://47.92.220.226:8000/webdriver/location.html'
        self.driver.get(url)

    @classmethod
    def testpage_quit(cls):
        cls.driver.quit()

    # 注册成功
    def test_regiser(self):
        ele_username = self.driver.find_element_by_id(u'username')
        ele_email = self.driver.find_element_by_name(u'email')
        ele_password = self.driver.find_element_by_xpath(u'//*[@id="password"]')
        ele_password_enter = self.driver.find_element_by_css_selector(u'#confirm_password')
        ele_register_bt = self.driver.find_element_by_xpath(u"//td[@colspan='2']/input[1]")
        ele_result = self.driver.find_element_by_id(u'regmsg')


        ele_username.send_keys(u'Wang')
        ele_email.send_keys(u'wang@qq.com')
        ele_password.send_keys(u'123456')
        ele_password_enter.send_keys(u'123456')

        ele_register_bt.click()

        result = ele_result.text
        act_result_json = json.loads(result.split(u'成功:')[-1], encoding='utf-8')
        exp={u'username': u'Wang', u'password': u'123456',  u'email': u'wang@qq.com'}

        self.assertDictContainsSubset(exp,act_result_json)


    # 注册失败
    def test_regiser_fail(self):
        ele_username = self.driver.find_element_by_id(u'username')
        ele_email = self.driver.find_element_by_name(u'email')
        ele_password = self.driver.find_element_by_xpath(u'//*[@id="password"]')
        ele_password_enter = self.driver.find_element_by_css_selector(u'#confirm_password')
        ele_register_bt = self.driver.find_element_by_xpath(u"//td[@colspan='2']/input[1]")
        ele_result = self.driver.find_element_by_id(u'regmsg')

        ele_username.send_keys(u'Wang')
        ele_email.send_keys(u'wang@qq.com')
        ele_password.send_keys(u'123456')
        ele_password_enter.send_keys(u'123321')

        ele_register_bt.click()

        act= ele_result.text

        exp =(u'两次输入的密码不一致')

        self.assertEqual(act, exp)

    # 根据用户ID查询
    def test_select_by_id(self):
        ele_username = self.driver.find_element_by_id(u'username')
        ele_email = self.driver.find_element_by_name(u'email')
        ele_password = self.driver.find_element_by_xpath(u'//*[@id="password"]')
        ele_password_enter = self.driver.find_element_by_css_selector(u'#confirm_password')
        ele_register_bt = self.driver.find_element_by_xpath(u"//td[@colspan='2']/input[1]")

        ele_username.send_keys(u'Wang')
        ele_email.send_keys(u'wang@qq.com')
        ele_password.send_keys(u'123456')
        ele_password_enter.send_keys(u'123456')

        ele_register_bt.click()

        ele_select_id = self.driver.find_element_by_id(u"search_uid")
        ele_retmsg=self.driver.find_element_by_xpath(u'/html/body/div[2]/div[1]/input[2]')
        ele_result = self.driver.find_element_by_xpath(u'//*[@id="search_msg"]')

        ele_select_id.send_keys(u'0')
        ele_retmsg.click()

        act_retmsg_json=json.loads(ele_result.text,encoding='utf-8')
        exp={"uid":0,"username":"Wang","password":"123456","email":"wang@qq.com"}

        self.assertEqual(exp, act_retmsg_json)

    # 根据用户email查询
    def test_select_by_email(self):
        ele_username = self.driver.find_element_by_id(u'username')
        ele_email = self.driver.find_element_by_name(u'email')
        ele_password = self.driver.find_element_by_xpath(u'//*[@id="password"]')
        ele_password_enter = self.driver.find_element_by_css_selector(u'#confirm_password')
        ele_register_bt = self.driver.find_element_by_xpath(u"//td[@colspan='2']/input[1]")

        ele_username.send_keys(u'Wang')
        ele_email.send_keys(u'wang@qq.com')
        ele_password.send_keys(u'123456')
        ele_password_enter.send_keys(u'123456')

        ele_register_bt.click()

        ele_select_email = self.driver.find_element_by_id(u"search_email")
        ele_retmsg=self.driver.find_element_by_xpath(u'/html/body/div[2]/div[3]/input[2]')
        ele_result = self.driver.find_element_by_xpath(u'//*[@id="search_msg"]')

        ele_select_email.send_keys(u'wang@qq.com')
        ele_retmsg.click()

        act_retmsg_json=json.loads(ele_result.text,encoding='utf-8')
        exp = {"uid": 0, "username": "Wang", "password": "123456", "email": "wang@qq.com"}

        self.assertEqual(exp, act_retmsg_json)

    # 根据用户名查询
    def test_select_by_username(self):
        ele_username = self.driver.find_element_by_id(u'username')
        ele_email = self.driver.find_element_by_name(u'email')
        ele_password = self.driver.find_element_by_xpath(u'//*[@id="password"]')
        ele_password_enter = self.driver.find_element_by_css_selector(u'#confirm_password')
        ele_register_bt = self.driver.find_element_by_xpath(u"//td[@colspan='2']/input[1]")

        ele_username.send_keys(u'Wang')
        ele_email.send_keys(u'wang@qq.com')
        ele_password.send_keys(u'123456')
        ele_password_enter.send_keys(u'123456')

        ele_register_bt.click()

        ele_select_username=self.driver.find_element_by_id(u"search_uname")
        ele_retmsg=self.driver.find_element_by_xpath(u'/html/body/div[2]/div[2]/input[2]')
        ele_result = self.driver.find_element_by_xpath(u'//*[@id="search_msg"]')

        ele_select_username.send_keys(u'Wang')
        ele_retmsg.click()

        act_retmsg_json=json.loads(ele_result.text,encoding='utf-8')
        exp={"uid": 0, "username": "Wang", "password": "123456", "email": "wang@qq.com"}
        self.assertEqual(exp, act_retmsg_json)



if __name__ == '__main__':
    unittest.main()

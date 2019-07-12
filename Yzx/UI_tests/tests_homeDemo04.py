#encoding:utf-8
import unittest
from selenium import  webdriver
import json



class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    def setUp(self):
        url = "http://47.92.220.226:8000/webdriver/location.html"
        self.driver.get(url)
        # 定位
        input_name = self.driver.find_element_by_id(u'username')
        input_email = self.driver.find_element_by_name(u'email')
        input_password = self.driver.find_element_by_id(u'password')
        input_twopwd = self.driver.find_element_by_css_selector(u'#confirm_password')
        denglu = self.driver.find_element_by_xpath(u'//td[@colspan]/input[1]')
        # 赋值{u'username': u'yanzhenxing', u'password': u'1233', u'uid': 0, u'email': u'1234@qq.com'}
        data = {
            'username': u'yanzhenxing',
            'email': u'1234@qq.com',
            'password': u'1233',
        }
        input_name.send_keys(data['username'])
        input_email.send_keys(data['email'])
        input_password.send_keys(data['password'])
        input_twopwd.send_keys(data['password'])
        # 点击
        denglu.click()
    def test_something(self):
        # 获得期望值
        ele_regmsg = self.driver.find_element_by_id(u"regmsg")
        regmsg_text = ele_regmsg.text
        regmsg_json = json.loads(regmsg_text.split(u"成功:")[-1], encoding='utf-8')

        elems = self.driver.find_element_by_id(u'search_uname')
        elems.send_keys(regmsg_json[u'username'])
        ele_search_name = self.driver.find_element_by_xpath(u'/html/body/div[2]/div[2]/input[2]')
        ele_search_name.click()
        seacher_name = self.driver.find_element_by_id(u'search_msg')
        seacher_name_text = seacher_name.text
        seacher_text_name_json = json.loads(seacher_name_text)
        self.assertEqual(regmsg_json,seacher_text_name_json)


if __name__ == '__main__':
    unittest.main()

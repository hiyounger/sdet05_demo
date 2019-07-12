#encoding:utf-8
import unittest
from selenium import webdriver
import json

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
    def setUp(self):
        url="http://47.92.220.226/webdriver/location.html"
        self.driver.get(url)

    #注册成功
    def test_registeSuccess(self):
        #1.获取所要操作的控件
        ele_username=self.driver.find_element_by_id(u"username")
        ele_email = self.driver.find_element_by_id(u"email")
        ele_password = self.driver.find_element_by_id(u"password")
        ele_surePassword = self.driver.find_element_by_id(u"confirm_password")
        ele_regBt = self.driver.find_element_by_xpath(u"/html/body/div[1]/form/table/tbody/tr[5]/td/input[1]")
        ele_regmsg=self.driver.find_element_by_id(u"regmsg")

        #2输入
        username=u"root"
        email = u"1322@qq"
        password = u"12345"
        surePassword = u"12345"

        #加入输入内容
        ele_username.send_keys(username)
        ele_email.send_keys(email)
        ele_password.send_keys(password)
        ele_surePassword.send_keys(surePassword)
        #点击登录
        ele_regBt.click()
        #查看输入的所有值
        ele_regmsg_text=ele_regmsg.text
        jsonData=json.loads(ele_regmsg_text.split(u"成功:")[-1],encoding="utf-8")
        print jsonData
        exp_result={u'username': u'root', u'password': u'12345',u'email': u'1322@qq'}
        asc_result=jsonData
        self.assertDictContainsSubset(exp_result,asc_result)
    # #注册失败
    # def test_registeFiled(self):
    #     # 1.获取所要操作的控件
    #     ele_username = self.driver.find_element_by_id(u"username")
    #     ele_email = self.driver.find_element_by_id(u"email")
    #     ele_password = self.driver.find_element_by_id(u"password")
    #     ele_surePassword = self.driver.find_element_by_id(u"confirm_password")
    #     ele_regBt = self.driver.find_element_by_xpath(u"/html/body/div[1]/form/table/tbody/tr[5]/td/input[1]")
    #     ele_regmsg = self.driver.find_element_by_id(u"regmsg")
    #
    #     # 2输入
    #     username = u"zhangsan"
    #     email = u"1322@qq"
    #     password = u"12345"
    #     surePassword = u"123"
    #
    #     # 加入输入内容
    #     ele_username.send_keys(username)
    #     ele_email.send_keys(email)
    #     ele_password.send_keys(password)
    #     ele_surePassword.send_keys(surePassword)
    #     # 点击登录
    #     ele_regBt.click()
    #     # 查看输入的所有值
    #     ele_regmsg_text = ele_regmsg.text
    #     exp_result = ele_regmsg_text
    #     asc_result = u"两次输入的密码不一致"
    #     self.assertEqual(exp_result,asc_result)
    # case03.通过ID查询一个已存在的用户、
    def test_queryByID(self):
        ele_byid=self.driver.find_element_by_id(u"search_uid")
        ele_btByID = self.driver.find_element_by_xpath(u"//div[2]/div[1]/input[2]")
        ele_byidmsg = self.driver.find_element_by_id(u"search_msg")


        id=0
        ele_byid.send_keys(id)
        ele_btByID.click()

        exp_result={"uid":0,"username":"root","password":"12345","email":"1322@qq"}
        asc_result=json.loads(ele_byidmsg.text)
        print "exp:",exp_result
        print "asc",asc_result
        print "--------------------"
        self.assertDictEqual(exp_result,asc_result)


if __name__ == '__main__':
    unittest.main()

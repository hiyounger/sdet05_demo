#encoding:utf-8
from selenium import webdriver

"""
class Registg():
    @classmethod
    def setUpClass(cls):

    @classmethod
    def setUp(self):
        url = "http://47.92.220.226:8000/webdriver/location.html"
        self.driver.get(url)
    @classmethod
    def registgData(self,):
        driver = webdriver.Firefox()
        # 1.获取所要操作的控件
        ele_username = self.driver.find_element_by_id(u"username")
        ele_email = self.driver.find_element_by_id(u"email")
        ele_password = self.driver.find_element_by_id(u"password")
        ele_surePassword = self.driver.find_element_by_id(u"confirm_password")
        ele_regBt = self.driver.find_element_by_xpath(u"/html/body/div[1]/form/table/tbody/tr[5]/td/input[1]")
        ele_regmsg = self.driver.find_element_by_id(u"regmsg")

        # 2输入
        username = u"root"
        email = u"1322@qq"
        password = u"12345"
        surePassword = u"12345"

        # 加入输入内容
        ele_username.send_keys(username)
        ele_email.send_keys(email)
        ele_password.send_keys(password)
        ele_surePassword.send_keys(surePassword)
        # 点击登录
        ele_regBt.click()
"""
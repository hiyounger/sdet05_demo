# -*- encoding:utf-8 -*-

class locationPage():

    url="http://47.92.220.226:8000/webdriver/location.html"
    def __init__(self,driver):
        self.driver=driver

    def open(self):
        self.driver.get(self.url)

    def register(self,register_data):
        self.ele_username_input.send_keys(register_data["username"])
        self.ele_email_input.send_keys(register_data["email"])
        self.ele_password_input.send_keys(register_data["password"])
        self.ele_confirm_password_input.send_keys(register_data["cpassword"])
        self.ele_submit.click()


    @property
    def ele_username_input(self):
        ele=self.driver.find_element_by_id("username1")
        return ele

    @property
    def ele_email_input(self):
        ele = self.driver.find_element_by_id("email")
        return ele

    @property
    def ele_password_input(self):
        ele = self.driver.find_element_by_id("password")
        return ele

    @property
    def ele_confirm_password_input(self):
        ele = self.driver.find_element_by_id("confirm_password")
        return ele

    @property
    def ele_submit(self):
        ele = self.driver.find_element_by_xpath("//tbody/tr[5]/td/input[1]")
        return ele

    @property
    def ele_regmsg(self):
        ele = self.driver.find_element_by_id("regmsg")
        return ele


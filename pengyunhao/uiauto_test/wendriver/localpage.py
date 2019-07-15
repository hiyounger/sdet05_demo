#encoding:utf-8

class BasePage():

    url="http://47.92.220.226:8000/webdriver/location.html"

    def __init__(self,driver):
        self.driver=driver

    def open(self):
        self.driver.get(self.url)

    def registerData(self,registerData):
        self.elememt_username_input.send_keys(registerData["username"])
        self.elememt_email_input.send_keys(registerData["email"])
        self.elememt_password_input.send_keys(registerData["password"])
        self.elememt_confirm_pwdinput.send_keys(registerData["cpassword"])

    @property
    def elememt_username_input(self):
        ele_username = self.driver.find_element_by_id(u'username1')
        return ele_username

    @property
    def elememt_email_input(self):
        ele_email = self.driver.find_element_by_name(u'email')
        return ele_email

    @property
    def elememt_password_input(self):
        ele_password = self.driver.find_element_by_id(u'password')
        return ele_password

    @property
    def elememt_confirm_pwdinput(self):
        ele_confirm_pwd = self.driver.find_element_by_css_selector(u'#confirm_password')
        return ele_confirm_pwd

    @property
    def elememt__registerbt_input(self):
        ele_registerbt = self.driver.find_element_by_xpath(u"//td[@colspan='2']/input[1]")
        return ele_registerbt


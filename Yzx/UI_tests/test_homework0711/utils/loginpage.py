#encoding:utf-8


class LoginPageUtils():

    @classmethod
    def register(cls, driver):
        # 定位
        input_name = driver.find_element_by_id(u'username')
        input_email = driver.find_element_by_name(u'email')
        input_password = driver.find_element_by_id(u'password')
        input_twopwd = driver.find_element_by_css_selector(u'#confirm_password')
        denglu = driver.find_element_by_xpath(u'//td[@colspan]/input[1]')
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
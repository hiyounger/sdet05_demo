# encoding:utf-8
# 开发团队：辉远科技
# 开发人员：
# 开发时间：2019/8/16 20:20
# 文件名称：crm_demo.py
# 开发工具：PyCharm
import time
from . import config


class Crm:
    '''
    客户关系管理类
    '''

    def __init__(self, driver):
        self.driver = driver

    def write(self, xpath):
        chishu = int(config.wait_max_time / config.wait_time)
        for i in range(chishu):
            try:
                element = self.driver.find_element_by_xpath(xpath)
                # print ("在第%s秒找到这个控件"%(i/2))
                return element
            except:
                time.sleep(config.wait_time)
                if i == (chishu - 1):
                    print("无法获取xpath为%s的控件" % xpath)
                    return None

    @property
    def putin1(self):
        element = self.driver.find_element_by_id('android:id/button1')
        return element

    @property
    def putin2(self):
        element = self.driver.find_element_by_xpath('//android.view.View[@content-desc="立即体验"]')
        return element

    @property
    def usermame(self):
        try:
            element = self.driver.find_element_by_xpath(
                '//android.webkit.WebView[@content-desc="crm_app"]/android.view.View/android.view.View/android.view.View[4]/android.view.View[1]/android.widget.EditText')
        except:
            time.sleep(5)
            element = self.driver.find_element_by_xpath(
                '//android.webkit.WebView[@content-desc="crm_app"]/android.view.View/android.view.View/android.view.View[4]/android.view.View[1]/android.widget.EditText')
        username = element.send_keys('13590177837')
        return username

    @property
    def passward(self):
        try:
            element = self.driver.find_element_by_xpath(
                '//android.webkit.WebView[@content-desc="crm_app"]/android.view.View/android.view.View/android.view.View[4]/android.view.View[2]/android.widget.EditText')
        except:
            time.sleep(5)
            element = self.driver.find_element_by_xpath(
                '//android.webkit.WebView[@content-desc="crm_app"]/android.view.View/android.view.View/android.view.View[4]/android.view.View[2]/android.widget.EditText')
        passward = element.send_keys('1991626')
        return passward

    @property
    def login_button(self):
        element = self.driver.find_element_by_xpath('//android.view.View[@content-desc="登录"]')
        return element

    # 待办模块
    @property
    def daiban_button(self):
        xpath = '(//android.view.View[@content-desc="待办"])[1]/android.view.View[1]'
        element = self.write(xpath)
        return element

    @property
    def vertify_result(self):
        xpath = '//android.view.View[@content-desc="待办事项"]'
        element = self.write(xpath)
        return element

    @property
    def contact_client_button(self):
        xpath = '//android.view.View[@content-desc=" 今日需联系客户 "]/android.view.View[3]'
        element = self.write(xpath)
        return element

    @property
    def vertify_clienttitle(self):
        xpath = '//android.view.View[@content-desc="今日需联系客户"]'
        element = self.write(xpath)
        return element

    @property
    def contact_button(self):
        xpath = '//android.view.View[@content-desc="今日需联系"]'
        element = self.write(xpath)
        return element

    @property
    def outdate_button(self):
        xpath = '//android.view.View[@content-desc="已逾期"]'
        element = self.write(xpath)
        return element

    @property
    def vertify_contact(self):
        xpath = '//android.view.View[@content-desc="兔兔我我 管理员 最后跟进时间：2019-08-09"]'
        element = self.write(xpath)
        return element

    @property
    def fenpeixians(self):
        xpath = '//android.view.View[@content-desc=" 分配给我的线索 "]/android.view.View[3]'
        element = self.write(xpath)
        return element

    @property
    def fenpeixians_result(self):
        xpath = '//android.view.View[@content-desc="分配给我的线索"]'
        element = self.write(xpath)
        return element

    # @property
    # def back(self):
    #     element=self.driver.find_element_by_xpath('//android.widget.Button[@content-desc=" "]')
    #     return element

    # CRM模块
    @property
    def cr(self):
        xpath = '(//android.view.View[@content-desc="CRM"])[1]/android.view.View[1]'
        element = self.write(xpath)
        return element

    @property
    def cr_info(self):
        xpath = '//android.view.View[@content-desc="悟空CRM"]'
        element = self.write(xpath)
        return element

    @property
    def xiansuo_info(self):
        xpath = '//android.view.View[@content-desc="线索"]'
        element = self.write(xpath)
        return element

    @property
    def xinjian_info(self):
        xpath = '//android.webkit.WebView[@content-desc="crm_app"]/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.widget.Button[2]'
        element = self.write(xpath)
        return element

    @property
    def xinjinan_input(self):
        xpath = '//android.webkit.WebView[@content-desc="crm_app"]/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View/android.widget.EditText'
        element = self.write(xpath)
        return element

    @property
    def save(self):
        xpath = '//android.widget.Button[@content-desc="保存"]'
        element = self.write(xpath)
        return element

    @property
    def tishi(self):
        xpath = '//android.view.View[@content-desc="线索名称已经存在,不能重复添加"]'
        element = self.write(xpath)
        return element

    @property
    def add_success(self):
        xpath = '//android.view.View[@content-desc="123451"]'
        element = self.write(xpath)
        return element

    @property
    def de_xiansuosetp1(self):
        xpath = '//android.view.View[@content-desc="阿宝宇"]'
        element = self.write(xpath)
        return element

    @property
    def de_xiansuostep2(self):
        xpath = '(//android.view.View[@content-desc="更多"])[1]/android.view.View[1]'
        element = self.write(xpath)
        return element

    @property
    def de_xiansuostep3(self):
        xpath = '//android.view.View[@content-desc="删除"]'
        element = self.write(xpath)
        return element

    @property
    def de_xiansuostep4(self):
        xpath = '//android.widget.Button[@content-desc="确定"]'
        element = self.write(xpath)
        return element

    @property
    def delete_success(self):
        xpath = '//android.view.View[@content-desc="删除成功"]'
        element = self.write(xpath)
        return element

    @property
    def update_step1(self):
        xpath = '//android.view.View[@content-desc="www1"]'
        element = self.write(xpath)
        return element

    @property
    def update_step2(self):
        xpath = '//android.webkit.WebView[@content-desc="crm_app"]/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View[2]/android.widget.Button'
        element = self.write(xpath)
        return element

    @property
    def upadte_step3(self):
        xpath = '/android.webkit.WebView[@content-desc="crm_app"]/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View/android.widget.EditText'
        element = self.write(xpath)
        return element

    @property
    def update_success(self):
        xpath = '//android.view.View[@content-desc="编辑成功"]'
        element = self.write(xpath)
        return element

    # 办公模块
    @property
    def bangong(self):
        xpath = '(//android.view.View[@content-desc="办公"])[1]/android.view.View[1]'
        element = self.write(xpath)
        return element

    @property
    def bangong_result(self):
        xpath = '(//android.view.View[@content-desc="办公"])[1]'
        element = self.write(xpath)
        return element

    @property
    def shenpi(self):
        xpath = '//android.widget.Image[@content-desc="k7phpPs3wVejHsJniXR6f4kUojFW2j8nkh+jQdagXAIhhpmCRlNfORf05zi6WVaF+6hvoJVY39zOfe+TECM4R5MQI4D4XzgErXD7h3cEAAAAAElFTkSuQmCC"]'
        element = self.write(xpath)
        return element

    @property
    def shenpi_result(self):
        xpath = '//android.view.View[@content-desc="审批"]'
        element = self.write(xpath)
        return element

    @property
    def putongshenpi(self):
        xpath = '//android.widget.Image[@content-desc="AOOXIC1B4kSyAAAAAElFTkSuQmCC"]'
        element = self.write(xpath)
        return element

    @property
    def putongshenpi_result(self):
        element = self.driver.find_element_by_accessibility_id(u'新建普通审批')
        return element

    @property
    def qingjiashenpi(self):
        xpath = '//android.widget.Image[@content-desc="SlgBqGz6ouI2VgcCRZZFsZ8jZb40yKYMW9FM12xpzDcD5LhurEiEybv0jGDIBulpeerI6G9DxhVmMoOMEt11uibXgoW0Z5H5UHOjgssWR6fpJrS2BqQZt8hX9LjCxuI9KwcDcvqkfZFkcZe00isBa7W2WNYX53kbPA48F1piT893qjpgVmYXbFa4G6MfAZMnZbJyQJn+jG8hrAFYRPN8QN2guEEbMTYtFFCVcUMiNQS4SYi0gDMJUE1Ihk+gjJZiRZov8YMEOEMRg4DexlOvIhJHKTnwklp46IrXv8LpKKdcsyKVVsAAAAASUVORK5CYII="]'
        element = self.write(xpath)
        return element

    @property
    def qingjiashenpi_result(self):
        xpath = '//android.view.View[@content-desc="新建请假审批"]'
        element = self.write(xpath)
        return element

    @property
    def chuchaishenpi(self):
        xpath = '//android.widget.Image[@content-desc="FJAnQp8B22KGzV3lrMC2gSkI9i7vh0UzFZgMyPMR1Mm1b7AZUZRDCDagU95j8JzDcoDhGTBH7oLndMRFJ2OmHzblDoTIQyg5KCSC8Ow74H1T2RC0qpgQnEfhBLATITahKEdpqDvL2OfaPRTkfwGcYk7lnKeMHAAAAABJRU5ErkJggg=="]'
        element = self.write(xpath)
        return element

    @property
    def chuchaishenpi_result(self):
        xpath = '//android.view.View[@content-desc="新建出差审批"]'
        element = self.write(xpath)
        return element

    # 我的模块
    @property
    def wOfaqide(self):
        xpath = '//android.widget.Image[@content-desc="wczWCGdSF4xWwAAAABJRU5ErkJggg=="]'
        element = self.write(xpath)
        return element

    @property
    def wofaqide_result(self):
        xpath = '//android.view.View[@content-desc="我发起的"]'
        element = self.write(xpath)
        return element

    @property
    def wode(self):
        xpath = '(//android.view.View[@content-desc="我的"])[1]'
        element = self.write(xpath)
        return element

    @property
    def wode_result(self):
        xpath = '(//android.view.View[@content-desc="我的"])[1]'
        element = self.write(xpath)
        return element

    @property
    def guanliyuan(self):
        xpath = '//android.view.View[@content-desc="管理员"]'
        element = self.write(xpath)
        return element

    @property
    def guanliyuan_result(self):
        xpath = '//android.view.View[@content-desc="个人信息"]'
        element = self.write(xpath)
        return element

    @property
    def back3(self):
        xpath = '//android.widget.Button[@content-desc=" "]'
        element = self.write(xpath)
        return element

    @property
    def back3_result(self):
        xpath = '(//android.view.View[@content-desc="我的"])[1]'
        element = self.write(xpath)
        return element

    @property
    def tel(self):
        xpath = '//android.view.View[@content-desc="企业通讯录"]'
        element = self.write(xpath)
        return element

    @property
    def tel_result(self):
        xpath = '//android.view.View[@content-desc="公司通讯录"]'
        element = self.write(xpath)
        return element

    @property
    def back4(self):
        xpath = '//android.widget.Button[@content-desc=" "]'
        element = self.write(xpath)
        return element

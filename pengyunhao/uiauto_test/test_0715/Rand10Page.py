#encoding:utf-8

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class Rand10Page():
    url="http://demo.hiyounger.cn/webdriver/10seconds"
    title=u"加载需要10秒的页面"
    keyword_xpath = u"//h1"
    keyword_text=u"HiYoung Webdriver Demo - 10 Seconds Loading Page"
    open_timeout = 20


    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)
    # 1. 判断页面是否正确打开，依据（标题、url、页面关键字）三个元素进行判断
    # 如果正常打开，返回True，否则，返回False
    def if_page_opened_success(self):
        act_page_title = self.driver.title
        act_page_url = self.driver.current_url

        # 1. 等待页面加载（动态的）,等待页面出现指定关键字，如果没出现，返回False，对应信息
        try:
            WebDriverWait(self.driver, self.open_timeout).until(
                expected_conditions.text_to_be_present_in_element((By.XPATH, self.keyword_xpath),
                                                                  self.keyword_text))
        except:
            return False, {"err_msg": "等待超时，指定页面元素(%s, %s)未找到" % (self.keyword_xpath, self.keyword_text)}

        failed_dic = {}
        if self.title != act_page_title:
            failed_dic['title'] = {"exp_value": self.title, "act_value": act_page_title}
        if self.url != act_page_url:
            failed_dic['url'] = {"exp_value": self.url, "act_value": act_page_url}

        if len(failed_dic.keys()) == 0:
            return True, {}
        else:
            return False, failed_dic

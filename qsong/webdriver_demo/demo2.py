# -*- encoding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time

# #1. 初始化一个Firefox 浏览器的driver
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

#1. 根据元素定位器与元素的文字进行等待（注意：不是value）
WebDriverWait(driver, 5).until(expected_conditions.text_to_be_present_in_element((By.XPATH, u"//div[@id='u1']/a[1]"), u"新闻"))

#2. 指定元素是否在页面可见
bt = driver.find_element(By.ID, u"su")
WebDriverWait(driver, 5).until(expected_conditions.visibility_of(bt))

#3. 指定定位器所代表的元素是否在页面可见
locator = (By.ID, u"su")
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locator))

#4. 关于页面元素找不到的异常处理方法
try:
    WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element((By.ID, u"su"), u"百度一下"))
except:
    print("页面打开超时或未发现指定控件(%s, %s)" % ("id=su", "百度一下"))

end_time = time.time()
cost_time = end_time - start_time
print("Cost time: %s" % cost_time)


#
# #2. 打开指定的页面url
# url_indexPage = "http://47.92.220.226:8000/webdriver/index.html"
# driver.get(url_indexPage)
#
# baidu_link = driver.find_element_by_link_text(u"百度一下")
# baidu_link.click()
#
#
#
#
# time.sleep(1)
# print(driver.title)
# print(driver.window_handles)
# driver.switch_to.window(driver.window_handles[-1])
#
# time.sleep(1)
# print(driver.title)
#
# driver.switch_to.window(driver.window_handles[0])
# time.sleep(1)
# print(driver.title)
#
# frame_link = driver.find_element_by_link_text(u"Frame框架页面")
# frame_link.click()
#
# middle_frame = driver.find_element_by_id(u"middleframe")
# driver.switch_to.frame(middle_frame)
#
# iframe = driver.find_element_by_id(u"iframe")
# driver.switch_to.frame(iframe)
#
# title_input = driver.find_element_by_id(u"note_title")
# title_input.send_keys(u"hello frame")
#
# driver.switch_to.default_content()
# title_input = driver.find_element_by_id(u"middleframe")



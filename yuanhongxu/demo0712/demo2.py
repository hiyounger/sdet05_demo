# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

start_time = time.time()
# 根据元素定位器和元素文字进行等待
# WebDriverWait(driver,5).until(expected_conditions.text_to_be_present_in_element((By.XPATH,'//div[@id="u1"]/a[1]'),u"新闻"))

# 指定元素在页面可见
# bt=driver.find_element(By.ID,"su")
#  WebDriverWait(driver,3).until(expected_conditions.visibility_of(bt))

# 指定元素选择器在页面可见
locator = (By.ID, "su")
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locator))

# try:
#     WebDriverWait(driver, 5).until(
#         expected_conditions.text_to_be_present_in_element((By.ID, 'su'), u"百度一下"))
# except:
#     print "页面超时或者未找到控件"


end_time = time.time()
cost_time = end_time - start_time
print cost_time

# url = "http://47.92.220.226:8000/webdriver/index.html"
# driver.get(url)

# baidu_link=driver.find_element_by_link_text(u"百度一下")
# baidu_link.click()

# time.sleep(1)
# print (driver.title)
# print (driver.window_handles)
# driver.switch_to.window(driver.window_handles[-1])
# print (driver.title)
# time.sleep(1)
# driver.switch_to.window(driver.window_handles[0])
# print (driver.title)

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
# title_input.send_keys(u"hello")
#
# driver.switch_to.default_content()
# title_input = driver.find_element_by_id(u"middleframe")

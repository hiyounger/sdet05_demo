#encoding:utf-8

from selenium import webdriver
import time

driver=webdriver.Firefox()
url="http://47.92.220.226:8000/webdriver/"
driver.get(url)

# baidu_link=driver.find_element_by_link_text(u"百度一下")
# baidu_link.click()
#
# time.sleep(2)
# print (driver.title)
# print (driver.window_handles)
# driver.switch_to.window(driver.window_handles[-1])
# time.sleep(2)
# print (driver.title)
#
# driver.switch_to.window(driver.window_handles[0])
# time.sleep(2)
# print (driver.title)

frame_link=driver.find_element_by_link_text(u"Frame框架页面")
frame_link.click()

middle_frame=driver.find_element_by_id("middleframe")
driver.switch_to.frame(middle_frame)

iframe=driver.find_element_by_id("iframe")
driver.switch_to.frame(iframe)

title_input=driver.find_element_by_id("note_title")
title_input.send_keys(u"hello hello hello")

driver.switch_to.default_content()
middle_frame=driver.find_element_by_id("middleframe")

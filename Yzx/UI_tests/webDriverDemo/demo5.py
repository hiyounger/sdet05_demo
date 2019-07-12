#encoding:utf-8
from selenium import webdriver
import json
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
driver= webdriver.Firefox()

url="http://47.92.220.226:8000/webdriver/"
driver.get(url)
# 页面跳转
element=driver.find_element_by_partial_link_text(u"百度一下")
element.click()
print driver.title
print  driver.window_handles
time.sleep(1)
driver.switch_to.window(driver.window_handles[-1])
print driver.title
time.sleep(1)
driver.switch_to.window(driver.window_handles[0])
print driver.title
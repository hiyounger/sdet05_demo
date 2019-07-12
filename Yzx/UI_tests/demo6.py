#encoding:utf-8
from selenium import webdriver
import json
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
driver= webdriver.Firefox()

url="http://47.92.220.226:8000/webdriver/"
driver.get(url)

frame1=driver.find_element_by_link_text(u'Frame框架页面')
frame1.click()
middle_frame=driver.find_element_by_id(u'middleframe')
driver.switch_to.frame(middle_frame)

iframe=driver.find_element_by_id(u'iframe')
driver.switch_to.frame(iframe)

title_input=driver.find_element_by_id(u'note_title')
title_input.send_keys(u'我是爸爸')
#encoding:utf-8
from selenium import webdriver
driver= webdriver.Firefox()

url="http://47.92.220.226/webdriver/"
driver.get(url)

# eles=driver.find_element_by_link_text(u'定位方法测试页面')
# eles.click()
eles = driver.find_element_by_partial_link_text(u'测试页面')
eles.click()

input_name=driver.find_element_by_id(u'username')
input_name.send_keys(u'yanzhenxing')
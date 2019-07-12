#encoding:utf-8
from selenium import webdriver
driver= webdriver.Firefox()

url="http://47.92.220.226/webdriver/"
driver.get(url)

eles=driver.find_elements_by_tag_name(u"a")
element_click=None
for element in eles:
    if element.text==u'定位方法测试页面':
        element_click=element
element_click.click()


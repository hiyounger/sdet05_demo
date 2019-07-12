#encoding:utf-8
from selenium import webdriver
driver= webdriver.Firefox()

url="http://47.92.220.226/webdriver/"
driver.get(url)

eles=driver.find_element_by_xpath('//ul/li[1]/a')
eles.click()



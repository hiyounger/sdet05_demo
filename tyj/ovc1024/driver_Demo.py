# encoding:utf-8
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://www.baidu.com')

soso_input = browser.find_element_by_xpath('//*[@id="kw"]')
soso_input.send_keys("ovc1024")

login_bt2=browser.find_element_by_xpath('//*[@id="su"]')
login_bt2.click()

browser.find_element_by_xpath()
browser.find_element_by_name()

# login_bt=browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[3]/a[7]")
# login_bt.click()


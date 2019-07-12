# encoding:utf-8
import time
from selenium import webdriver

driver = webdriver.Firefox()
# 打开百度
url="http://47.92.220.226/bbs/"
driver.get(url)
# 找到登录的位置，点击登录
login_bt=driver.find_element_by_xpath('/html/body/nav/div/div[3]/a[1]')
login_bt.click()

# 添加数据数据
username_input = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/form/div[1]/input')
username_input.send_keys('1234@qq.com')
passwrd_input= driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/form/div[2]/input')
passwrd_input.send_keys('1111')

# 点击登录
login_bt2=driver.find_element_by_id('comm-submit')
login_bt2.click()

print (driver.current_url)
print driver.title




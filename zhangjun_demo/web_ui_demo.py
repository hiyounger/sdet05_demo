#encoding:utf-8
from selenium import webdriver
driver=webdriver.Firefox()
# driver.get('http://47.92.220.226/bbs/')
# login_bt=driver.find_element_by_xpath("/html/body/nav/div/div[3]/a[1]")
# login_bt.click()
#
# username_input=driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div/form/div[1]/input")
# username_input.send_keys("1216911016@qq.com")
# password_input=driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div/form/div[2]/input")
# password_input.send_keys("123456")
# login_bt2=driver.find_element_by_id("comm-submit")
# login_bt2.click()


driver.get("http://47.92.220.226/webdriver/index.html")
login_bt=driver.find_element_by_xpath("/html/body/a[1]")
login_bt.click()

username=driver.find_element_by_id("username")
username.send_keys("zhangjun")
password=driver.find_element_by_id("password")
password.send_keys("123456")
login_bt1=driver.find_element_by_xpath("/html/body/div[1]/button")
login_bt1.click()





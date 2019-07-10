#-*- encoding:utf-8 -*-
from selenium import webdriver

# browser=webdriver.Firefox()
# browser.get("http://www.baidu.com")

drive=webdriver.Firefox()

url="http://47.92.220.226/webdriver/findelements.html"
drive.get(url)

username=drive.find_element_by_id("username")
username.send_keys("hahahhaah")

chuqing5_1=drive.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[2]/td[2]")
chuqing5_2=drive.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[3]/td[2]")
chuqing5_3=drive.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[4]/td[2]")
chuqing5_4=drive.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[5]/td[2]")
sum_5=int(chuqing5_1.text)+int(chuqing5_2.text)+int(chuqing5_3.text)+int(chuqing5_4.text)
print sum_5

chuqing6_1=drive.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[2]/td[3]")
chuqing6_2=drive.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[3]/td[3]")
chuqing6_3=drive.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[4]/td[3]")
chuqing6_4=drive.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[5]/td[3]")
sum_6=int(chuqing6_1.text)+int(chuqing6_2.text)+int(chuqing6_3.text)+int(chuqing6_4.text)
print sum_6



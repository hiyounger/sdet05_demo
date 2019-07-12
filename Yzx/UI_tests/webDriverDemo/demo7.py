#encoding:utf-8
from selenium import webdriver
import json
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

driver= webdriver.Firefox()

url="http://www.baidu.com"
driver.get(url)
start_time=time.time()

# 根据元素定位器与元素的文字进行等待（注意：不是vale）
WebDriverWait(driver,3).until(expected_conditions.text_to_be_present_in_element((By.XPATH,u'/html/body/div[1]/div[1]/div/div[3]/a[1]'),u'新闻'))
# WebDriverWait(driver,5).until(expected_conditions.text_to_be_present_in_element((By.XPATH,u'//div[@id="ul"/a[1]'),u'新闻'))
end_time=time.time()
cost_time=start_time-end_time
print cost_time

# # 指定元素是否在页面可见
# bt=driver.find_element(By.ID,u'su')
# WebDriverWait(driver,5).until(expected_conditions.visibility_of(bt))
# # 指定定位器所代表的元素是否在页面可见
# locator=(By.ID,u'su')
# WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located(locator))
try:
    WebDriverWait(driver,3).until(expected_conditions.text_to_be_present_in_element((By.ID,u'su'),u'百度一下'))
except:
    print ("页面打开超时或未发现指定控件（%s,%s）"%("id='su'","百度一下"))



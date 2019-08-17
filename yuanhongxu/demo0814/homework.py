# coding:utf-8

from appium import webdriver
import time

desired_caps = {
    "platformName": "Android",
    "platformVersion": "6.0.1",
    "deviceName": "816a68b87d74",
    "appPackage": "com.miui.notes",
    "appActivity": ".ui.NotesListActivity"
}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(10)
el1 = driver.find_element_by_id("android:id/button1")
el1.click()
time.sleep(10)
el2 = driver.find_element_by_accessibility_id("新建便签")
el2.click()
time.sleep(10)
el3 = driver.find_element_by_id("android:id/button2")
el3.click()
time.sleep(10)
el4 = driver.find_element_by_id("com.miui.notes:id/rich_editor")
el4.send_keys("hello appium")
time.sleep(10)
el5 = driver.find_element_by_accessibility_id("返回")
el5.click()

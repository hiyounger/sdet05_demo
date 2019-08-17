# coding:utf-8
from appium import webdriver
import time

# desired_caps = {
#     "platformName": "Android",
#     "platformVersion": "6.0.1",
#     "deviceName": "816a68b87d74",
#     "appPackage": "com.miui.notes",
#     "appActivity": ".ui.NotesListActivity",
#     "unicodeKeyboard": "True",
#     "resetKeyboard": "True",
#     "automationName": "uiautomator2"
# }

desired_caps = {}
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "6.0.1"
desired_caps["deviceName"] = "816a68b87d74"
desired_caps["appPackage"] = "com.miui.notes"
desired_caps["appActivity"] = ".ui.NotesListActivity"
# desired_caps["automationName"] = "uiautomator2"
desired_caps["unicodeKeyboard"] = True
desired_caps["resetKeyboard"] = True
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(5)

ele = driver.find_element_by_id("android:id/button1")
ele.click()
time.sleep(2)

ele1 = driver.find_element_by_accessibility_id(u"新建便签")
ele1.click()
time.sleep(2)

ele2 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.Button[1]")
ele2.click()
time.sleep(2)

ele3 = driver.find_element_by_id("com.miui.notes:id/rich_editor")
ele3.send_keys(u"今天是个好日子")
time.sleep(2)

ele4 = driver.find_element_by_id("com.miui.notes:id/done")
ele4.click()
time.sleep(2)

ele5 = driver.find_element_by_id("com.miui.notes:id/home")
ele5.click()
time.sleep(2)

ele6=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView")
print (ele6.text)

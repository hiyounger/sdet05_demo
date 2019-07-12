from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
input = driver.find_element_by_id("kw")
input.send_keys("hello webdriver")
bt = driver.find_element_by_id("su")
bt.click()

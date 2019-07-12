# encoding:utf-8
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://47.92.220.226/webdriver/findelements.html')

# username_input = driver.find_element_by_id('username')
# username_input.send_keys('chenyao')
# passwd_input = driver.find_element_by_name('password')
# passwd_input.send_keys('123456')
# login_bt = driver.find_element_by_name('submit')
# login_bt.click()

# baidu_input = driver.find_element_by_xpath('/html/body/div[2]/div[1]/a')
# baidu_input.click()
# link_elements = driver.find_element_by_tag_name('a')

team05_02=driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[2]/td[2]")
team05_03=driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[3]/td[2]")
team05_04=driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[4]/td[2]")
team05_05=driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[5]/td[2]")
team05_sum=int(team05_02.text)+int(team05_03.text)+int(team05_04.text)+int(team05_05.text)
print("5月出勤天数：\n02组:%s\n03组:%s\n04组:%s\n05组:%s\n总计：%s天" %(int(team05_02.text),int(team05_03.text),int(team05_04.text),int(team05_05.text),team05_sum))
print
team06_02=driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[2]/td[3]")
team06_03=driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[3]/td[3]")
team06_04=driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[4]/td[3]")
team06_05=driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[5]/td[3]")
team06_sum=int(team06_02.text)+int(team06_03.text)+int(team06_04.text)+int(team06_05.text)
print("6月出勤天数：\n02组:%s\n03组:%s\n04组:%s\n05组:%s\n总计：%s天" %(int(team06_02.text),int(team06_03.text),int(team06_04.text),int(team06_05.text),team06_sum))



from selenium import webdriver

url = 'http://47.92.220.226/webdriver/findelements.html'
driver = webdriver.Firefox()
driver.get(url)
# days=driver.find_elements_by_tag_name('td')
# for i in days:
#     print i
days1 = driver.find_element_by_xpath('/html/body/div[3]/table/tbody/tr[2]/td[2]')
days2 =driver.find_element_by_xpath('/html/body/div[3]/table/tbody/tr[3]/td[2]')
days3 =driver.find_element_by_xpath('/html/body/div[3]/table/tbody/tr[4]/td[2]')
days4 =driver.find_element_by_xpath('/html/body/div[3]/table/tbody/tr[5]/td[2]')
print days1.text
print days2.text
print days3.text
print days4.text
print int(days1.text)+int(days2.text)+int(days3.text)+int(days4.text)
days5 = driver.find_element_by_xpath('/html/body/div[3]/table/tbody/tr[2]/td[3]')
days6 =driver.find_element_by_xpath('/html/body/div[3]/table/tbody/tr[3]/td[3]')
days7 =driver.find_element_by_xpath('/html/body/div[3]/table/tbody/tr[4]/td[3]')
days8 =driver.find_element_by_xpath('/html/body/div[3]/table/tbody/tr[5]/td[3]')
print days5.text
print days6.text
print days7.text
print days8.text
print int(days5.text)+int(days6.text)+int(days7.text)+int(days8.text)



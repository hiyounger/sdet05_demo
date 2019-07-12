# encoding:utf-8
from selenium import webdriver

driver = webdriver.Firefox()
url = "https://47.92.220.226/webdriver/findelements.html"

driver.get(url)
scort_table1 = driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[2]/td[2]")
print  scort_table1.text
scort_table2 = driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[2]/td[3]")
print scort_table2.text

scort_table3 = driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[3]/td[2]")
print scort_table3.text
scort_table4 = driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[3]/td[3]")
print scort_table4.text

scort_table5 = driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[4]/td[2]")
print scort_table5.text
scort_table6 = driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[4]/td[3]")
print scort_table6.text

scort_table7 = driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[5]/td[2]")
print scort_table7.text
scort_table8 = driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[5]/td[3]")
print scort_table8.text

may_table = int(scort_table1.text)+int(scort_table3.text)+int(scort_table5.text)+int(scort_table7.text)
print may_table

june_table = int(scort_table2.text)+int(scort_table4.text)+int(scort_table6.text)+int(scort_table8.text)
print june_table

#drive.find_element_by_xpath()
#drive.find_element_by_name()
#drive.find_element_by_class_name()
#drive.find_element_by_css_selector()
#drive.find_element_by_link_text()
#drive.find_element_by_partial_text()

id_element=driver.find_element_by_id("table")
print id_element.text


# encoding:utf-8

from selenium import webdriver

driver = webdriver.Firefox()

url = "http://47.92.220.226/webdriver/findelements.html"
driver.get(url)

number1=driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[2]/td[2]")

number2=driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[3]/td[2]")

number3=driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[4]/td[2]")

number4=driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[5]/td[2]")
and_member=(int(number1.text)+int(number2.text)+int(number3.text)+int(number4.text))

number5=driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[2]/td[3]")

number6=driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[3]/td[3]")

number7=driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[4]/td[3]")

number8=driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[5]/td[3]")
and_member1=(int(number5.text)+int(number6.text)+int(number7.text)+int(number8.text))
print "五月出勤总天数为：%s"%(and_member)
print "六月出勤总天数为：%s"%(and_member1)



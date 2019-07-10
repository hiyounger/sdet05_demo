 # coding:utf-8
from selenium import webdriver

driver=webdriver.Firefox()
url='http://47.92.220.226/webdriver/findelements.html'
driver.get(url)



May_group2=driver.find_element_by_xpath('/html/body/div[3]/table/tbody/tr[2]/td[2]')
b1=int(May_group2.text)
print b1

May_group3=driver.find_element_by_xpath('/html/body/div[3]/table/tbody/tr[3]/td[2]')
b2=int(May_group3.text)
print b2

May_group4=driver.find_element_by_xpath('/html/body/div[3]/table/tbody/tr[4]/td[2]')
b3=int(May_group4.text)
print b3

May_group5=driver.find_element_by_xpath('/html/body/div[3]/table/tbody/tr[5]/td[2]')
b4=int(May_group5.text)
print b4

May_sum=b1+b2+b3+b4
print May_sum
print

June_group2=driver.find_element_by_xpath('/html/body/div[3]/table/tbody/tr[2]/td[3]')
a1=int(June_group2.text)
print a1

June_group3=driver.find_element_by_xpath('/html/body/div[3]/table/tbody/tr[3]/td[3]')
a2=int(June_group3.text)
print a2

June_group4=driver.find_element_by_xpath('/html/body/div[3]/table/tbody/tr[4]/td[3]')
a3=int(June_group4.text)
print a3

June_group5=driver.find_element_by_xpath('/html/body/div[3]/table/tbody/tr[5]/td[3]')
a4=int(June_group5.text)
print a4

June_sum=a1+a2+a3+a4
print June_sum

# login_bt=driver.find_element_by_xpath("/html/body/nav/div/div[3]/a[1]")
# login_bt.click()
#
# input_name=driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div/form/div[1]/input")
# input_name.send_keys('wangyunfei@ovc1024.cn')
#
# input_password=driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div/form/div[2]/input")
# input_password.send_keys(123456)
#
# login_bt2=driver.find_element_by_xpath('//*[@id="comm-submit"]')
# login_bt2.click()



# print (driver.current_url)
# print (driver.title)

#encoding:utf-8

from selenium import  webdriver
driver=webdriver.Firefox()

url="http://47.92.220.226/webdriver/findelements.html"
driver.get(url)

#根据id查找元素
username_imput=driver.find_element_by_id("table")
#输出表格中的数据
print username_imput.text
#通过标签查找
tag_elements=driver.find_elements_by_tag_name("td")
sum=int(tag_elements[4].text)+int(tag_elements[7].text)+int(tag_elements[10].text)+int(tag_elements[13].text)
print "5月总和:%r"%(sum)
sum=int(tag_elements[5].text)+int(tag_elements[8].text)+int(tag_elements[11].text)+int(tag_elements[14].text)
print "6月总和:%r"%(sum)

# 通过xpath查找
# xpath_element=driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[1]/td[2]")
# print xpath_element
# name_element=driver.find_element_by_name("div1input")
# print name_element
# class_element=driver.find_element_by_class_name()
# css_element=driver.find_element_by_css_selector()
# link_element=driver.find_element_by_link_text()
# partial_element=driver.find_element_by_partial_link_text()



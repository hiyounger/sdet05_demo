#encoding:utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import json
import time
#指定浏览器
driver=webdriver.Firefox()
#获取地址
driver.get('http://47.92.220.226/webdriver/index.html')
#相对定位
# eles_aTag=driver.find_element_by_xpath("//ul/li[1]/a")
# eles_aTag.click()
#
# #查找定位
# # eles_aTag=driver.find_elements_by_tag_name(u"a")
# # eles_locationTest=None
# # for element in eles_aTag:
# #     if element.text==u"定位方法测试页面":
# #         eles_locationTest=element
# #         break
# # eles_locationTest.click()
#
# #A标签文字定位
# # eles_aTag=driver.find_element_by_link_text(u"定位方法测试页面")
# # eles_aTag.click()
#
# #A标签部分文字定位
# # eles_aTag=driver.find_element_by_partial_link_text(u"定位方法")
# # eles_aTag.click()
# #通过id定位
# username=driver.find_element_by_id(u"username")
# username.send_keys(u"zhangjun")
#
# useremail=driver.find_element_by_name(u"email")
# useremail.send_keys(u"487296792@qq.com")
#
# userpassword=driver.find_element_by_xpath(u'//*[@id="password"]')
# userpassword.send_keys(u"123456")
#
# confirm_password=driver.find_element_by_css_selector(u"#confirm_password")
# confirm_password.send_keys(u"123456")
#
# register=driver.find_element_by_xpath(u"//td[@colspan='2']/input[1]")
# register.click()
#
# #查询注册信息
# regmsg=driver.find_element_by_id(u"regmsg")
# regmsg_text=regmsg.text
# regmsg_json=json.loads(regmsg_text.split(u'成功:')[-1],encoding='utf-8')
# print ("uid:%s" % regmsg_json['uid'])
# print ("username:%s" % regmsg_json['username'])
# print ("password:%s" % regmsg_json['password'])
# print ("email:%s" % regmsg_json['email'])
#
# #根据id查询
# serch=driver.find_element_by_xpath(u'//*[@id="search_uid"]')
# serch.send_keys(u"0")
# serch_bt=driver.find_element_by_xpath(u"//div[2]/div[1]/input[2]")
# serch_bt.click()
# search_msg=driver.find_element_by_id(u'search_msg')
# search_msg_text=search_msg.text
# search_msg_json=json.loads(search_msg_text,encoding='utf-8')
# print ("uid:%s" % search_msg_json['uid'])
# print ("username:%s" % search_msg_json['username'])
# print ("password:%s" % search_msg_json['password'])
# print ("email:%s" % search_msg_json['email'])
#
# #根据用户名查询
# # serch=driver.find_element_by_xpath(u'//*[@id="search_uname"]')
# # serch.send_keys(u"zhangjun")
# # serch_bt1=driver.find_element_by_xpath(u"//div[2]/div[2]/input[2]")
# # serch_bt1.click()
# # search_msg=driver.find_element_by_id(u'search_msg')
# # search_msg_text=search_msg.text
# # search_msg_json=json.loads(search_msg_text,encoding='utf-8')
# # print ("uid:%s" % search_msg_json['uid'])
# # print ("username:%s" % search_msg_json['username'])
# # print ("password:%s" % search_msg_json['password'])
# # print ("email:%s" % search_msg_json['email'])
#
# #根据邮箱查询
# serch=driver.find_element_by_xpath(u'//*[@id="search_email"]')
# serch.send_keys(u"487296792@qq.com")
# serch_bt2=driver.find_element_by_xpath(u"//div[2]/div[3]/input[2]")
# serch_bt2.click()
# search_msg=driver.find_element_by_id(u'search_msg')
# search_msg_text=search_msg.text
# search_msg_json=json.loads(search_msg_text,encoding='utf-8')
# print ("uid:%s" % search_msg_json['uid'])
# print ("username:%s" % search_msg_json['username'])
# print ("password:%s" % search_msg_json['password'])
# print ("email:%s" % search_msg_json['email'])
#
# #双重调用
# ele_table=driver.find_element_by_id(u"table")
# ele_table_trs=ele_table.find_elements_by_tag_name(u"tr")
# May=[]
# June=[]
# for i in range(len(ele_table_trs)):
#     if i==0:
#         continue
#     else:
#         tds=ele_table_trs[i].find_elements_by_tag_name(u"td")
#         for j in range(len(tds)):
#             if j==1:
#                 May.append(tds[j].text)
#             elif j==2:
#                 June.append(tds[j].text)
#             else:
#                 continue
# print (May)
# print(June)





#返回首页
# ret_index=driver.find_element_by_link_text(u"返回首页")
# ret_index.click()
driver.back()
ele_opt=driver.find_element_by_xpath(u"//ul/li[2]/a")
ele_opt.click()

# text_input=driver.find_element_by_xpath(u'//*[@id="1_1"]')
# text_input.send_keys(u"zhangjun")
# text_bt=driver.find_element_by_xpath(u'/html/body/div[1]/div[1]/input[2]')
# text_bt.click()
# text1=driver.find_element_by_id(u'//*[@id="1_1_msg"]')
# text1_text=text1.text
# text1_json=json.loads(text1_text.split(u'输入的值为:')[-1],encoding='utf-8')
# print (text1_json)

#下拉框
ele_select=Select(driver.find_element_by_id(u'fruit'))
print ele_select.first_selected_option.text

ele_options=ele_select.options
print ele_options[2].text
print len(ele_options)

for i in ele_options:
    print i.text

ele_select.select_by_index(2)
time.sleep(1)
ele_select.select_by_value(u"lizhi")
time.sleep(1)
ele_select.select_by_visible_text(u"猕猴桃")

#单选框
ele_button=driver.find_elements_by_name(u'fruit')
for button in ele_button:
    if button.get_attribute(u"value")==u"berry":
        button.click()
    print("value:%s,is_selected:%s"%(button.get_attribute("value"),button.is_selected()))

#复选框


#隐藏
ele_div1=driver.find_element_by_id(u"div1")
ele_div2=driver.find_element_by_id(u"div2")
print ("If div1 display:%s"%ele_div1.is_displayed())
print ("If div2 display:%s"%ele_div2.is_displayed())

driver.find_element_by_id(u"button1").click()

print ("If div1 display:%s"% ele_div1.is_displayed())
print ("If div2 display:%s"% ele_div2.is_displayed())

ele_enable_input=driver.find_element_by_xpath(u"//div[3]/div[1]/input")
print ("ele_enable_input is enable :%s"% ele_enable_input.is_enabled())

ele_disnable_input=driver.find_element_by_xpath(u"//div[3]/div[2]/input")
print ("ele_disnable_input is enable :%s"% ele_disnable_input.is_enabled())

#点击变色
ele_doubleClick=driver.find_element_by_id(u"context_click")
action_chains=ActionChains(driver)
action_chains.double_click(ele_doubleClick).perform()
print (ele_doubleClick.get_attribute("style"))


#弹窗
#Alert弹窗
ele_alert=driver.find_element_by_xpath(u"//div[5]/div/input[1]")
ele_alert.click()
alert=driver.switch_to.alert
print ("Alter text:%s" % alert.text)
time.sleep(2)
alert.accept()

#confirm弹窗
ele_confirm=driver.find_element_by_xpath(u"//div[5]/div/input[2]")
ele_confirm.click()
confirm = driver.switch_to.alert
print ("Confirm text:%s" % confirm.text)
time.sleep(2)
confirm.accept()
# confirm.dismiss()
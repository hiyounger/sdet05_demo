# coding:utf-8
from selenium import webdriver
import time
import json
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
# 1、 初始化
driver = webdriver.Firefox()

# 2、打开页面
url = "http://47.92.220.226/webdriver/"
driver.get(url)

# 3、定位（定位方法测试页面）页面元素
# 3.1、使用标签定位
# eles_aTag=driver.find_elements_by_tag_name(u"a")
# ele_Tag=None
# for element in eles_aTag:
#     if element.text == u"定位方法测试页面":
#         ele_Tag=element
#         break
#
# time.sleep(5)
# ele_Tag.click()

# 3.2、使用Xpath相对定位
# ele_locationg=driver.find_element_by_xpath('//ul/li[1]/a')
# ele_locationg.click()
# time.sleep(5)

# 3.3、使用link_text定位
# 全部
# ele_locationg=driver.find_element_by_link_text(u'定位方法测试页面')
# ele_locationg.click()

# 部分
# ele_locationg=driver.find_element_by_partial_link_text(u'定位方法')
# ele_locationg.click()

# 部分
# ele_locationg = driver.find_elements_by_partial_link_text(u'页面')
# ele_Tag = None
# for element in ele_locationg:
#     if element.text == u"定位方法测试页面":
#         ele_Tag = element
#         break
# ele_Tag.click()

# ================================用户注册
# 当前在定位方法测试页面
# 通过by_id的方法定位输入框，并输入值
# ele_username = driver.find_element_by_id(u'username')
# ele_username.send_keys(u'汪')
#
# ele_email = driver.find_element_by_name(u'email')
# ele_email.send_keys(u'wang@qq.com')
#
# ele_password = driver.find_element_by_xpath(u'//*[@id="password"]')
# ele_password.send_keys(u'123456')
#
# ele_password_enter = driver.find_element_by_css_selector(u'#confirm_password')
# ele_password_enter.send_keys(u'123456')
#
# ele_register_bt = driver.find_element_by_xpath(u"//td[@colspan='2']/input[1]")
# ele_register_bt.click()

# ele_result=driver.find_element_by_id(u'regmsg')
# print ele_result.text

# =====================用户查询
# 通过id查
# ele_select_id=driver.find_element_by_id(u"search_uid")
# ele_select_id.send_keys(u'0')
#
# ele_retmsg=driver.find_element_by_xpath(u'/html/body/div[2]/div[1]/input[2]')
# ele_retmsg.click()
#
# ele_result=driver.find_element_by_xpath(u'//*[@id="search_msg"]')
# retmsg_text=ele_result.text
# retmsg_json=json.loads(retmsg_text.split(u'成功:')[-1],encoding='utf-8')
# print ("uid:%s"% retmsg_json['uid'])
# print ("username:%s"% retmsg_json['username'])
# print ("password:%s"% retmsg_json['password'])
# print ("email:%s"% retmsg_json['email'])

# 通过用户名查
# ele_select_username=driver.find_element_by_id(u"search_uname")
# ele_select_username.send_keys(u'汪')
#
# ele_retmsg=driver.find_element_by_xpath(u'/html/body/div[2]/div[2]/input[2]')
# ele_retmsg.click()
#
# ele_result=driver.find_element_by_xpath(u'//*[@id="search_msg"]')
# retmsg_text=ele_result.text
# retmsg_json=json.loads(retmsg_text,encoding='utf-8')
# print ("uid:%s"% retmsg_json['uid'])
# print ("username:%s"% retmsg_json['username'])
# print ("password:%s"% retmsg_json['password'])
# print ("email:%s"% retmsg_json['email'])

# 通过邮箱查询
# ele_select_email=driver.find_element_by_id(u"search_email")
# ele_select_email.send_keys(u'wang@qq.com')
#
# ele_retmsg=driver.find_element_by_xpath(u'/html/body/div[2]/div[3]/input[2]')
# ele_retmsg.click()
#
# ele_result=driver.find_element_by_xpath(u'//*[@id="search_msg"]')
# retmsg_text=ele_result.text
# retmsg_json=json.loads(retmsg_text,encoding='utf-8')
# print retmsg_text
# print ("uid:%s"% retmsg_json['uid'])
# print ("username:%s"% retmsg_json['username'])
# print ("password:%s"% retmsg_json['password'])
# print ("email:%s"% retmsg_json['email'])

# ============================
# 获取列表的值
# ele_table=driver.find_element_by_id(u'table')
# ele_trs=ele_table.find_elements_by_tag_name(u'tr')
# May=[]
# June=[]
# May_sum=0
# June_sum=0
# for i in range(len(ele_trs)):
#     if i==0:
#         continue
#     else:
#         tds=ele_trs[i].find_elements_by_tag_name(u'td')
#         for j in range(len(tds)):
#             if j==1:
#                 May.append(tds[j].text)
#                 May_sum+=int(tds[j].text)
#             elif j==2:
#                 June.append(tds[j].text)
#                 June_sum+=int(tds[j].text)
#             else:
#                 continue
# print May
# print June
# print ('五月出勤总天数为:%s'%May_sum)
# print ('六月出勤总天数为:%s'%June_sum)
# # 返回上一级
# driver.back()


# ===============================
# 点击进入‘页面元素操作练习’页面
ele_opyTest=driver.find_element_by_link_text(u'页面元素操作练习')
ele_opyTest.click()

ele_text_input=driver.find_element_by_id(u'1_1')
ele_text_input.send_keys(u'123')
ele_t_input=driver.find_element_by_xpath(u'/html/body/div[1]/div[1]/input[2]')
ele_t_input.click()
ele_label_text=driver.find_element_by_id(u'1_1_msg')
print ele_label_text.text
print

ele_password_input=driver.find_element_by_id(u'1_2')
ele_password_input.send_keys(u'123')
ele_p_input=driver.find_element_by_xpath(u'/html/body/div[1]/div[2]/input[2]')
ele_p_input.click()
ele_label_password=driver.find_element_by_id(u'1_2_msg')
print ele_label_password.text
print

ele_email_input=driver.find_element_by_id(u'1_3')
ele_email_input.send_keys(u'123@qq.com')
ele_e_input=driver.find_element_by_xpath(u'/html/body/div[1]/div[3]/input[2]')
ele_e_input.click()
ele_label_email=driver.find_element_by_id(u'1_3_msg')
print ele_label_email.text

# 选择列表栏
ele_select=Select(driver.find_element_by_id(u'fruit'))
# 获取当前所选项
print  ele_select.first_selected_option.text
print

# 获取所有可选项
print  len(ele_select.options)
for opt in  ele_select.options:
    print opt.text
print

# 选择指定项
ele_select.select_by_index(2)

print
time.sleep(1)
ele_select.select_by_value(u'xigua')

print
time.sleep(1)
ele_select.select_by_visible_text(u'猕猴桃')

time.sleep(1)

# 单选
ele_radiobts=driver.find_elements_by_name(u'fruit')
for radio in ele_radiobts:
    if radio.get_attribute(u'value')==u'watermelon':
        radio.click()
    print ('value:%s,is_selected:%s'%( radio.get_attribute(u'value'),radio.is_selected()))
print
# 多选
ele_radio_bts=driver.find_elements_by_name(u'fruit2')
for radios in ele_radio_bts:
    if radios.get_attribute(u'value')==u'watermelon,orange':
        radios.click()
    print ('value:%s,is_selected:%s' % (radios.get_attribute(u'value'), radios.is_selected()))
# 可见不可见
ele_div1=driver.find_element_by_id(u'div1')
ele_div2=driver.find_element_by_id(u'div2')
print('if div1 displayed:%s'%ele_div1.is_displayed())
print('if div2 displayed:%s'%ele_div2.is_displayed())
driver.find_element_by_xpath(u'//*[@id="button1"]').click()
print
print('if div1 displayed:%s'%ele_div1.is_displayed())
print('if div2 displayed:%s'%ele_div2.is_displayed())

print

ele_enable_input=driver.find_element_by_xpath(u'//div[3]/div[1]/input')
print ('ele_enable_input if enable:%s'%ele_enable_input.is_enabled())

print

ele_disable_input=driver.find_element_by_xpath(u'//div[3]/div[2]/input')
print ('ele_enable_input if enable:%s'%ele_disable_input.is_enabled())


# 双击按钮
ele_double=driver.find_element_by_xpath(u'//*[@id="context_click"]')
action_chains=ActionChains(driver)
action_chains.double_click(ele_double).perform()
print ("style:%s"%ele_double.get_attribute(u'style'))

# 弹窗alert
ele_alerbt=driver.find_element_by_xpath(u'/html/body/div[5]/div/input[1]')
ele_alerbt.click()
alert=driver.switch_to.alert
print ('Alert text:%s'%alert.text)
time.sleep(2)
alert.accept()

# confirm
ele_confirmbt=driver.find_element_by_xpath(u'/html/body/div[5]/div/input[2]')
ele_confirmbt.click()
confirm=driver.switch_to.confirm
print ('Confirm text:%s'%confirm.text)
time.sleep(2)
confirm.dismiss()





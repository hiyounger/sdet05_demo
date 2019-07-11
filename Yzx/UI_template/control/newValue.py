#encoding:utf-8
from selenium import webdriver
import json
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
driver= webdriver.Firefox()

url="http://47.92.220.226/webdriver/"
driver.get(url)
# 各种定位方式
# eles=driver.find_element_by_link_text(u'定位方法测试页面')
# eles.click()
eles = driver.find_element_by_partial_link_text(u'测试页面')
eles.click()

input_name=driver.find_element_by_id(u'username')
input_name.send_keys(u'yanzhenxing')
input_email=driver.find_element_by_name(u'email')
input_email.send_keys(u'1234@qq.com')
# input_password=driver.find_elements_by_class_name(u'login_input')[2]
# input_password.send_keys(u'1233')
input_password=driver.find_element_by_id(u'password')
input_password.send_keys('1233')
input_twopwd=driver.find_element_by_css_selector(u'#confirm_password')
input_twopwd.send_keys(u'1233')
denglu=driver.find_element_by_xpath(u'//td[@colspan]/input[1]')
denglu.click()

ele_regmsg = driver.find_element_by_id(u"regmsg")
regmsg_text = ele_regmsg.text
regmsg_json = json.loads(regmsg_text.split(u"成功:")[-1], encoding='utf-8')
print("uid: %s" % regmsg_json['uid'])
print("username: %s" % regmsg_json['username'])
print("password: %s" % regmsg_json['password'])
print("email: %s" % regmsg_json['email'])

elems=driver.find_element_by_id(u'search_uid')
elems.send_keys('0')
ele_search_id=driver.find_element_by_xpath(u'/html/body/div[2]/div[1]/input[2]')
ele_search_id.click()
seacher=driver.find_element_by_id(u'search_msg')
seacher_text_uid = seacher.text
print seacher_text_uid
seacher_text_uid_json=json.loads(seacher_text_uid)
print("uid: %s" % seacher_text_uid_json[u'uid'])
print("username: %s" % seacher_text_uid_json[u'username'])
print("password: %s" % seacher_text_uid_json[u'password'])
print("email: %s" % seacher_text_uid_json[u'email'])


elems1=driver.find_element_by_id(u'search_uname')
elems1.send_keys('yanzhenxing')
ele_search_name=driver.find_element_by_xpath(u'/html/body/div[2]/div[2]/input[2]')
ele_search_name.click()
seacher_name=driver.find_element_by_id(u'search_msg')
seacher_name_text = seacher_name.text
seacher_text_name_json=json.loads(seacher_name_text)
print("uid: %s" % seacher_text_name_json[u'uid'])
print("username: %s" % seacher_text_name_json[u'username'])
print("password: %s" % seacher_text_name_json[u'password'])
print("email: %s" % seacher_text_name_json[u'email'])

elems2=driver.find_element_by_id(u'search_email')
elems2.send_keys('1234@qq.com')
ele_search_email=driver.find_element_by_xpath(u'/html/body/div[2]/div[3]/input[2]')
ele_search_email.click()
seacher_text_email=driver.find_element_by_id(u'search_msg')
seacher_text_email_text = seacher_text_email.text
seacher_text_email_text_json=json.loads(seacher_text_email_text)
print("uid: %s" % seacher_text_email_text_json['uid'])
print("username: %s" % seacher_text_email_text_json['username'])
print("password: %s" % seacher_text_email_text_json['password'])
print("email: %s" % seacher_text_email_text_json['email'])
# 多重定位
ele_table=driver.find_element_by_id(u'table')
ele_table_trs=ele_table.find_elements_by_tag_name(u'tr')
may=[]
june=[]
for i in range(len(ele_table_trs)):
    if i==0:
        continue
    else:
        tds=ele_table_trs[i].find_elements_by_tag_name(u'td')
        for j in range(len(tds)):
            if j==1:
                may.append(tds[j].text)
            elif j==2:
                june.append(tds[j].text)
            else:
                continue
print may
print june
may_sum=0
june_sum=0
for m in may:
    may_sum+=int(m)
for j in june:
    june_sum+=int(j)
print may_sum
print  june_sum


driver.back()
ele_optationTest=driver.find_element_by_link_text(u'页面元素操作练习')
ele_optationTest.click()
# 文本框
ele_by_id1_1=driver.find_element_by_id(u'1_1')
ele_by_id1_1.send_keys(u'1214')
ele_by_id1_1_click=driver.find_element_by_xpath(u'/html/body/div[1]/div[1]/input[2]')
ele_by_id1_1_click.click()
ele_1_1_msg=driver.find_element_by_id(u'1_1_msg')
print ele_1_1_msg.text

ele_by_id1_2=driver.find_element_by_id(u'1_2')
ele_by_id1_2.send_keys(u'12141221331')
ele_by_id1_2_click=driver.find_element_by_xpath(u'/html/body/div[1]/div[2]/input[2]')
ele_by_id1_2_click.click()
ele_1_2_msg=driver.find_element_by_id(u'1_2_msg')
print ele_1_2_msg.text

ele_by_id1_3=driver.find_element_by_id(u'1_3')
ele_by_id1_3.send_keys(u'1214@qq.com')
ele_by_id1_3_click=driver.find_element_by_xpath(u'/html/body/div[1]/div[3]/input[2]')
ele_by_id1_3_click.click()
ele_1_3_msg=driver.find_element_by_id(u'1_3_msg')
print ele_1_3_msg.text

# 下拉表格
ele_select=Select(driver.find_element_by_id(u'fruit'))
print ele_select.first_selected_option.text
ele_select_text=ele_select.options
print ele_select_text[2].text
print len(ele_select_text)
for opt in ele_select_text:
    print opt.text

ele_select.select_by_index(2)
time.sleep(1)
ele_select.select_by_value(u'mihoutao')
time.sleep(1)
ele_select.select_by_visible_text(u'荔枝')
time.sleep(1)
# 单选按钮操作
ele_radiobts=driver.find_elements_by_name(u'fruit')
for ele in ele_radiobts:
    if ele.get_attribute(u'value')==u'berry':
        ele.click()
    print ('value :%s ,is_selected :%s'%(ele.get_attribute(u'value'),ele.is_selected()))

# 复选按钮操作
ele_checkboxbts=driver.find_elements_by_name(u'fruit2')
for ele in ele_checkboxbts:
    # if ele.get_attribute(u'value')==u'watermelon':
    ele.click()
    print ('value :%s ,is_selected :%s'%(ele.get_attribute(u'value'),ele.is_selected()))
# div 分层显示
ele_div1=driver.find_element_by_id(u'div1')
ele_div2=driver.find_element_by_id(u'div2')
print ("If div1 display: %s"%ele_div1.is_displayed())
print ("If div2 display: %s"%ele_div2.is_displayed())
ele_enable_input=driver.find_element_by_id('button1').click()
print ("If div1 display: %s"%ele_div1.is_displayed())
print ("If div2 display: %s"%ele_div2.is_displayed())
# 可用不可用
ele_enable_input =driver.find_element_by_xpath(u'//div[3]/div[1]/input')
print("ele_enable_input if enabled: %s"%ele_enable_input.is_enabled())
ele_disenable_input =driver.find_element_by_xpath(u'//div[3]/div[2]/input')
print("ele_disenable_input if enabled: %s"%ele_disenable_input.is_enabled())
# 双击变红操作
ele_double_clickbt=driver.find_element_by_id(u"context_click")
action_chains=ActionChains(driver)
action_chains.double_click(ele_double_clickbt).perform()
print (ele_double_clickbt.get_attribute('style'))
#alter
ele_alter=driver.find_element_by_xpath('//div[5]/div/input[1]')
ele_alter.click()
alter=driver.switch_to.alert
print ('Alert text:%s'%alter.text)
time.sleep(1)
alter.accept()
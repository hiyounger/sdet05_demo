# encoding:utf-8

from selenium import webdriver
import json
import time

driver = webdriver.Firefox()

url = "http://47.92.220.226/webdriver/index.html"
driver.get(url)
# eles_aTag = driver.find_elements_by_tag_name(u"a")
# ele_locationtest = None
# for element in eles_aTag:
#     if element.text == u"定位方法测试页面":
#         ele_locationtest = element
#         break
# ele_locationtest.click()

# ele_locationTest=driver.find_element_by_xpath('//html/body/ul/li[1]/a')
# ele_locationTest.click()

ele_locationTest = driver.find_element_by_link_text(u"定位方法测试页面")
ele_locationTest.click()
# ele_locationTest = driver.find_element_by_partial_link_text(u"定位方法")
# ele_locationTest.click()

#---------------------------------------------------------
# ele_username = driver.find_element_by_id(u"username")
# ele_username.send_keys(u"chenguanxi")
#
# ele_email = driver.find_element_by_name(u"email")
# ele_email.send_keys(u"1286060621@qq.com")
#
# ele_password = driver.find_elements_by_class_name(u"login_input")[2]
# ele_password.send_keys(u"123456")
#
# ele_confirm_pwd = driver.find_element_by_css_selector(u"#confirm_password")
# ele_confirm_pwd.send_keys(u"123456")
#
# ele_login = driver.find_element_by_xpath(u"/html/body/div[1]/form/table/tbody/tr[5]/td/input[1]")
# ele_login.click()
#
# ele_regmsg = driver.find_element_by_id(u"regmsg")
# regmsg = ele_regmsg.text
# regmsg_json = json.loads(regmsg.split(u"成功:")[-1], encoding = 'utf-8')
#
# print "uid:%s"% regmsg_json['uid']
# print "username:%s"% regmsg_json['username']
# print "password:%s"% regmsg_json['password']
# print "email:%s"% regmsg_json['email']
#
# ele_id1 = driver.find_element_by_id(u"search_uid")
# ele_id1.send_keys(u"0")
#
# ele_button_login1 = driver.find_element_by_xpath(u"/html/body/div[2]/div[1]/input[2]")
# ele_button_login1.click()
#
# ele_search_msg = driver.find_element_by_id(u"search_msg")
# msg = ele_search_msg.text
# msg_json = json.loads(msg)
#
# print "uid:%s\nusername:%s\npassword:%s\nemail:%s"%(msg_json['uid'],msg_json['username'],msg_json['password'],msg_json['email'])
#
# ele_id2 = driver.find_element_by_id(u"c")
# ele_id2.send_keys(u"chenguanxi")
#
# ele_button_login2 = driver.find_element_by_xpath(u"/html/body/div[2]/div[2]/input[2]")
# ele_button_login2.click()
#
# ele_search_user = driver.find_element_by_id(u"search_msg")
# msg1 = ele_search_user.text
# msg1_json = json.loads(msg1)
#
# print "uid:%s\nusername:%s\npassword:%s\nemail:%s"%(msg1_json['uid'],msg1_json['username'],msg1_json['password'],msg1_json['email'])
#
#
# ele_id3 = driver.find_element_by_id(u"csearch_email")
# ele_id3.send_keys(u"1286060621@qq.com")
#
# ele_button_login3 = driver.find_element_by_xpath(u"/html/body/div[2]/div[3]/input[2]")
# ele_button_login3.click()
#
# ele_search_email = driver.find_element_by_id(u"search_msg")
# msg2 = ele_search_email.text
# msg2_json = json.loads(msg2)
#
# print "uid:%s\nusername:%s\npassword:%s\nemail:%s"%(msg2_json['uid'],msg2_json['username'],msg2_json['password'],msg2_json['email'])

ele_table = driver.find_element_by_id('table')
ele_table_trs = ele_table.find_elements_by_tag_name('tr')
may = []
june = []
for i in range(len(ele_table_trs)):
    if i == 0:
        continue
    else:
        tds = ele_table_trs[i].find_elements_by_tag_name('td')
        for j in range(len(tds)):
                if j == 1:
                    may.append(tds[j].text)
                elif j == 2:
                    june.append(tds[j].text)
                else:
                    continue
print may
print june
may_sum = 0
june_sum = 0

for i in may:
    may_sum += int(i)
for i in june:
    june_sum += int(i)
print may_sum
print june_sum

driver.back()

ele_optTest = driver.find_element_by_link_text(u"页面元素操作练习")
ele_optTest.click()

# ele_txt = driver.find_element_by_id(u'1_1')
# ele_txt.send_keys("hahaha")
#
# ele_txt_login = driver.find_element_by_id(u"1_1_msg")
# regmsg = ele_txt_login.text
# regmsg_json = json.loads(regmsg.split(u"值为:")[-1], encoding = 'utf-8')
# print regmsg_json.text
#
# ele_txt = driver.find_element_by_id(u'1_1')
# ele_txt.send_keys("hahaha")
#
# ele_txt_login = driver.find_element_by_id(u"1_1_msg")
# regmsg= ele_txt_login.text
# regmsg_json = json.loads(regmsg.split(u"值为:")[-1], encoding = 'utf-8')
# print regmsg_json.text


# from selenium.webdriver.support.ui import Select
#
# ele_select = Select(driver.find_element_by_id(u'fruit'))
# print ele_select.first_selected_option.text
#
# ele_options = ele_select.options
# print ele_options[2].text
# print  len(ele_options)
# for opt in ele_options:
#     print opt.text
#
# ele_select.select_by_index(2)
# time.sleep(3)
# ele_select.select_by_value(u'mihoutao')
# time.sleep(3)
# ele_select.select_by_visible_text(u"荔枝")
#
#
#
#
# ele_radiobts = driver.find_elements_by_name(u"fruit")
# for radiobt in ele_radiobts:
#     if radiobt.get_attribute(u"value") == u"berry":
#         radiobt.click()
#     print "value:%s  ,  is_selected:%s"%(radiobt.get_attribute('value'),radiobt.is_selected())
#
# ele_checkbox = driver.find_elements_by_name(u"fruit2")
# for checkbox in ele_checkbox:
#     if checkbox.get_attribute("value") == u"berry":
#         checkbox.click()
#     elif checkbox.get_attribute("value") == u"watermelon":
#             checkbox.click()
#     elif checkbox.get_attribute("value") == u"orange":
#                 checkbox.click()
#     print "value:%s  ,  is_selected:%s" % (checkbox.get_attribute('value'), checkbox.is_selected())

ele_div1 = driver.find_element_by_id("div1")
ele_div2 = driver.find_element_by_id("div2")
print "If div1 displayed:%s"%(ele_div1.is_displayed())
print "If div2 displayed:%s"%(ele_div2.is_displayed())

driver.find_element_by_id(u"button1").click()
print "If div1 displayed:%s"%(ele_div1.is_displayed())
print "If div2 displayed:%s"%(ele_div2.is_displayed())

ele_enable_input = driver.find_element_by_xpath('/html/body/div[3]/div[1]/input')
print "ele_enable_input if enable:%s"% ele_enable_input.is_enabled()

ele_disable_input = driver.find_element_by_xpath('/html/body/div[3]/div[2]/input')
print "ele_disable_input if enable:%s"% ele_disable_input.is_enabled()

from selenium.webdriver import ActionChains
ele_doublebt = driver.find_element_by_id("context_click")
action_chains = ActionChains(driver)
action_chains.double_click(ele_doublebt).perform()
print ele_doublebt.get_attribute("style")

ele_alertbt = driver.find_element_by_xpath("//div[5]/div/input[1]")
ele_alertbt.click()
alert = driver.switch_to.alert
print "Alert text:%s"% alert.text
time.sleep(2)
alert.accept()

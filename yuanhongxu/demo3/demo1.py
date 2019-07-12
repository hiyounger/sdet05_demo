# -*- encoding:utf-8 -*-

from selenium import webdriver
import json
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver import ActionChains

drive = webdriver.Firefox()

url = "http://47.92.220.226:8000/webdriver/"
drive.get(url)

# tag_a=drive.find_elements_by_tag_name(u"a")
# ele_loginTest=None
# for a in tag_a:
#     if a.text==u"定位方法测试页面":
#         ele_loginTest=a
#         break
# ele_loginTest.click()

# ele_loginTest=drive.find_element_by_xpath("//ul/li[1]/a")
# ele_loginTest.click()

# ele_loginTest=drive.find_element_by_link_text(u"定位方法测试页面")
# ele_loginTest.click()
ele_loginTest = drive.find_element_by_partial_link_text(u"定位方法")
ele_loginTest.click()

# =============================================================
ele_username = drive.find_element_by_id(u"username")
ele_username.send_keys(u"yuan")

ele_mail = drive.find_element_by_name(u"email")
ele_mail.send_keys(u"yuan@qq.com")

ele_password = drive.find_elements_by_class_name(u"login_input")[2]
ele_password.send_keys(u"yuan123")

ele_confirmpwd = drive.find_element_by_css_selector(u"#confirm_password")
ele_confirmpwd.send_keys(u"yuan123")

ele_regest_bt = drive.find_element_by_xpath(u"//td[@colspan=2]/input[1]")
ele_regest_bt.click()

ele_regmsg = drive.find_element_by_id(u"regmsg")
ele_regmsg_text = ele_regmsg.text
return_msg = json.loads(ele_regmsg_text.split(u"成功:")[-1])
print (u"uid:%s" % return_msg[u"uid"])
print (u"username:%s" % return_msg[u"username"])
print (u"email:%s" % return_msg[u"email"])
print (u"password:%s" % return_msg[u"password"])

ele_search_uid = drive.find_element_by_id(u"search_uid")
ele_search_uid.send_keys(0)
ele_search = drive.find_element_by_xpath("/html/body/div[2]/div[1]/input[2]")
ele_search.click()

# ele_search_msg = drive.find_element_by_id(u"search_msg")
# return_search_msg = json.loads(ele_search_msg.text)
# print (u"uid:%s" % return_search_msg[u"uid"])
# print (u"username:%s" % return_search_msg[u"username"])
# print (u"password:%s" % return_search_msg[u"password"])
# print (u"email:%s" % return_search_msg[u"email"])
# time.sleep(3)
#
ele_search_uname = drive.find_element_by_id(u"search_uname")
ele_search_uname.send_keys(u"yuan")
ele_search1 = drive.find_element_by_xpath("/html/body/div[2]/div[2]/input[2]")
ele_search1.click()
#
# ele_search_msg1 = drive.find_element_by_id(u"search_msg")
# return_search_uname = json.loads(ele_search_msg1.text)
# print (u"uid:%s" % return_search_uname[u"uid"])
# print (u"username:%s" % return_search_uname[u"username"])
# print (u"password:%s" % return_search_uname[u"password"])
# print (u"email:%s" % return_search_uname[u"email"])
# time.sleep(3)
#
ele_search_email = drive.find_element_by_id(u"search_email")
ele_search_email.send_keys(u"yuan@qq.com")
ele_search2 = drive.find_element_by_xpath("/html/body/div[2]/div[3]/input[2]")
ele_search2.click()
#
# ele_search_msg2 = drive.find_element_by_id(u"search_msg")
# return_search_email = json.loads(ele_search_msg2.text)
# print (u"uid:%s" % return_search_email[u"uid"])
# print (u"username:%s" % return_search_email[u"username"])
# print (u"password:%s" % return_search_email[u"password"])
# print (u"email:%s" % return_search_email[u"email"])

ele_table = drive.find_element_by_id("table")
ele_table_tr = ele_table.find_elements_by_tag_name("tr")
may = []
june = []
for i in range(len(ele_table_tr)):
    if i == 0:
        continue
    else:
        tds = ele_table_tr[i].find_elements_by_tag_name("td")
        for j in range(len(tds)):
            if j == 1:
                may.append(tds[j].text)
            elif j == 2:
                june.append(tds[j].text)
            else:
                continue

may_sum = 0
june_sum = 0
for i in may:
    may_sum += int(i)
for i in june:
    june_sum += int(i)

print may
print june
print may_sum
print june_sum

drive.back()

ele_optTest = drive.find_element_by_link_text(u"页面元素操作练习")
ele_optTest.click()

ele_opt_text = drive.find_element_by_id("1_1")
ele_opt_text.send_keys(u"123a")
ele_opt_text1 = drive.find_element_by_xpath("/html/body/div[1]/div[1]/input[2]")
ele_opt_text1.click()

ele_opt_pwd = drive.find_element_by_id("1_2")
ele_opt_pwd.send_keys(u"123a")
ele_opt_pwd1 = drive.find_element_by_xpath("/html/body/div[1]/div[2]/input[2]")
ele_opt_pwd1.click()

ele_opt_email = drive.find_element_by_id("1_3")
ele_opt_email.send_keys(u"123@qq.com")
ele_opt_email1 = drive.find_element_by_xpath("/html/body/div[1]/div[3]/input[2]")
ele_opt_email1.click()

ele_fruit = Select(drive.find_element_by_id(u"fruit"))
print ele_fruit.first_selected_option.text

all_fruit = ele_fruit.options
print len(all_fruit)
print all_fruit[2].text
for fruit in all_fruit:
    print fruit.text

ele_fruit.select_by_index(1)
ele_fruit.select_by_value(u"mihoutao")
ele_fruit.select_by_visible_text(u"荔枝")

# ele_radiobts=drive.find_elements_by_name(u"fruit")
# for radiobt in ele_radiobts:
#     if radiobt.get_attribute("value")=="berry":
#         radiobt.click()
#     print radiobt.is_selected()
#     print radiobt.get_attribute("value")

# ele_radiobts2=drive.find_elements_by_name(u"fruit2")
# for radiobt2 in ele_radiobts2:
#     if radiobt2.get_attribute("value")=="berry":
#         radiobt2.click()
#     print radiobt2.is_selected()
#     print radiobt2.get_attribute("value")


ele_div1 = drive.find_element_by_id(u"div1")
ele_div2 = drive.find_element_by_id(u"div2")
print ele_div1.is_displayed()
print ele_div2.is_displayed()
ele_button = drive.find_element_by_id(u"button1")
ele_button.click()
print ele_div1.is_displayed()
print ele_div2.is_displayed()

print "================================"

ele_enable_input = drive.find_element_by_xpath("/html/body/div[3]/div[1]/input")
print ele_enable_input.is_enabled()

ele_disenable_input = drive.find_element_by_xpath("/html/body/div[3]/div[2]/input")
print ele_disenable_input.is_enabled()

ele_doubleClickBt = drive.find_element_by_id("context_click")
action_chains = ActionChains(drive)
action_chains.double_click(ele_doubleClickBt).perform()
print ele_doubleClickBt.get_attribute("style")

ele_alterbt=drive.find_element_by_xpath("/html/body/div[5]/div/input[1]")
ele_alterbt.click()
alert=drive.switch_to.alert
print alert.text
time.sleep(2)
alert.accept()

# ele_alterbt2 = drive.find_element_by_xpath("/html/body/div[5]/div/input[2]")
# ele_alterbt2.click()
# alert = drive.switch_to.alert
# print alert.text
# time.sleep(2)
# alert.accept()
# alert.dismiss()

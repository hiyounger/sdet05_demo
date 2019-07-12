#encoding:utf-8

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import json
from selenium.webdriver import ActionChains
#初始化一个irfox浏览器的driver
driver=webdriver.Firefox()

#打开指定url的页面
url="http://47.92.220.226/webdriver/"
driver.get(url)

# #根据标签定位(定位方法测试页面)页面元素
# tag_index=driver.find_elements_by_tag_name("a")
# #用来接收所找到的标签
# tag_a_index=None
#
# #遍历所有a标签
# for i in tag_index:
#     #根据a标签的文本定位到他
#     if i.text==u"定位方法测试页面":
#         #将找到的a标签赋值
#         tag_a_index=i
#         break
# #等待时间/秒
# time.sleep(3)
# #点击
# tag_a_index.click()

# #通过xpath绝对路径定位
# xpath_index=driver.find_element_by_xpath("/html/body/ul/li[1]/a")
# xpath_index.click()

# #通过xpath相对路径定位
# xpath_index=driver.find_element_by_xpath("//ul/li[1]/a")
# xpath_index.click()

# #通过link_text定位元素
# link_text=driver.find_element_by_link_text("定位方法测试页面")
# link_text.click()

#通过部分link_text定位元素
partialLink_text=driver.find_element_by_partial_link_text(u"定位方法")
partialLink_text.click()

#通过id定位元素
username=driver.find_element_by_id(u"username")
#在文本框中输入
username.send_keys(u"root")

#通过name定位
email=driver.find_element_by_name(u"email")
email.send_keys(u"1450004653@qq.com")

#通过clssname定位
password=driver.find_elements_by_class_name(u"login_input")[2]
password.send_keys(u"123")

#通过css_selector定位
Surepassword=driver.find_element_by_css_selector(u"#confirm_password")
Surepassword.send_keys(u"123")

register=driver.find_element_by_xpath(u"//td/input[@type='button']")
register.click()


# regmsg=driver.find_element_by_id(u"regmsg").text
# print regmsg
# regmsgJson=json.loads(regmsg.split(u"成功:")[-1],encoding="utf-8")
# print ("uid:%s" % (regmsgJson["uid"]))
# print ("username:%s" % (regmsgJson["username"]))
# print ("password:%s" % (regmsgJson["password"]))
# print ("email:%s" % (regmsgJson["email"]))
#
# search_uid=driver.find_element_by_id(u"search_uid").send_keys(u"0")
# serch_msg=driver.find_element_by_xpath(u"/html/body/div[2]/div[1]/input[2]")
# serch_msg.click()
# serch_msg=serch_msg.text
# search_uidJson=json.loads(regmsg.split(u"成功:")[-1],encoding="utf-8")
# print ("uid:%s" % (search_uidJson["uid"]))
# print ("username:%s" % (search_uidJson["username"]))
# print ("password:%s" % (search_uidJson["password"]))
# print ("email:%s" % (search_uidJson["email"]))

ele_table=driver.find_element_by_id(u"table")
ele_table_tr=driver.find_elements_by_tag_name(u"tr")
may=[]
june=[]
for i in range(len(ele_table_tr)):
    if i ==0:
        continue
    else:
        td=ele_table_tr[i].find_elements_by_tag_name(u"td")
        for j in range(len(td)):
            if j==1:
                may.append(td[j].text)
            elif j==2:
                june.append(td[j].text)
            else:
                continue
print (may)
print (june)

driver.back()
ele_by_name=driver.find_element_by_link_text("页面元素操作练习")
ele_by_name.click()

#输入文本点击按钮输入输入的值
input_text=driver.find_element_by_id(u"1_1")
input_text.send_keys(u"qwe")
dianji=driver.find_element_by_xpath("/html/body/div[1]/div[1]/input[2]")
dianji.click()
input_text_shuchu=driver.find_element_by_id(u"1_1_msg")
print input_text_shuchu.text
time.sleep(2)
#输入文本点击按钮输入输入的值
input_text=driver.find_element_by_id(u"1_2")
input_text.send_keys(u"123")
dianji=driver.find_element_by_xpath("/html/body/div[1]/div[2]/input[2]")
dianji.click()
input_text_shuchu=driver.find_element_by_id(u"1_2_msg")
print input_text_shuchu.text
time.sleep(2)
#输入文本点击按钮输入输入的值
input_text=driver.find_element_by_id(u"1_3")
input_text.send_keys(u"342@545")
dianji=driver.find_element_by_xpath("/html/body/div[1]/div[3]/input[2]")
dianji.click()
input_text_shuchu=driver.find_element_by_id(u"1_3_msg")
print input_text_shuchu.text



#下拉列表
ele_selet=Select(driver.find_element_by_id(u"fruit"))
#获取当前选项
print ele_selet.first_selected_option.text
#获取所有可选项
ele_options=ele_selet.options
print ele_options[2].text
print len(ele_options)
for opt in ele_options:
    print opt.text

#选择一个指定的选项
ele_selet.select_by_index(2)
time.sleep(3)
ele_selet.select_by_value(u"mihoutao")
time.sleep(3)
ele_selet.select_by_visible_text(u"荔枝")

#单选按钮操作
#radiobt.is_selected查看是否选中
ele_radiobts=driver.find_elements_by_name(u"fruit")
for radiobt in ele_radiobts:
    if radiobt.get_attribute(u"value")==u"berry":
        radiobt.click()
    print ("value:%s,is_selected:%s"%(radiobt.get_attribute("value"),radiobt.is_selected()))

#隐藏按钮
ele_div1=driver.find_element_by_id("div1")
ele_div2=driver.find_element_by_id("div2")
print ("if div1 displayed:%s" % (ele_div1.is_displayed()))
print ("if div2 displayed:%s" % (ele_div2.is_displayed()))
#是否可用
driver.find_element_by_id("button1").click()
print ("if div1 displayed:%s" % (ele_div1.is_displayed()))
print ("if div2 displayed:%s" % (ele_div2.is_displayed()))

ele_enable_input=driver.find_element_by_xpath("//div[3]/div[1]/input")
print ("ele_enable_input if enabled:%s" % ele_enable_input.is_enabled())

ele_enable_input=driver.find_element_by_xpath("//div[3]/div[2]/input")
print ("ele_enable_input if enabled:%s" % ele_enable_input.is_enabled())

#鼠标动作
ele_doubleClick=driver.find_element_by_id("context_click")
action_chains=ActionChains(driver)
action_chains.double_click(ele_doubleClick).perform()
print (ele_doubleClick.get_attribute("style"))

#alert弹窗
ele_alert=driver.find_element_by_xpath("//div[5]/div/input[1]")
ele_alert.click()
alert=driver.switch_to.alert
print ("alert text:%s" % alert.text)
time.sleep(2)
alert.accept()

#confirm弹窗
ele_confirm=driver.find_element_by_xpath("//div[5]/div/input[2]")
ele_confirm.click()
confirm=driver.switch_to.alert
print ("alert text:%s" % confirm.text)
time.sleep(2)
confirm.accept()
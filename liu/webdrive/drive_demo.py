#encoding:utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import  json
import time
from selenium.webdriver import ActionChains



#初始化一个Fierfox的driver
driver = webdriver.Firefox()

#打开指定的页面url
url_indexPage = "http://47.92.220.226/webdriver/index.html"
driver.get(url_indexPage)

#
# #定位<定位方法测试页面>页面元素
# # eles_locationTest= driver.find_element_by_xpath('/html/body/ul/li[1]/a')
# # eles_locationTest.click()
# #根据标签定位页面元素
# # eles_aTag = driver.find_elements_by_tag_name(u"a")
# # eles_locationTest = None
# # for element in eles_aTag:
# #     if element.text == u"定位方法测试页面":
# #         eles_locationTest = element
# #         break
# # eles_locationTest.click()
# #根据相对路径
# # eles_locationTest = driver.find_element_by_xpath('//ul/li[1]/a')
# # eles_locationTest.click()
# #根据link文字定位a控件
# # eles_locationTest = driver.find_element_by_link_text(u'定位方法测试页面')
# # eles_locationTest.click()
# eles_locationTest = driver.find_element_by_partial_link_text(u'定位方法')
# eles_locationTest.click()
# #目前在定位方法测试页面
# # 通过id定位一个输入框，并输入的值
# ele_username = driver.find_element_by_id(u'username')
# ele_username.send_keys((u"qsong"))
#
# ele_email = driver.find_element_by_name(u'email')
# ele_email.send_keys((u"qsong.vip@qq.com"))
#
# ele_password = driver.find_elements_by_class_name(u'login_input')[2]
# ele_password.send_keys((u"hiyoung888"))
#
# ele_confirm_pwd = driver.find_element_by_css_selector(u'#confirm_password')
# ele_confirm_pwd.send_keys((u"hiyoung888"))
#
# ele_register_bt = driver.find_element_by_xpath(u"//td[@colspan='2']/input[1]")
# ele_register_bt.click()
#
# ele_insert_id = driver.find_element_by_xpath(u'//*[@id="search_uid"]')
# ele_insert_id.send_keys(u'0')
# ele_query_id = driver.find_element_by_xpath(u'//div[1]/input[2]')
# ele_query_id.click()
#
# ele_insert_name = driver.find_element_by_xpath(u'//*[@id="search_uname"]')
# ele_insert_name.send_keys(u'qsong')
# ele_query_name = driver.find_element_by_xpath(u'//div[2]/input[2]')
# ele_query_name.click()
#
#
# ele_insert_email = driver.find_element_by_xpath(u'//*[@id="search_email"]')
# ele_insert_email.send_keys(u'qsong.vip@qq.com')
# ele_query_email = driver.find_element_by_xpath(u'//div[3]/input[2]')
# ele_query_email.click()
#
# #通过id获取返回值显示页面元素
# ele_retmsg = driver.find_element_by_id(u'regmsg')
# retmsg_text = ele_retmsg.text
# retmsg_json = json.loads(retmsg_text.split(u'成功:')[-1])
#
# print(retmsg_json)
# print(u'uid:%s' % retmsg_json[u'uid'])
# print(u'username:%s' % retmsg_json[u'username'])
# print(u'password:%s' % retmsg_json[u'password'])
# print(u'email:%s' % retmsg_json[u'email'])
#
# ele_table = driver.find_element_by_id(u'table')
# ele_table_trs = ele_table.find_elements_by_tag_name(u"tr")
# may=[]
# june=[]
# for i in range(len(ele_table_trs)):
#     if i != 0:
#         tds = ele_table_trs[i].find_elements_by_tag_name(u'td')
#         for j in  range(len(tds)):
#             if j==1:
#                 may.append(tds[j].text)
#             elif j==2:
#                 june.append(tds[j].text)
#             else:
#                 continue
#
# print (may)
# print(june)
# # may_text = may.text
# # may_json = json.loads(may_text.split("u'")[-1])
# # print(may_json)
#
# driver.back()
#
ele_operate = driver.find_element_by_xpath(u'/html/body/ul/li[2]/a')
ele_operate.click()

# #页面元素操作练习界面
# ele_insert_text = driver.find_element_by_xpath(u'//*[@id="1_1"]')
# ele_insert_text.send_keys(u'123')
# ele_query_text = driver.find_element_by_xpath(u'/html/body/div[1]/div[1]/input[2]')
# ele_query_text.click()
#
# ele_insert_password = driver.find_element_by_xpath(u'//*[@id="1_2"]')
# ele_insert_password.send_keys(u'123')
# ele_query_password = driver.find_element_by_xpath(u'/html/body/div[1]/div[2]/input[2]')
# ele_query_password.click()
#
# ele_insert_Email = driver.find_element_by_xpath(u'//*[@id="1_3"]')
# ele_insert_Email.send_keys(u'123@1')
# ele_query_Email = driver.find_element_by_xpath(u'/html/body/div[1]/div[3]/input[2]')
# ele_query_Email.click()
#
# ele_return = driver.find_element_by_xpath(u'//*[@id="1_1_msg"]')
# ret_text = ele_return.text
# ret_json = json.loads(retmsg_text.split(u'为:')[-1])
#
# print(ret_json)




#目前在定位方法测试页面
#1.1通过id定位一个输入款，并输入的值
ele_select = Select(driver.find_element_by_id(u'fruit'))
#1.2获取当前选中的项
print ele_select.first_selected_option.text
#1.3获取所有可选项
ele_options = ele_select.options
print ele_options[2].text
print len (ele_options)
for opt in ele_options:
    print opt.text
#2选择一个指定的选项
ele_select.select_by_index(2)
time.sleep(2)
ele_select.select_by_value(u'mihoutao')
time.sleep(2)
ele_select.select_by_visible_text(u'荔枝')
#3 单选按钮操作
ele_radiobts = driver.find_elements_by_name(u'fruit')
for radiobt in ele_radiobts:
    if radiobt.get_attribute(u'value')==u'berry':
        radiobt.click()
    print("value: %s ,is_selected: %s"%(radiobt.get_attribute('value'),radiobt.is_selected()))

ele_radiobtsdb = driver.find_elements_by_name(u'fruit2')
for radiobts in ele_radiobtsdb:
    if radiobts.get_attribute(u'value')==u'berry'or radiobts.get_attribute(u'value')==u'orange':
        radiobts.click()
    print("value: %s ,is_selected: %s"%(radiobts.get_attribute('value'),radiobts.is_selected()))


ele_div1 = driver.find_element_by_id('div1')
ele_div2 = driver.find_element_by_id('div2')
print('if div1 displayed:%s' % ele_div1.is_displayed())
print('if div2 displayed:%s' % ele_div2.is_displayed())

driver.find_element_by_id('button1').click()
print('if div1 displayed:%s' % ele_div1.is_displayed())
print('if div2 displayed:%s' % ele_div2.is_displayed())

ele_enable_input = driver.find_element_by_xpath("//div[3]/div[1]/input")
print("ele_enable_input if enable:%s" % ele_enable_input.is_enabled())

ele_disenable_input = driver.find_element_by_xpath("//div[3]/div[2]/input")
print("ele_disenable_input if enable:%s" % ele_disenable_input.is_enabled())

ele_doubleClickBt = driver.find_element_by_id("context_click")
action_chains = ActionChains(driver)
action_chains.double_click(ele_doubleClickBt).perform()
print(ele_doubleClickBt.get_attribute("style"))

ele_alertbt = driver.find_element_by_xpath("//div[5]/div/input[1]")
ele_alertbt.click()
alter = driver.switch_to.alert
print ("Alter text:%s"%alter.text)
time.sleep(1.5)
alter.accept()

ele_alertbt2 = driver.find_element_by_xpath("//div[5]/div/input[2]")
ele_alertbt2.click()
alter2 = driver.switch_to.alert
print ("Alter text:%s"%alter2.text)
time.sleep(1.5)
alter2.accept()
# -*- encoding: utf-8 -*-

from base import Base

class Rand10SecPage(Base):

    url = "http://demo.hiyounger.cn/webdriver/10seconds"
    title = u"加载需要10秒的页面"
    keyword_xpath = u"//h1"
    keyword_text = u"HiYoung Webdriver Demo - 10 Seconds Loading Page"
    open_timeout = 20

class Webdriver_Demo(Base):

    url = "http://demo.hiyounger.cn/webdriver/element"
    title = u"页面元素操作练习页面"
    keyword_xpath = u"//h1"
    keyword_text = u"HiYoung Webdriver Demo - Elements"
    open_timeout = 20
#encoding:utf-8
from Yzx.templates_example.page_is_opean_judage.judage_base import if_pageOpean_juage
class Juage(if_pageOpean_juage):
    url = "http://demo.hiyounger.cn/webdriver/10seconds"
    title = u"加载需要10秒的页面"
    keyword_xpath = u"//h1"
    keyword_text = u"HiYoung Webdriver Demo - 10 Seconds Loading Page"
    open_timeout = 20
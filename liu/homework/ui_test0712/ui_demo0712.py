# encoding:utf-8
class BasePage():
    page_name = None
    page_url = None

    def open(self):
        print ("我是：%s, 我是open函数" %self.page_name)

class LocationPage(BasePage):

    def __init__(self,name,url):
        self.page_name = name
        self.page_url = url

    def instance_method(self):
        print("我是一个实例方法"+self.page_name)

    @classmethod
    def class_method(cls):
        print("我是一个类方法")

    @property
    def info(self):
        __info = "PageInfo: name:%s, url:%s"%(self.page_name,self.page_url)
        return __info
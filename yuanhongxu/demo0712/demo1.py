# -*- encoding:utf-8 -*-


class father():
    page_name=None
    page_url=None

    def open(self):
        return ("这是open方法：%s"%self.page_name)

class son(father):

    def __init__(self,name,url):
        self.page_name=name
        self.page_url=url

    def function(self):
        return "这是一个实例方法"

    @classmethod
    def function2(cls):
        return "这是一个类方法"

    @property
    def info(self):
        __info="page info name:%s url:%s"%(self.page_name,self.page_url)
        return __info


son_page1=son("baidu","www.baidu.com")

print son_page1.page_name
print son_page1.page_url
print son_page1.info
print son_page1.function()
print son.function2()
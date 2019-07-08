# encoding:utf-8
import unittest
import requests
from ddt import ddt, file_data


@ddt
class TestTelLocation(unittest.TestCase):
    @file_data('test_tellocation.json')
    def test_testPhone(self, phone):
    # 1.定义所需请求的URL和参数
        url = "http://apis.juhe.cn/mobile/get"
        payload = {
            "phone": phone,
            "key": "802831374e480e92f88f1bd989a805b0"
        }
    # 2.通过requests 发送一个get请求包含（url,payload）,并获取响应
        resp = requests.get(url,params=payload)
        resp.encoding = 'utf-8'
        resp_jsondata = resp.json()
    # 3.验证
        print (resp_jsondata['reason'])



if __name__ == '__main__':
    unittest.main()

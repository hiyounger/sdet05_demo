#encoding:utf-8

import unittest
import requests
from ddt import ddt,file_data

@ddt
class TestPhone(unittest.TestCase):
    @file_data("testphone_config.json")
    def test_phone(self,phone):
        #1.定义所需请求的url和参数
        url="http://apis.juhe.cn/mobile/get"
        payload={
            "phone":phone,
            "key":"802831374e480e92f88f1bd989a805b0"
        }
        #2.通过request发送一个get请求(url,payload),并获取响应
        resp=requests.get(url,params=payload)
        resp.encoding="utf-8"
        resp_json=resp.json()
        #3验证
        print (resp_json["reason"])
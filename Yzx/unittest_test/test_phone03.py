import unittest
import requests
import json
from ddt import  ddt,file_data

@ddt
class MyTestCase(unittest.TestCase):
    @file_data("test_phone.json")
    def test_testPhone_case006(self,phone):
        url="http://apis.juhe.cn/mobile/get"
        payload={
            'phone':phone,
            'key':"802831374e480e92f88f1bd989a805b0"
        }
        resp=requests.get(url,params=payload)
        resp.encoding="utf-8"
        resp_jsondata=resp.json()
        print resp_jsondata['result']
        print resp_jsondata['result']['province']
        print resp_jsondata['result']['city']
        print resp_jsondata['result']['company']


if __name__ == '__main__':
    unittest.main()

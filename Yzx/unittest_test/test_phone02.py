import unittest
import requests
import json

class MyTestCase(unittest.TestCase):
    def test_testPhone_case006(self):
        url="http://apis.juhe.cn/mobile/get"
        payload={
            'phone':"1884587",
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

# encoding:utf-8
import unittest
import requests
import json
from ddt import ddt,file_data
@ddt
class MyTestCase(unittest.TestCase):
    @file_data("test_demo.json")
    def test_get_member_by_uid(self,uid):
        url = "http://192.168.8.52:9527/getmember?/"
        payload={
            "uid":uid,
        }
        resp=requests.get(url,params=payload)
        resp.encoding="utf-8"
        self.assertEqual(200,resp.status_code,u"请求url:%s,返回状态码%s"%(url,resp.status_code))
        resp_jsondata=resp.json()
        print (type(resp_jsondata))
        print (resp_jsondata["uid"])

    @file_data("test_demo1.json")
    def test_register(self, username,password):
        url = "http://192.168.8.52:9527/register"
        payload = {
            "username":username,
            "password":password,
        }
        resp = requests.get(url, params=payload)
        resp.encoding = "utf-8"
        self.assertEqual(200, resp.status_code, u"请求url:%s,返回状态码%s" % (url, resp.status_code))
        resp_jsondata = resp.json()
        print (type(resp_jsondata))
        print (resp_jsondata["uid"])






if __name__ == '__main__':
    unittest.main()

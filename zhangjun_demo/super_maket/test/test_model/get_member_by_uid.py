# encoding:utf-8
import unittest
import requests
import json
from ddt import ddt,file_data
@ddt
class MyTestCase(unittest.TestCase):
    @file_data("get_member_by_uid")
    def test_get_member_by_uid(self,uid):
        url = "http://192.168.8.52:5002/member/"
        payload={
            "uid":uid,
        }
        resp=requests.get(url,params=payload)
        resp.encoding="utf-8"
        resp_jsondata=resp.json()
        print (type(resp_jsondata))
        print (resp_jsondata["reason"])





if __name__ == '__main__':
    unittest.main()

#-*- encoding:utf-8 -*-
import unittest
import requests
from ddt import ddt, file_data

@ddt
class MyTestCase(unittest.TestCase):
    @file_data("test_demo.json")
    def test_case01(self,input_data,exp_data):
        url="http://192.168.8.52:9527/register"
        payload={
            "username":input_data["username"],
            "password":input_data["password"]
        }
        resp=requests.post(url,data=payload)
        resp_data=resp.json()
        resp.encoding="utf-8"
        file_list=[]
        for key in exp_data.keys():
            if exp_data[key]!=resp_data[key]:
                file_list.append(key)
        self.assertEqual(len(file_list), 0)

    # @file_data("test_demo2.json")
    # def test_case02(self, input_data, exp_data):
    #     url = "http://192.168.8.52:9527getmember?uid=%s"%input_data["uid"]
    #     payload = {}
    #     resp = requests.get(url,params=payload)
    #     resp_data = resp.json()
    #     resp.encoding = "utf-8"
    #     file_list = []
    #     for key in exp_data.keys():
    #         if exp_data[key] != resp_data[key]:
    #             file_list.append(key)
    #     self.assertEqual(len(file_list), 0)


if __name__ == '__main__':
    unittest.main()

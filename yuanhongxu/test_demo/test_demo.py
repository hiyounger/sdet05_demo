#-*- encoding:utf-8 -*-
import unittest
import requests
import json
from ddt import ddt,file_data

@ddt
class MyTestCase(unittest.TestCase):
    # def test_case01(self):
    #     num1=1
    #     num2=1
    #     act_result=num2+num1
    #     exp_result=2
    #
    #     self.assertEqual(act_result, exp_result,"act:%s+%s=%s,exp:%s"%(num1,num2,act_result,exp_result))
    #
    # def test_case02(self):
    #     num1 = 1
    #     num2 = 1
    #     act_result = num2 + num1
    #     exp_result = 3
    #
    #     self.assertEqual(act_result, exp_result, "act:%s+%s=%s,exp:%s" % (num1, num2, act_result, exp_result))

    # def test_case03(self):
    #     url="http://www.baidu.com"
    #     resp=requests.get(url)
    #     print (resp.text)
    #
    # def test_case04(self):
    #     url="http://127.0.0.1:5002/member"
    #     resp=requests.get(url)
    #     print (resp.text)

    @file_data("test_demo.json")
    def test_case05(self,phone):
        url="http://apis.juhe.cn/mobile/get"
        data={
            "phone":phone,
            "key":"802831374e480e92f88f1bd989a805b0"
        }
        resp=requests.get(url,params=data)
        resp.encoding="utf-8"
        resp_text=resp.text
        print(type(resp_text))
        print (resp_text)
        resp_json=json.loads(resp_text)
        print (type(resp_json))
        print (resp_json)
        print (resp_json["resultcode"])
        resp_data=resp.json()
        print (resp_data["reason"])




if __name__ == '__main__':
    unittest.main()

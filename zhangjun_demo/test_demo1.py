# encoding:utf-8
import unittest
import requests
import json
from ddt import ddt,file_data

@ddt
class MyTestCase(unittest.TestCase):
    # def test_case01(self):
    #     num1=1
    #     num2=2
    #     act_result=num1+num2
    #     exp_result=4
    #     self.assertEqual(exp_result, act_result,"exp:%s+%s=%s,act:=%s"%(num1,num2,act_result,exp_result))
    @file_data
    def test_case03(self):
        url = "http://apis.juhe.cn/mobile/get"
        payload={
            "phone":"180625029",
            "key":"802831374e480e92f88f1bd989a805b0",
        }


        resp=requests.get(url,params=payload)
        resp.encoding="utf-8"
        # print (resp.text)
        # print (type(resp.text))
        # resp_json=json.loads(resp.text)
        # print (type(resp_json))
        # print (resp_json["resultcode"])
        resp_jsondata=resp.json()
        print (type(resp_jsondata))
        print (resp_jsondata["resultcode"])





if __name__ == '__main__':
    unittest.main()

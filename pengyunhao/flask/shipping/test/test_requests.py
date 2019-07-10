#encoding:utf-8
import unittest
import requests
import json

class myTest(unittest.TestCase):
    def test01(self):
        num1=1
        num2=2
        exp_result=num1+num2
        act_result=2
        self.assertEqual(exp_result,act_result,"exp:%s+%s=%s,act=%s"%(num1,num2,exp_result,act_result))

    def test_reqursts01(self):
        url="http://www.baidu.com"
        resp=requests.get(url)
        print (resp.text)

    def test_requests02(self):
        url="http://192.168.8.52/member"
        resp=requests.get(url)
        print (resp.text)

    def test_phone01(self):
        url="http://apis.juhe.cn/mobile/get?"+"phone=180625&key=802831374e480e92f88f1bd989a805b0"
        resp=requests.get(url)
        resp.encoding="utf-8"
        resp_text=resp.text
        print (type(resp_text))
        print (resp_text)
        resp_json=json.loads(resp_text)
        print (type(resp_json))
        print (resp_json["resultcode"])


    def test_phone02(self):
        #1.定于一所需的请求的url和参数
        url="http://apis.juhe.cn/mobile/get"
        payload={
            "phone":"180625",
            "key":"802831374e480e92f88f1bd989a805b0"
        }
        #2.通过requests发送一个GET请求(url,payload)
        resp=requests.get(url,params=payload)
        #3.设置http响应内容的字符编码，常用于中午
        resp.encoding="utf-8"
        #4.获取http响应的内容
        resp_text=resp.text
        print (type(resp_text))
        print (resp_text)
        #5.将符合字典格式的字符串转换成json字典
        resp_json=json.loads(resp_text)
        print (type(resp_json))
        print (resp_json["resultcode"])
        #6.如果响应返回的值为json，识别：header中包含Content——Type中包含application/json
        #使用resp.json直接获取json格式字典
        resp_jsondata=resp.json()
        print resp_jsondata["reason"]
# encoding:utf-8
import unittest
import requests
import json


class MyTestCase(unittest.TestCase):

    def test_case_001(self):
        url = 'http://www.baidu.com'
        resp = requests.get(url)
        print (resp.text)

    def test_case_002(self):
        url = 'http://192.168.8.52:5001/member'
        resp = requests.get(url)
        print (resp.text)

    def test_testphone_case003(self):
        url = 'http://apis.juhe.cn/mobile/get?' + 'phone=1884509&key=802831374e480e92f88f1bd989a805b0'
        resp = requests.get(url)
        resp.encoding = 'utf-8'
        resp_text = resp.text
        print (type(resp_text))
        print resp_text
        resp_json = json.loads(resp_text)
        print (type(resp_json))
        print resp_json

    def test_testphone_case004(self):
        # 1定义所需请求的URL和参数（请求值）
        url = 'http://apis.juhe.cn/mobile/get'
        payload = {
            'phone': '1884509',
            'key': "802831374e480e92f88f1bd989a805b0"
        }
        # 2通过requests发送一个get请求 包含了请求值（url,payload）
        resp = requests.get(url, params=payload)
        # 3设置http响应内容的字符编码
        resp.encoding = 'utf-8'
        # 4获取http响应的内容
        resp_text = resp.text
        print (type(resp_text))  # 获取响应内容的类型
        print resp_text
        # 5将符合字典格式的字符串转换成json字典
        resp_json = json.loads(resp_text)
        print (type(resp_json))
        print (resp_json['resultcode'])
        # 6如果响应的返回值为json，识别，响应header中包含Content-type == application/json
        # 使用resp.json直接获取json格式字典
        resp_jsondata = resp.json()
        print (resp_jsondata['reason'])


if __name__ == '__main__':
    unittest.main()

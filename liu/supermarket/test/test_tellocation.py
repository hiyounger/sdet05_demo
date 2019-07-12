#encoding:utf-8
import unittest
import requests
import json
from ddt import ddt,file_data


    # def test_demo01(self):
    #     num1 = 1
    #     num2 = 1
    #     act_result = num1+num2
    #     exp_result = 3
    #     self.assertEqual(act_result,exp_result,'exp:%s+%s=%s,act_result=%s'%(num1,num2,act_result,exp_result))
    #
    # def test_demo02(self):
    #     num1 = 1
    #     num2 = 2
    #     act_result = num1+num2
    #     exp_result = 3
    #     self.assertEqual(act_result,exp_result,'%s+%s=%s,act_result=%s'%(num1,num2,act_result,exp_result))
    #  def test_case01(self):
    #
    #     url = "http://www.baidu.com"
    #     resp = requests.get(url)
    #     print (resp.text)
    #

     # def test_case02(self):
     #    url = "http://127.0.0.1:5002/member"
     #    resp = requests.get(url)
     #    print (resp.text)
     # def  test_testPhone_case005(self):
     #     # 定义所需要的url和参数
     #    url = 'http://apis.juhe.cn/mobile/get'
     #    payload = {
     #        'phone': '180625',
     #        'key':'802831374e480e92f88f1bd989a805b0'
     #    }
     #    #通过requests发送一个get请求（url,payload）
     #    resp = requests.get(url,params=payload)
     #    #设置http响应内容的文字编码，常用于中文
     #    resp.encoding = 'utf-8'
     #    #获取http响应的内容
     #    resp_text = resp.text
     #    print (resp_text)
     #    #将符号字典格式的字符串，转换成json字典
     #    print(type(resp_text))
     #    resp_json =json.loads(resp_text)
     #    print (resp_json)
     #    print(resp_json['resultcode'])
     #    #如果响应的返回值位json，识别：响应header中包含Conten-Type   application/json
     #    #使用resp。json直接获取json格式字典
     #    resp_jsondata = resp.json()
     #    print(resp_jsondata['reason'])
@ddt
class TestTelLocation(unittest.TestCase):

    @file_data("test_tellocation.json")
    def test_testPhone_case005(self, phone):
        url = 'http://apis.juhe.cn/mobile/get'
        payload = {
            'phone': phone,
            'key':'802831374e480e92f88f1bd989a805b0'
        }
        resp = requests.get(url,params=payload)
        resp.encoding = "utf-8"
        resp_jsondata = resp.json()
        print(resp_jsondata['reason'])


if __name__ == '__main__':
    unittest.main()

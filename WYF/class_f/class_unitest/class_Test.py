# encoding:utf-8
import unittest
import requests
from ddt import ddt,file_data

@ddt
class MyTestCase(unittest.TestCase):

    @file_data("class_test.json")
    def test_testUid(self,uid):
        url="http://192.168.8.52:9527/getmember"
        payload={
            'uid':uid
        }
        resq=requests.get(url,params=payload)
        resq.encoding='utf-8'
        self.assertEqual(200,resq.status_code,u'请求url：%s,返回响应码:%s'%(url,resq.status_code))
        resq_jsondata=resq.json()
        print (resq_jsondata)

if __name__ == '__main__':
    unittest.main()

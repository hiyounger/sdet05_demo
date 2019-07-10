# encoding:utf-8
import unittest
import requests
from ddt import ddt,file_data

@ddt
class MyTestCase(unittest.TestCase):

    @file_data("test_tellocation.json")
    def test_testPhon(self,phone):
        url="http://apis.juhe.cn/mobile/get"
        payload={
            'phone':phone,
            'key':'802831374e480e92f88f1bd989a805b0'
        }
        resq=requests.get(url,params=payload)
        resq.encoding='utf-8'
        resq_jsondata=resq.json()
        print (resq_jsondata['reason'])

if __name__ == '__main__':
    unittest.main()

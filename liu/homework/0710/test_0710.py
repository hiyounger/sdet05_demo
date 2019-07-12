#encoding:utf-8
import unittest
import requests
import json
from ddt import ddt,file_data

@ddt
class MyTestCase(unittest.TestCase):
    @file_data('test_0710.json')
    def test_0710get_case(self, uid):
        url = 'http://www.198.168.8.9527:/getmember'
        payload = {
            'uid':uid
        }
        resp = requests.get(url, params=payload)
        resp.encoding = "utf-8"
        resp_jsondata = resp.json()
        self.assertEqual(200, resp.status_code,u'请输入url:%s,返回状态码：%s'%(url,resp.status_code))
        act = resp_jsondata['retuen_code']
        exp = '200'
        self.assertEqual(act,exp)





    @file_data('test_0710.json')
    def test_0710post_case(self, username,password):
        url = 'http://www.198.168.8.9527:/getmember'
        payload = {
            'username': username,
            'password':password
        }
        resp = requests.get(url, params=payload)
        resp.encoding = "utf-8"
        resp_jsondata = resp.json()
        print(resp_jsondata['reason'])
        self.assertEqual(200, resp.status_code, u'请输入url:%s,返回状态码：%s' % (url, resp.status_code))







if __name__ == '__main__':
    unittest.main()

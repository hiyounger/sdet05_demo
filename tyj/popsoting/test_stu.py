# encoding:utf-8
import unittest
import requests
import json
from ddt import ddt, file_data


@ddt
class MyTestCase(unittest.TestCase):
    @file_data('test_stu.json')
    # 根据UID获取信息
    def test_stu(self, uid):
        url = "http://192.168.8.52:9527/getmember"
        payload = {
            'uid': uid
        }
        resp = requests.get(url, params=payload)
        resp.encoding = 'utf-8'
        resp_payload = resp.json()
        self.assertEqual(200, resp.status_code,u'')
        if resp_payload['status_code'] == 200:
            exp = [{'uid': uid}]
            act = resp_payload[{"uid": uid}]
        self.assertEqual(exp, act)


if __name__ == '__main__':
    unittest.main()

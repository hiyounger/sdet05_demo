#encoding:utf-8
import unittest
import requests
import json
from Yzx.unittest_test import config

class MyTestCase(unittest.TestCase):
    def test_testPhone_case005(self):
        phone="1884587"
        url=config.url+phone+config.key
        resp = requests.get(url)
        resp.encoding="utf-8"
        resp_text=resp.text
        resp_json=json.loads(resp_text)
        print resp_json
        print resp_json['result']['city']



if __name__ == '__main__':
    unittest.main()

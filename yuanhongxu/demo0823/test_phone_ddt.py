# coding:utf-8
import unittest
from ddt import ddt, file_data
import json
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

url = "http://apis.juhe.cn/mobile/get"


class MyTestCase(unittest.TestCase):
    def test_something(self):
        input_data = {
            "phone": "15823719487",
            "key": "802831374e480e92f88f1bd989a805b0"
        }
        exp_data = {
            "resultcode": "200",
            "reason": "Return Successd!",
            "result": {
                "province": "湖北",
                "city": "武汉",
                "areacode": "027",
                "zip": "430000",
                "company": "联通",
                "card": ""
            },
            "error_code": 0
        }
        payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"uid\"\r\n\r\n1\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        headers = {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'uid': "1",
            'cache-control': "no-cache",
            'Postman-Token': "9597ca13-e388-436e-b335-60e82cddbc22"
        }

        response = requests.request("GET", url, data=payload, headers=headers, params=input_data)
        resp = json.loads(response.text)


        exp_result=exp_data["result"]["province"]
        act_result=resp["result"]["province"]


        self.assertEqual(exp_result, act_result,"exp_result:%s,act_result%s,url:%s,input_data:%s"%(exp_result,act_result,url,input_data))


if __name__ == '__main__':
    unittest.main()

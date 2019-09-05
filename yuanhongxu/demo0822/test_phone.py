# coding:utf-8
import unittest
from ddt import ddt, file_data
import json
import requests


@ddt
class MyTestCase(unittest.TestCase):

    @file_data("test_phone.json")
    def test_case01(self, input_data, exp_data):
        url = "http://apis.juhe.cn/mobile/get"

        # querystring = {"phone": input_data["phone"], "key":input_data["key"] ,"dtype":input_data["dtype"]}
        # querystring = {}
        # for key in input_data.keys():
        #     querystring[key] = input_data[key]
        querystring = input_data

        payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"uid\"\r\n\r\n1\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        headers = {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'uid': "1",
            'cache-control': "no-cache",
            'Postman-Token': "9597ca13-e388-436e-b335-60e82cddbc22"
        }

        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        resp = json.loads(response.text)
        file_list = []
        for key in exp_data.keys():
            if exp_data[key] != resp[key]:
                file_list.append(key)
        self.assertEqual(len(file_list), 0, "错误参数列表%s" % (file_list))


if __name__ == '__main__':
    unittest.main()

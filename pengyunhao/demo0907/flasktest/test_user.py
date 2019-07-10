import requests
from ddt import file_data
import unittest
@file_data("user_test")
class userTest(unittest.TestCase):
    def test_addSuccess(self):
        url="http://127.0.0.1:5000/register"
        payload={

        }
        resp=requests.post(url)
        resp.encoding="utf-8"
        print resp.json()

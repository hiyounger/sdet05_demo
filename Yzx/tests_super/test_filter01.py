import unittest
import requests
import json
from ddt import ddt,file_data

@ddt
class MyTestCase(unittest.TestCase):
    @file_data("test_filterData.json")
    def test_something(self,le):
        url="http://127.0.0.1:5000/filter/score"
        data={
            'le':le
        }
        resq=requests.get(url,params=data)
        resq.encoding="utf-8"
        resq_data=resq.json()
        print resq_data

        # self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()

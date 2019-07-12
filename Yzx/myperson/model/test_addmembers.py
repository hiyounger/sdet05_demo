import unittest
import requests
from ddt import ddt,file_data
from Yzx.myperson import config
@ddt
class TestAddmember(unittest.TestCase):
    @file_data("test_addMember.json")
    def test_addMember_case001(self,input_data,except_data):
        url='http://%s:%s/register'%(config.DB_HOST,config.DB_PORT)
        data1={
            'username':input_data['username'],
            'password':input_data['password']
        }
        resp=requests.post(url,data=data1)
        resp.encoding='utf-8'
        resp_jsondata = resp.json()
        # {"password": "123",    "uid": 61,    "username": "123781111111"}
        except_data={
            'username': input_data['username'],
            'password': input_data['password'],
            'uid':resp_jsondata['uid']
        }
        fail_list = []
        for key in resp_jsondata.keys():
            try:
                # 判断响应体中，键与对应的值是否匹配
                if except_data[key] != resp_jsondata[key]:
                    fail_list.append(key)
            except:
                # 判断响应体中不存在的指定的键
                fail_list.append(key)
        self.assertEqual(0, len(fail_list),
                         "exp_json:%s,act_json:%s,failed_keys:%s" % (str(except_data), str(resp_jsondata), str(fail_list)))
if __name__ == '__main__':
    unittest.main()

#encoding:utf-8
import unittest
import requests
# unittest第三个参数
class MyTestCase(unittest.TestCase):
    def test_case01(self):
        nmu1=1
        nmu2=2
        exp_result=3
        act_result=nmu1+nmu2
        self.assertEqual(exp_result, act_result, "exp:%s+%s=%s act:=%s"%(nmu1,nmu2,act_result,exp_result))
    def test_case02(self):
        nmu1=1
        nmu2=2
        exp_result=4
        act_result=nmu1+nmu2
        self.assertEqual(exp_result, act_result, "exp:%s+%s=%s act:=%s"%(nmu1,nmu2,act_result,exp_result))
    def test_case03(self):
        url="http://www.baidu.com"
        resp=requests.get(url)
        print resp.text
    def test_case04(self):
       url="http://127.0.0.1:5000/member"
       resp=requests.get(url)
       print resp.text
    def test_case05(self):
        nmu1=1
        nmu2=2
        exp_result=3
        act_result=nmu1+nmu2
        self.assertEqual(exp_result, act_result, "exp:%s+%s=%s act:=%s"%(nmu1,nmu2,act_result,exp_result))
    def test_case06(self):
        nmu1=1
        nmu2=2
        exp_result=3
        act_result=nmu1+nmu2
        self.assertEqual(exp_result, act_result, "exp:%s+%s=%s act:=%s"%(nmu1,nmu2,act_result,exp_result))

if __name__ == '__main__':
    unittest.main()

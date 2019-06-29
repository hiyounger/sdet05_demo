#encoding:utf-8
import unittest

from pengyunhao.work0626.shopping.member import MemberUtils


class TestMemberUtils(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print ("测试开始")
    @classmethod
    def tearDownClass(cls):
        print ("测试清理")

    def setUp(self):
        print ("测试1开始")
    def tearDown(self):
        print ("测试1清理")
    def test_getMemberDisc0(self):
        tel="5345"
        #实际结果
        act_discount=MemberUtils.getMemberDisc(tel)
        #期望结果
        exp_discount=1
        #比较实际结果和期望结果
        self.assertEqual(act_discount,exp_discount)

    def test_getMemberDisc1(self):
        tel="1234"
        #实际结果
        act_discount=MemberUtils.getMemberDisc(tel)
        #期望结果
        exp_discount=0.9
        #比较实际结果和期望结果
        self.assertEqual(act_discount,exp_discount)


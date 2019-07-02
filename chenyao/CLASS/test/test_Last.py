import unittest

from chenyao.CLASS.members import MemberHelper

class TestMemberHelperLast(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('1.setup test class')
    @classmethod
    def tearDownClass(cls):
        print('2.teardown test class')

    def setUp(self):
        print('3.set up test case')
    def tearDown(self):
        print('4.tear down test case')

    def test_case01_Last_msg(self):
        tel_last=5672
        act_msg=MemberHelper.member_get(tel_last)
        exp_msg=1
        self.assertEqual(exp_msg, act_msg)
    # def test_case02_Last_msg(self):
    #     tel_last=567a
    #     act_msg=MemberHelper.member_get(tel_last)
    #     exp_msg=1
    #     self.assertEqual(exp_msg, act_msg)
    def test_case03_Last_msg(self):
        tel_last=1111
        act_msg=MemberHelper.member_get(tel_last)
        exp_msg=False
        self.assertEqual(exp_msg, act_msg)
    def test_case04_Last_msg(self):
        tel_last=672
        act_msg=MemberHelper.member_get(tel_last)
        exp_msg=False
        self.assertEqual(exp_msg, act_msg)
    def test_case05_Last_msg(self):
        tel_last=-5672
        act_msg=MemberHelper.member_get(tel_last)
        exp_msg=False
        self.assertEqual(exp_msg, act_msg)

if __name__ == '__main__':
    unittest.main()

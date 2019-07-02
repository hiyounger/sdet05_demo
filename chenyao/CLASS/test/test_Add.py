import unittest

from chenyao.CLASS.members import MemberHelper

class TestMemberHelperAdd(unittest.TestCase):
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

    def test_case01_Add(self):
        tel=13312345671
        act_msg=MemberHelper.add_member_by_tel(tel)
        exp_msg=False
        self.assertEqual(exp_msg, act_msg)

    def test_case02_Add(self):
        tel = 133123456
        act_msg = MemberHelper.add_member_by_tel(tel)
        exp_msg = 1
        self.assertEqual(exp_msg, act_msg)
    def test_case03_Add(self):
        tel=13312345678
        act_msg=MemberHelper.add_member_by_tel(tel)
        exp_msg=1
        self.assertEqual(exp_msg, act_msg)
    def test_case04_Add(self):
        tel=0
        act_msg=MemberHelper.add_member_by_tel(tel)
        exp_msg=1
        self.assertEqual(exp_msg, act_msg)
    # def test_case05_Add(self):
    #     tel=
    #     act_msg=MemberHelper.add_member_by_tel(tel)
    #     exp_msg=1
    #     self.assertEqual(exp_msg, act_msg)
    # def test_case06_Add(self):
    #     tel =a
    #     act_msg = MemberHelper.add_member_by_tel(tel)
    #     exp_msg = 1
    #     self.assertEqual(exp_msg, act_msg)
    def test_case07_Add(self):
        tel=-1000
        act_msg=MemberHelper.add_member_by_tel(tel)
        exp_msg=1
        self.assertEqual(exp_msg, act_msg)
    def test_case08_Add(self):
        tel=13312345675
        act_msg=MemberHelper.add_member_by_tel(tel)
        exp_msg=1
        self.assertEqual(exp_msg, act_msg)

if __name__ == '__main__':
    unittest.main()

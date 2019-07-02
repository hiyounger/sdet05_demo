import unittest

from chenyao.CLASS.members import MemberHelper

class TestMemberHepler_Delete(unittest.TestCase):
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

    def test_case01_Delete(self):
        tel=13312345673
        disc=1.0
        act_Del=MemberHelper.member_delete(tel,disc)
        exp_Del=1
        self.assertEqual(exp_Del, act_Del)
    def test_case02_Delete(self):
        tel=13312345676
        disc=1.0
        act_Del=MemberHelper.member_delete(tel,disc)
        exp_Del=False
        self.assertEqual(exp_Del, act_Del)
    def test_case03_Delete(self):
        tel=133123456
        disc=1.0
        act_Del=MemberHelper.member_delete(tel,disc)
        exp_Del=False
        self.assertEqual(exp_Del, act_Del)
    def test_case04_Delete(self):
        tel=13312345678
        disc=1.0
        act_Del=MemberHelper.member_delete(tel,disc)
        exp_Del=False
        self.assertEqual(exp_Del, act_Del)
    def test_case05_Delete(self):
        tel=-1000
        disc=1.0
        act_Del=MemberHelper.member_delete(tel,disc)
        exp_Del=False
        self.assertEqual(exp_Del, act_Del)

if __name__ == '__main__':
    unittest.main()

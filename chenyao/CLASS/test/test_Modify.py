import unittest

from chenyao.CLASS.members import MemberHelper

class TestMemberHelperModify(unittest.TestCase):
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

    def test_case01_Modify(self):
        tel=13312345674
        disc=0.5
        act_mem=MemberHelper.member_mod(tel,disc)
        exp_mem=1
        self.assertEqual(exp_mem, act_mem)
    def test_case02_Modify(self):
        tel=13312345674
        disc=0
        act_mem=MemberHelper.member_mod(tel,disc)
        exp_mem=1
        self.assertEqual(exp_mem, act_mem)
    def test_case03_Modify(self):
        tel=13312345674
        disc=-1
        act_mem=MemberHelper.member_mod(tel,disc)
        exp_mem=1
        self.assertEqual(exp_mem, act_mem)
    def test_case04_Modify(self):
        tel=13312345674
        disc=a
        act_mem=MemberHelper.member_mod(tel,disc)
        exp_mem=False
        self.assertEqual(exp_mem, act_mem)
    def test_case05_Modify(self):
        tel=13312345677
        disc=0.5
        act_mem=MemberHelper.member_mod(tel,disc)
        exp_mem=False
        self.assertEqual(exp_mem, act_mem)
    def test_case06_Modify(self):
        tel=133123456
        disc=0.5
        act_mem=MemberHelper.member_mod(tel,disc)
        exp_mem=False
        self.assertEqual(exp_mem, act_mem)
    def test_case07_Modify(self):
        tel=133123456789
        disc=-1
        act_mem=MemberHelper.member_mod(tel,disc)
        exp_mem=False
        self.assertEqual(exp_mem, act_mem)
if __name__ == '__main__':
    unittest.main()

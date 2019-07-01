import unittest

from chenyao.CLASS.members import MemberHelper

class TestMemberHelper(unittest.TestCase):
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

    def test_case01_getdefaultdisc(self):
        print('5.test case01')
        tel='13312345671'
        act_disc=MemberHelper.get_member_discount(tel)
        exp_disc=0.9
        self.assertEqual(exp_disc,act_disc )
    def test_case02_getdefaultdisc(self):
        print('6.test case02')
        tel='13312345672'
        act_disc=MemberHelper.get_member_discount(tel)
        exp_disc=0.8
        self.assertEqual(exp_disc,act_disc )

if __name__ == '__main__':
    unittest.main()

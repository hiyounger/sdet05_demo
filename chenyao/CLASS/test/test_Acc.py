import unittest

from chenyao.CLASS.members import MemberHelper

class TestMemberHelperAcc(unittest.TestCase):
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

    def test_case01_Acc(self):
        tel=13312345673
        score=1000
        act_mem=MemberHelper.score_acc(tel,score)
        exp_mem=1
        self.assertEqual(exp_mem,act_mem )


if __name__ == '__main__':
    unittest.main()

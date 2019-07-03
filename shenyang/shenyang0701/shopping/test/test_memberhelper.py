import unittest

from benchmark1.shopping.members import MemberHelper


class TestMemberHelper(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("1, Steup test class")

    @classmethod
    def tearDownClass(cls):
        print("2, Tear Down test class")

    def setUp(self):
        print("3, Set up test case")

    def tearDown(self):
        print("4, Tear down test case")

    def test_case01_getdefalutdisc(self):
        print("5, test case01")
        tel = '199999999'
        act_disc = MemberHelper.get_memeber_discount(tel)
        exp_disc = 1
        self.assertEqual(exp_disc, act_disc)

    def test_case02_get0p9disc(self):
        print("6, test case02")
        tel = '13312345675'
        act_disc = MemberHelper.get_memeber_discount(tel)
        exp_disc = 0.9
        self.assertEqual(exp_disc, act_disc)


if __name__ == '__main__':
    unittest.main()

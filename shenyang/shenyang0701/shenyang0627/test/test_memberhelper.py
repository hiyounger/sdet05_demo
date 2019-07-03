import unittest

from benchmark1.shenyang0627.shopping import MemberHelper
class TestMemberHelper(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print "1.Setup test class"

    @classmethod
    def tearDownClass(cls):
        print "2.Tear Down test class"

    def setUp(self):
        print "3.Set up test class"

    def tearDown(self):
        print "4.Tear down test class"

    def test_case01_getdefaultdisc(self):
        print "5.test_case01"
        tel='1388686868'
        act_disc= MemberHelper.get_member_discount(tel)
        exp_disc= 0.5
        self.assertEqual(act_disc, exp_disc)

    def test_case02_get0pdisc(self):
        print "6.test_case02"
        tel = '13912345671'
        act_disc = MemberHelper.get_member_discount(tel)
        exp_disc = 0.8
        self.assertEqual(act_disc, exp_disc)

if __name__ == '__main__':
    unittest.main()

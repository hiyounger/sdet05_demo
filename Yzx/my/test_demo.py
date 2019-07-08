#encoding:utf-8
import unittest


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print ("setUpClass:类前置条件")
    def setUp(self):
        print ('setUp:方法前置条件')
    @classmethod
    def tearDownClass(cls):
        print ('tearDown:类后置方法')
    def tearDown(self):
        print ('teardown:方法前置条件')
    def test_something00(self):
        exp=10
        act=10
        self.assertEqual(exp, act)
    def test_something01(self):
        exp=10
        act=10
        self.assertEqual(exp, act)
    def test_something02(self):
        exp=10
        act=10
        self.assertEqual(exp, act)
    def test_something03(self):
        exp=10
        act=10
        self.assertEqual(exp, act)


if __name__ == '__main__':
    unittest.main()

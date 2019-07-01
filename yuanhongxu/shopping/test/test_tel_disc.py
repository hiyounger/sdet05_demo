#-*- encoding:utf-8 -*-
import unittest

from yuanhongxu.shopping.huiyuan import huiyuan_help

class TestHuiYuanHelp(unittest.TestCase):

    def setUp(self):
        print ("测试准备")

    def tearDown(self):
        print ("测试收尾")

    @classmethod
    def setUpClass(cls):
        print ("测试总准备")

    @classmethod
    def tearDownClass(cls):
        print ("测试总收尾")



    def test_case01(self):
        print ("case01")
        tel="13512345678"
        act_disc=huiyuan_help.tel_disc(tel)
        exp_disc=0.8
        self.assertEqual(act_disc, exp_disc)

    def test_case02(self):
        print ("case02")
        tel="13512345679"
        act_disc=huiyuan_help.tel_disc(tel)
        exp_disc=0.9
        self.assertEqual(act_disc, exp_disc)

    def test_case03(self):
        print ("case03")
        tel="13512345670"
        act_disc=huiyuan_help.tel_disc(tel)
        exp_disc=1
        self.assertEqual(act_disc, exp_disc)

    def test_case04(self):
        print ("case04")
        tel="123"
        act_disc=huiyuan_help.tel_disc(tel)
        exp_disc=0.9
        self.assertEqual(act_disc, exp_disc)

    def test_case05(self):
        print ("case05")
        tel="aaa"
        act_disc=huiyuan_help.tel_disc(tel)
        exp_disc=1
        self.assertEqual(act_disc, exp_disc)

    def test_case06(self):
        print ("case06")
        tel="!"
        act_disc=huiyuan_help.tel_disc(tel)
        exp_disc=1
        self.assertEqual(act_disc, exp_disc)



if __name__ == '__main__':
    unittest.main()

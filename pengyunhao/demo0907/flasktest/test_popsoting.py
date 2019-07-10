#encoding:utf-8

import unittest
from pengyunhao.demo0907 import popsoting

class testPopsoting(unittest.TestCase):
    list = [6, 8, 10, 1, 7, 3, 9]
    a="desc"
    b="asc"
    def test_popsoting(self):
        testPopsoting.list.sort()
        exp_result=testPopsoting.list
        print exp_result
        asc_result=popsoting.listsorting(testPopsoting.list,testPopsoting.a)
        self.assertEqual(exp_result,asc_result)

    def test_popsoting02(self):
        testPopsoting.list.sort(reverse=True)
        exp_result=testPopsoting.list
        print testPopsoting.list
        asc_result = popsoting.listsorting(testPopsoting.list, testPopsoting.b)
        self.assertEqual(exp_result, asc_result)
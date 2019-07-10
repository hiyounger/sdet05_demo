import unittest
from Yzx.myperson import popsoting

class TestPopsoting(unittest.TestCase):
    def test_popsotring_desc(self):
        list1 = [6, 8, 10, 1, 7, 3, 9]
        exp=[1, 3, 6, 7, 8, 9, 10]
        act=popsoting.listsorting(list1,'desc')
        self.assertEqual(exp, act)

    def test_popsotring_asc(self):
        list1 = [6, 8, 10, 1, 7, 3, 9]
        exp = [1, 3, 6, 7, 8, 9, 10]
        act = popsoting.listsorting(list1, 'asc')
        self.assertEqual(exp, act,'exp:=%s act:=%s'%(act,exp))


if __name__ == '__main__':
    unittest.main()

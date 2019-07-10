import unittest
from yuanhongxu.popsoting import popsoting

class MyTestCase(unittest.TestCase):
    def test_01(self):
        start_list = [6, 8, 10, 1, 7, 3, 9]
        exp_result=popsoting.listsorting(start_list,"asc")
        act_result=[1, 3, 6, 7, 8, 9, 10]
        self.assertEqual(exp_result, act_result)

    def test_02(self):
        start_list = [6, 8, 10, 1, 7, 3, 9]
        exp_result=popsoting.listsorting(start_list,"desc")
        act_result=[10, 9, 8, 7, 6, 3, 1]
        self.assertEqual(exp_result, act_result)


if __name__ == '__main__':
    unittest.main()

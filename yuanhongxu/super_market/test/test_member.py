import unittest
from yuanhongxu.super_market.model.members import members

class MyTestCase(unittest.TestCase):
    def test_something(self):
        act_reust=len(members.get_all_member())
        exp_reust=2
        self.assertEqual(act_reust, exp_reust)


if __name__ == '__main__':
    unittest.main()

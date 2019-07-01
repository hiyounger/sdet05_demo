import unittest
from Yzx.flask.model.member import Mermbers


class MyTestCase(unittest.TestCase):
    def test_case01_testGetAllMembers(self):
        act_result = len(Mermbers.get_members())
        exp_result = 2
        self.assertEqual(exp_result, act_result)


if __name__ == '__main__':
    unittest.main()

import unittest

from Yzx.Person.homework0628.shop.members import Members

class TestMemberLastFour(unittest.TestCase):
    def test_get_member_last_four_tel_case01(self):
        exp=Members.get_mermber_by_tell_last_four(1000)
        act=False
        self.assertEqual(exp, act)


if __name__ == '__main__':
    unittest.main()

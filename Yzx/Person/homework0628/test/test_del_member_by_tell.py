import unittest

from Yzx.Person.homework0628.shop.members import Members

class TestDelMemberByTell(unittest.TestCase):
    def test_del_member_by_tell_case01(self):
        exp=False
        act=Members.del_member_by_tell(1884587168)
        self.assertEqual(exp, act)


if __name__ == '__main__':
    unittest.main()

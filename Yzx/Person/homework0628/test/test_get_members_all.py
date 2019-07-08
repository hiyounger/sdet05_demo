import unittest

from Yzx.Person.homework0628.shop.members import Members

class TestAllMembers(unittest.TestCase):

    def test_all_mermbers_case01(self):
        exp=1
        act=Members.get_members_all()
        self.assertEqual(exp, act)


if __name__ == '__main__':
    unittest.main()

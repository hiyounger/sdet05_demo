import unittest

from YZX.homework0628.shop.members import Members

class TestAddMember(unittest.TestCase):

    def test_addcase01(self):
        tel='18845871680'
        exp_add=False
        act_add=Members.add_member_by_tell(tel)
        self.assertEqual(exp_add, exp_add)
    def test_addcase02(self):
        tel='1'
        exp_add=False
        act_add=Members.add_member_by_tell(tel)
        self.assertEqual(exp_add, exp_add)
if __name__ == '__main__':
    unittest.main()

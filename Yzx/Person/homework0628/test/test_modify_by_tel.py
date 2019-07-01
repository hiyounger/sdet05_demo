import unittest

from YZX.homework0628.shop.members import Members

class TestModifyMemberByTel(unittest.TestCase):
    def test_modify_mermber_by_tel_case01(self):
        exp=False
        act=Members.modify_member_by_tel(1884587168,0.3)
        self.assertEqual(exp, act)




if __name__ == '__main__':
    unittest.main()

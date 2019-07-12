import unittest
from WYF.super_market.model.members import Member


class MyTestCase(unittest.TestCase):
    def test_all_members01(self):
        exp = 4
        act = len(Member.get_all_members())
        self.assertEqual(act, exp)

    def test_members01_by_tel(self):
        tel = '18812345672'
        exp = [{'id': 2, 'tel': '18812345672', 'discount': 0.9, 'state': 1, 'jifen': 1500}]
        act = (Member.get_member_last_four(tel))
        self.assertEqual(act, exp)

    def test_members02_by_tel(self):
        tel = '45673'
        exp = [{'id': 3, 'tel': '18812345673', 'discount': 0.8, 'state': 1, 'jifen': 2000},
               {'id': 4, 'tel': '18832145673', 'discount': 0.8, 'state': 1, 'jifen': 2000}]
        act = Member.get_member_last_four(tel)
        self.assertEqual(act, exp)

    def test_members01_by_id(self):
        uid = 1
        exp = [{'id':1,'tel':'18812345671','discount':0.98,'state':1,'jifen':1000}]
        act = Member.get_member_by_id(uid)

        self.assertEqual(exp,act)

    def test_members01_add(self):
        tel='123456768912'
        exp = {'id':5,'tel':'123456768912','discount':1}
        act = Member.add_member(tel)

        self.assertEqual(exp,act)



if __name__ == '__main__':
    unittest.main()

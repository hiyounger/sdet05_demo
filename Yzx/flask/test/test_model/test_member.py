import unittest
from Yzx.flask.model.member import Mermbers


class MyTestCase(unittest.TestCase):
    def test_case01_testGetAllMembers(self):
        act_result = len(Mermbers.get_members())
        exp_result = 3
        self.assertEqual(exp_result, act_result)

    def test_case02_testGetMembersByTel(self):
        tel = "5099"
        act_result = Mermbers.get_members_by_tel(tel)
        exp_result = [{'id': '2', 'tel': '18845095099', 'disc': 0.1, 'state': 1, 'points': 0000},
                      {'id': '3', 'tel': '18845195099', 'disc': 0.1, 'state': 1, 'points': 0000}]
        self.assertEqual(exp_result, act_result)

    def test_case03_testGetMemberByUid(self):
        uid = "1"
        act_result = Mermbers.get_member_by_uid(uid)
        exp_result = [{'id': '1', 'tel': '18845871680', 'disc': 0.9, 'state': 1, 'points': 0000}]
        self.assertEqual(exp_result, act_result)


if __name__ == '__main__':
    unittest.main()

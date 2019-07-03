import unittest
from tyj.super_market.model.members_demo import get_members


class MyTestCase(unittest.TestCase):
    def test_case101(self):
        act_reselt = len(get_members.all_member())
        exp_reselt = 5
        self.assertEqual(exp_reselt, act_reselt)

    def test_case201(self):
        targer_tel = '13112345670'
        act_reselt = get_members.get_member_by_tel(targer_tel)
        exp_reselt = [{'id': '1', 'tel': '13112345670', 'disc': 0.98}]
        self.assertEqual(exp_reselt, act_reselt)

    def test_case202(self):
        targer_tel = '5671'
        act_reselt = get_members.get_member_by_tel(targer_tel)
        exp_reselt = [{'id': '2', 'tel': '13112345671', 'disc': 0.9}, {'id': '5', 'tel': '13212345671', 'disc': 0.8}]
        self.assertEqual(exp_reselt, act_reselt)

    def test_case301(self):
        targer_uid = '1'
        act_reselt = get_members.get_member_by_uid(targer_uid)
        exp_reselt = [{'id': '1', 'tel': '13112345670', 'disc': 0.98}]
        self.assertEqual(exp_reselt, act_reselt)


if __name__ == '__main__':
    unittest.main()

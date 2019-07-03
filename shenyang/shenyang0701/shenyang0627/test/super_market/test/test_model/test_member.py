import unittest

from shenyang.shenyang0701.shenyang0627.test.super_market.model.members import Member


class MyTestCase(unittest.TestCase):

    def test_case01_testGetAllMembers(self):
        act_result = len(Member.get_all_members())
        exp_result = 4
        self.assertEqual(exp_result, act_result)

    def test_case_02_testGetMemberByTel(self):
        target_tel = '13912345671'
        exp_result = [{'uid': '1', 'tel': '13912345671', 'disc': 0.8}]
        act_result = Member.get_members_by_tel(target_tel)
        self.assertEqual(exp_result, act_result)

    def test_case_03_testGetMemberByTel4(self):
        target_tel = '5672'
        exp_result = [{'uid': '2', 'tel': '13912345672', 'disc': 0.9}, {'uid': '5', 'tel': '13912345672', 'disc': 0.9}]
        act_result = Member.get_members_by_tel(target_tel)
        self.assertEqual(exp_result, act_result)

    def test_case_04_testGetMemberByUid(self):
        target_uid = '1'
        exp_result = [{'uid': '1', 'tel': '13912345672', 'disc': 0.9}]
        act_result = Member.get_members_by_tel(target_uid)
        self.assertEqual(exp_result, act_result)


if __name__ == '__main__':
            unittest.main()

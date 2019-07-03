#encoding:utf-8
import unittest
from jiawei.super_market.model.members import Member


class MyTestCase(unittest.TestCase):
    def test_case01_testGetAllMember(self):
        act_result = len(Member.get_all_member())
        exp_result = 5
        self.assertEqual(exp_result, act_result)

    def test_case201_testGetMemberByTel(self):
        target_tel = "13312345678"
        exp_result = [{'uid': '1', 'tel': '13312345678', 'disc': 0.9, 'state': "live", 'itg': 5080}]
        act_result = Member.get_member_by_tel(target_tel)
        self.assertEqual(exp_result, act_result)

    def test_case202_testGetMemberByTel(self):
        target_tel = "5678"
        exp_result = [{'uid': '1', 'tel': '13312345678', 'disc': 0.9, 'state': "live", 'itg': 5080},
                      {'uid': '5', 'tel': '13412345678', 'disc': 0.9, 'state': "live", 'itg': 5080}]
        act_result = Member.get_member_by_tel(target_tel)
        self.assertEqual(exp_result, act_result)

    def test_case301_getMemberByUid(self):
        target_uid = '1'
        exp_result = [{'uid': '1', 'tel': '13312345678', 'disc': 0.9, 'state': "live", 'itg': 5080}]
        act_result = Member.get_member_by_uid(target_uid)
        self.assertEqual(exp_result, act_result)


if __name__ == '__main__':
    unittest.main()

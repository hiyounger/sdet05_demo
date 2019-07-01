import unittest

from qsong.super_market.model.members import Member


class MyTestCase(unittest.TestCase):

    def test_case101_testGetAllMembers(self):
        act_result = len(Member.get_all_members())
        exp_result = 5
        self.assertEqual(exp_result, act_result)

    def test_case201_testGetMemberByTel(self):
        target_tel = "18812345672"
        exp_result = [{'id': '1', 'tel': "18812345672", 'discount': 0.95}]
        act_result = Member.get_members_by_tel(target_tel)
        self.assertEqual(exp_result, act_result)

    def test_case202_testGetMemberByTel4(self):
        target_tel = "5671"
        exp_result = [{'id': '4', 'tel': "18812345671", 'discount': 0.8},{'id': '5', 'tel': "18811345671", 'discount': 0.8}]
        act_result = Member.get_members_by_tel(target_tel)
        self.assertEqual(exp_result, act_result)

    def test_case301_getMemberByUid(self):
        target_uid = "1"
        exp_result = [{'id': '1', 'tel': "18812345672", 'discount': 0.95}]
        act_result = Member.get_members_by_uid(target_uid)
        self.assertEqual(exp_result, act_result)


if __name__ == '__main__':
    unittest.main()

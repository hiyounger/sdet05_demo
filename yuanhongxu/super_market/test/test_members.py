import unittest
from yuanhongxu.super_market.model.members import member


class MyTestCase(unittest.TestCase):

    def test_case101_testGetAllMember(self):
        act_result = len(member.get_all_member())
        exp_result = 3
        self.assertEqual(act_result, exp_result)

    def test_case201_testGetMemberByTel(self):
        tel = '13512345678'
        act_result = member.get_member_by_tel(tel)
        exp_result = [{'status': 'inactive', 'disc': 0.8, 'tel': '13512345678', 'id': '1', 'jifen': 100}]
        self.assertEqual(act_result, exp_result)

    def test_case202_testGetMemberByTel(self):
        tel = "5678"
        act_result = member.get_member_by_tel(tel)
        exp_result = [{'status': 'inactive', 'disc': 0.8, 'tel': '13512345678', 'id': '1', 'jifen': 100},
                      {"id": "2", "tel": "13513345678", "disc": 0.8, "status": "inactive", "jifen": 100}]
        self.assertEqual(act_result, exp_result)

    def test_case301_testGetMemberById(self):
        uid = "1"
        act_result = member.get_member_by_uid(uid)
        exp_result = [{'status': 'inactive', 'disc': 0.8, 'tel': '13512345678', 'id': '1', 'jifen': 100}]
        self.assertEqual(act_result, exp_result)

    def test_case401_testAddMember(self):
        tel = "13587654321"
        act_result = member.add_member(tel)
        exp_result = {"id": "4", "tel": "13587654321", "disc": 1.0, "status": "active", "jifen": 0}
        self.assertEqual(act_result, exp_result)


if __name__ == '__main__':
    unittest.main()

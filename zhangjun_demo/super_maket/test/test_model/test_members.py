import unittest
from zhangjun_demo.super_maket.model.members_zj import Member


class MyTestCase(unittest.TestCase):
    def test_case01(self):
        act_request = len(Member.get_all_members())
        exp_request = 4
        self.assertEqual(exp_request, act_request)

    def test_case02_GetMemberByTel(self):
        tel = '18812345673'
        exp_request = [{'id': '3', 'tel': '18812345673', 'discount': 0.85, 'sta': 1}]
        act_request = Member.get_member_list(tel)
        self.assertEqual(exp_request, act_request)

    def test_case03_GetMemberByTelEndswith(self):
        tel = '5673'
        exp_request = [{'id': '3', 'tel': '18812345673', 'discount': 0.85, 'sta': 1},{'id': '4', 'tel': '18813445673', 'discount': 0.85, 'sta': 1}]
        act_request = Member.get_member_list(tel)
        self.assertEqual(exp_request, act_request)

    def test_case04_GetMemberByUid(self):
        uid ='3'
        exp_request = [{'id': '3', 'tel': '18812345673', 'discount': 0.85, 'sta': 1}]
        act_request = Member.get_member_list_by_id(uid)
        self.assertEqual(exp_request, act_request)

    def test_case05_AddVip(self):
        usel_tel='18821345677'
        exp_request = {'id': '5', 'tel': '18821345677', 'discount': 1.0, 'sta': 1}
        act_request = Member.add_vip(usel_tel)
        print (act_request)
        self.assertEqual(exp_request, act_request)


if __name__ == '__main__':
    unittest.main()

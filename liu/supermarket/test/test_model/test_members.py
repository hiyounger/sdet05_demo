import unittest
from liu.supermarket.model.membersbak import Member

class test_case_001(unittest.TestCase):
    def test_case_001_testGetAllMembers(self):
        acu_result=len(Member.get_all_members())
        exp_result=3
        self.assertEqual(acu_result,exp_result)


    def test_case_101_testGetMemberByTel(self):
        target_tel='18812345678'
        acu_result = Member.get_member_by_tel(target_tel)
        exp_result =[{'id':'1','tel':'18812345678','disc':0.9,'score':100,'active':1}]
        self.assertEqual(acu_result, exp_result)

    def test_case_102_testGetMemberByTel4(self):
        target_tel = '5678'
        acu_result = Member.get_member_by_tel(target_tel)
        exp_result = [{'id':'1','tel':'18812345678','disc':0.9,'score':100,'active':1},{'id':'2','tel':'18712345678','disc':0.8,'score':100,'active':1}]
        self.assertEqual(acu_result, exp_result)

    def test_case_201_testGetMemberByID(self):
        target_uid = '2'
        acu_result = Member.get_member_by_uid(target_uid)
        exp_result = [{'id': '2', 'tel': '18712345678', 'disc': 0.8,'score':100,'active':1}]
        self.assertEqual(acu_result, exp_result)

    def test_case_301_AddMemberByTel(self):
        target_utel='18812345670'
        acu_result = Member.add_member_by_tel(target_utel)
        exp_result ={'id': '4', 'tel': '18812345670', 'disc': 1.0,'score':100,'active':1}
        self.assertEqual(acu_result, exp_result)


if __name__ == '__main__':
    unittest.main()

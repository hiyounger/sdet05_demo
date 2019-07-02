import unittest

from chenyao.supermarket.model.member import Members

class MyTestCase(unittest.TestCase):

    def test_case101_Test_Model(self):
        act_result=len(Members.show_members())
        exp_result=5
        self.assertEqual(exp_result, act_result)

    def test_case201_Test_Tel(self):
        target_tel='13312345671'
        act_result=[{'id': '1', 'tel': '13312345671', 'disc': 0.9, 'score': 0}]
        exp_result=Members.show_members_tel(target_tel)
        self.assertEqual(exp_result, act_result)
    def test_case202_Test_Last(self):
        target_tel=5671
        act_result=[{'id': '1', 'tel': '13312345671', 'disc': 0.9, 'score': 0},{'id': '5', 'tel': '13311145671', 'disc': 0.9, 'score': 0}]
        exp_result=Members.show_members_tel(str(target_tel))
        self.assertEqual(exp_result, act_result)

    def test_case301_Test_Model_Tel(self):
        target_uid='1'
        act_result=[{'id': '1', 'tel': '13312345671', 'disc': 0.9, 'score': 0}]
        exp_result=Members.show_members_uid(target_uid)
        self.assertEqual(exp_result, act_result)

if __name__ == '__main__':
    unittest.main()

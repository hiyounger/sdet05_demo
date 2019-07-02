#encoding:utf-8
import unittest

from pengyunhao.flask.shipping.model.members import Member
from pengyunhao.flask.shipping.db import mysql

class MyTestCase(unittest.TestCase):
    def testGetAllMember(self):
        #实际
        actResult=Member.getAllMember()
        #期望
        expResult=mysql.member
        self.assertEqual(actResult,expResult)

    def testGetMemvetByTel(self):
        tel="12346789"
        expResult=[{"id": 1, "tel": "12346789", "discount": 0.9}]
        actResult=Member.getMemberByTel(tel)
        self.assertEqual(expResult,actResult)

    def testGetMemvetByLastTel(self):
        tel="4544"
        expResult=[{"id": "2", "tel": "54354544", "discount": 0.9},
                    {"id": "3", "tel": "54544544", "discount": 0.9}]
        actResult=Member.getMemberByTel(tel)
        self.assertEqual(expResult,actResult)

    def testUpdateMember(self):
        uid="1"
        expResult=[{"id": "1", "tel": "12346789", "discount": 0.9}]
        actResult=Member.UpdateMember(uid)
        self.assertEqual(expResult,actResult)


if __name__=="__main__":
    unittest.main()
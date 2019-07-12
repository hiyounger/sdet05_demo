# coding:utf-8
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()
class Student():
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(11), unique=True, nullable=False)
    password = db.Column(db.String(11), nullable=False)
    __tablename__ = 'students'

    @classmethod
    def add_student(cls, username):
        student = Student()
        student.username = username
        ret_dic={'uid':1, "username":"xiaoming", "password":"123456"}
        return ret_dic

    @classmethod
    def get_student_by_uid(cls,uid):
        stu_list=[]
        student = Student.query.filter(Student.uid.endswith(uid)).first()
        student_info={'uid':student.uid, "username":student.username, "password":student.password}
        stu_list.append(student_info)
        ret_dic = {
            'new_member': student_info,
            'count': len(student_info),
            'members': student_info
        }
        return ret_dic

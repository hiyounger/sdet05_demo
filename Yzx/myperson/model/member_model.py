# encoding:utf-8
from flask_sqlalchemy import SQLAlchemy
# dic=[
#     {
#         'uid':1, "username":"xiaoming", "password":"123456"
#     },
#     {
#         'uid': 2, "username": "xiaoming", "password": "123456"
#     },
# ]
db = SQLAlchemy()
class Member(db.Model):
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String)

    __tablename__ = "memeberUser"

    # 增加用户
    @classmethod
    def add_members_by(cls, username, password):
        member_list = []
        list = {
            'uid': len(dic) + 1, "username": username, "password": password
        }
        member_list.append(list)
        ret_dic = {
            'member': member_list
        }
        return ret_dic

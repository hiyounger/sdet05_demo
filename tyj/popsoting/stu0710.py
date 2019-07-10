# encoding:utf-8
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
#
#
class Dict():
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), unique=True, nullable=False)

    __tablename__ = "dic"


    @classmethod
    def add_stu(cls, username,password):
        stu = Dict()
        stu.username = username
        stu.password = password
        db.session.add(stu)
        db.session.commit()
        ret_dic = cls.get_by_uid(username)
        return ret_dic

    @classmethod
    def get_by_uid(cls,uid):


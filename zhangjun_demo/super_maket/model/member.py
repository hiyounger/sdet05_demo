#encoding:utf-8
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class Member(db.Model):

    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tel= db.Column(db.String(11), unique=True,nullable=False)
    discount = db.Column(db.FLOAT,nullable=False,default=1)
    score = db.Column(db.Integer, nullable=False,default=0)
    active=db.Column(db.Integer, nullable=False,default=1)
    __tablename__ = "members"

    @classmethod
    def add_member(cls,tel):
        mem=Member
        mem.tel=tel
        db.session.add(mem)
        db.session.commit()
        return {'haha':'hehe'}

    @classmethod
    def get_member_list_by_id(cls, uid):
        member_list = []
        for member in Member.members:
            if member['uid'] == uid:
                member_list.append(member)
                break
                tar_members = {
                    'count': len(member_list),
                    'members': member_list}
                return tar_members
            else:
                print('你的输入有误,请重新输入!')








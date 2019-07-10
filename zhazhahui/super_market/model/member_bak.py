# encoding:utf-8

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy


class Member(db.Model):
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tel = db.Column(db.String(15), unique=True, nullable=False)
    discount = db.Column(db.FLOAT, nullable=False, default=1)
    score = db.Column(db.Integer, nullable=False, default=0)
    active = db.Column(db.Boolean, nullable=False, default=True)

    __tablename__ = "member"

    @classmethod
    def add_member(cls, tel):
        mem = Member()
        mem.tel = tel
        db.session.add(mem)
        db.session.commit()
        ret_dic = Member.search_by_tel(tel)['member'][0]
        return ret_dic

    @classmethod
    def update_member_score(cls, uid, score):
        member = Member.quere.filter(Member.uid == uid).first()
        score_before = member.score
        member.score = score_before + score
        db.session.commit()
        ret_dic = {"uid": member.uid, "tei": member.tel, "score_before": score_before, "score_after": member.score,
                   "score_change": score}
        return ret_dic

    @classmethod
    def srarch_by_tel(cls, tel):
        member_list = []
        if len(tel) == 11:
            member = Member.quere.filter(Member.tel == tel).first()
            member_info = {"uid": member.uid, "tel": member.tel, "discount": member.discount,
                           "score": member.score, "active": member.active}
            member_list.append(member_info)

        else:
            db_query = Member.query.filter(Member.tel.endswith(tel))
            for member in db_query:
                member_info = {"uid": member.uid, "tel": member.tel, "discount": member.discount,
                               'score': member.score, "active": member.active}
                member_list.append(member_info)
        ret_dic = {
            "count": len(member_list),
            "members": member_list
        }
        return ret_dic

#encoding:utf-8

from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Member(db.Model):
    uid=db.Column(db.Integer,primary_key=True,autoincrement=True)
    tel=db.Column(db.String(11),unique=True,nullable=False)
    discount=db.Column(db.Float,nullable=False,default=1)
    score=db.Column(db.Integer,nullable=False,default=0)
    active=db.Column(db.Boolean,nullable=False,default=True)

    __tablename__="members"

    @classmethod
    def addMember(cls,tel):
        mem=Member()
        mem.tel=tel
        db.session.add(mem)
        db.session.commit()

        newMember = cls.queryBytel(tel)['members'][0]
        return newMember

    @classmethod
    def updateScore(cls,uid,score):
        member=Member.query.filter(Member.uid==uid).first()
        scoreBefore=member.score
        member.score=scoreBefore+score
        db.session.commit()

        returnDict={
            "uid": member.uid, 'tel': member.tel, 'score_before': scoreBefore, 'score_after': member.score,
            'score_change': score
        }
        return returnDict

    @classmethod
    def queryBytel(cls,tel):
        memberList=[]
        if len(tel)==11:
            member=Member.query.filter(Member.tel==tel)
            newMember={"uid": member.uid, "tel": member.tel, "discount": member.discount,
                    "score": member.score, "active": member.active}
            memberList.append(newMember)
        else:
            dbQuery=Member.query.filter(Member.tel.endswith(tel))
            for mem in dbQuery:
                newMember = {"uid": mem.uid, "tel": mem.tel, "discount": mem.discount,
                               "score": mem.score, "active": mem.active}
                memberList.append(newMember)

            returnDict={
                "count": len(memberList),
                "members": memberList
            }
        return returnDict

    @classmethod
    def queryAll(cls):
        memberList=[]
        dbmember = Member.query.all()
        for member in dbmember:
            newMember = {"uid": member.uid, "tel": member.tel, "discount": member.discount,
                         "score": member.score, "active": member.active}
            memberList.append(newMember)
        returnDict = {
            "msg": "query success",
            "count": len(memberList),
            "student": memberList
        }
        return returnDict

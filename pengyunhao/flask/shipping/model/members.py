#encoding:utf-8

from pengyunhao.flask.shipping.db import mysql

class Member():
    @classmethod
    def getAllMember(cls):
        return mysql.member

    @classmethod
    def getMemberByTel(cls,tel):
        memberList=[]
        for member in mysql.member:
            if member["tel"]==tel:
                memberList.append(member)
                break
            elif member["tel"].endswith(tel):
                memberList.append(member)
        return memberList

    @classmethod
    def getMemberByUid(cls,uid):
        memberList=[]
        for member in mysql.member:
            if member["id"]==uid:
                memberList.append(member)
                break
        return memberList

    @classmethod
    def AddMember(cls,tel):
        #tel=str(tel)
        newMember={"tel":tel,"discount":1}
        newMember["uid"]=str(len(newMember)+2)
        mysql.member.append(newMember)
        return newMember
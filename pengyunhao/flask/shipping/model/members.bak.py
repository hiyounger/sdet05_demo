#encoding:utf-8

from pengyunhao.flask.shipping.db import mysql

class Member():
    @classmethod
    def getAllMember(cls):
        dictMember={"member":mysql.member}
        return dictMember

    @classmethod
    def getMemberByTel(cls,tel):
        memberList=[]
        for member in mysql.member:
            if member["tel"]==tel:
                memberList.append(member)
                break
            elif member["tel"].endswith(tel):
                memberList.append(member)
        dictMember={"member":memberList}
        return dictMember

    @classmethod
    def getMemberByid(cls,id):
        memberList=[]
        for member in mysql.member:
            if member["id"]==id:
                memberList.append(member)
                break
        dictMember = {"member": memberList}
        return dictMember

    @classmethod
    def AddMember(cls,tel):
        #tel=str(tel)
        newMember={"tel":tel,"discount":1}
        newMember["id"]=str(len(newMember)+3)
        mysql.member.append(newMember)
        dictMember = {"member": newMember}
        return dictMember

    @classmethod
    def updateMemberByID(cls,id,newMember):
        #根据id，以及传入的newMember对现有用户信息进行修改
        for i in range(len(mysql.member)):
            if mysql.member[i]["id"]==id:
                for key in newMember.keys():
                    mysql.member[i][key]=newMember[key]
                return mysql.member[i]
        return {}

    @classmethod
    def updateScore(cls,id,score):
        for i in range (len(mysql.member)):
            if mysql.member[i]["id"]==id:
                scoreBefore=mysql.member[i]["score"]
                scoreAfter=scoreBefore+int(score)
                mysql.member[i]["score"]=scoreAfter

                updateScoreMember={
                    "id":id,
                    "tel": mysql.member[i]["tel"],
                    "scoreBefore":scoreBefore,
                    "scoreAfter":scoreAfter,
                    "scoreChange":score,
                }

                return updateScoreMember

    @classmethod
    def updateActive(cls,id):
        for i in range(len(mysql.member)):
            if mysql.member[i]["id"]==id:
                mysql.member[i]["active"]="0"
                updateActiveMember={
                                "id":id,
                                "tel":mysql.member[i]["tel"],
                                "active":"0","discount":"1"}
                return updateActiveMember
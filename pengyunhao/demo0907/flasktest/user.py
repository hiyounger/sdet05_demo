#encoding:utf-8
from pengyunhao.demo0907.flasktest import mysql


class user():
    @classmethod
    def addUser(cls,username,password):
        newUser={}
        user=[]
        if mysql.user["username"]==username:
            returnData={
                "error_code": 401,
                "error_msg": "用户已存在"
            }
            return returnData
        else:
            uid=len(mysql.user)
            newUser["uid"]=uid+2
            newUser["username"]=username
            newUser["password"]=password
            user.append(newUser)
            return newUser

    @classmethod
    def allUser(self,uid):
        if mysql.user["uid"]==uid:
            return mysql.user
        else:
            returnData={"error_code": 405,
                        "error_msg": "用户不存在"}
            return returnData

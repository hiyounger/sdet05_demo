# encoding:utf-8
from Yzx.flask.db import mysql
from Yzx.flask.tools.logger import info,debug,error

class Mermbers():
    # 查询所有用户
    @classmethod
    def get_members(cls):
        members_dic={
            'count':len(mysql.members),
           'members': mysql.members,
            'msg':"return members successful"
        }
        return members_dic

    # 根据手机号码查询用户
    @classmethod
    def get_members_by_tel(cls, tel):
        members_list = []
        for mem in mysql.members:
            if str(tel) == mem['tel']:
                members_list.append(mem)
                break
            elif mem['tel'].endswith(tel):
                members_list.append(mem)
        members_dic={
            'members':members_list,
            'msg':"return members by tel sucessful"
        }
        return members_dic

    # 根据用户id查询用户
    @classmethod
    def get_member_by_uid(cls, uid):
        members_list = []
        for mem in mysql.members:
            if mem['id']==uid:
                members_list.append(mem)
                break
        members_dic = {
            'members': members_list,
            'msg': "return members by tel sucessful"
        }
        return members_dic

    # 增添用户
    @classmethod
    def add_member(cls,tel):
        members_list=mysql.members
        new_member={'tel':tel,'disc':1.0,'points': 0000,'state': 1}
        new_member['id']=str(len(mysql.members)+1)
        members_list.append(new_member)
        return new_member
    # 更新用户put
    @classmethod
    def update_member_by_id(cls,uid,new_info_dic):
        for i in range(len(mysql.members)):
            if mysql.members[i]['id']==uid:
                for key in new_info_dic.keys():
                    mysql.members[i][key]=new_info_dic[key]
                return mysql.members[i]
        return {}
    # 会员积分累计
    @classmethod
    def update_member_points(cls,uid,points):
        for i in range(len(mysql.members)):
            if mysql.members[i]['id']==uid:
                score_befor=mysql.members[i]['points']
                score_after=mysql.members[i]['points']+int(points)
                mysql.members[i]['points']=score_after
                return_dic={
                    'uid':uid,
                    'tel':mysql.members[i]['tel'],
                    'score_befor':score_befor,
                    'score_after':score_after,
                    'score_change':points
                }
                return return_dic
    # 注销用户
    @classmethod
    def delete_member_by_id(cls,id):
        for i in range(len(mysql.members)):
            if mysql.members[i]['id'] == id:
                mysql.members[i]['state']=0
                mysql.members[i]['disc']=1
                return_dic = {
                    'uid': id,
                    'tel': mysql.members[i]['tel'],
                    'state': 0,
                    'disc': 1
                }
                return  return_dic
    #列出积分大于某值的用户
    @classmethod
    def find_socre_big(cls,score):
        member_list=[]
        for mem in mysql.members:
            if str(mem['points'])>=score:
                member_list.append(mem)
        return_dic={
            'count':len(member_list),
            'members':member_list
        }
        return return_dic


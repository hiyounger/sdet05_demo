# encoding:utf-8
from Yzx.flask.db import mysql


class Mermbers():
    @classmethod
    def get_members(cls):
        return mysql.members

    @classmethod
    def get_members_by_tel(cls, tel):
        members_list = []
        for mem in mysql.members:
            if tel == mem['tel']:
                members_list.append(mem)
                break
            elif mem['tel'].endswith(tel):
                members_list.append(mem)
        return members_list

    @classmethod
    def get_member_by_uid(cls, uid):
        members_list = []
        for mem in mysql.members:
            if mem['id']==uid:
                members_list.append(mem)
                break
        return members_list

    @classmethod
    def add_member(cls,tel):
        members_list=mysql.members
        new_member={'tel':tel,'disc':1.0,'points': 0000,'state': 1}
        new_member['id']=str(len(mysql.members)+1)
        members_list.append(new_member)
        return str(new_member)


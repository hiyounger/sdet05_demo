# encoding:utf-8
from tyj.super_market.db import mysql


class get_members():
    @classmethod
    def all_member(cls):
        return mysql.members

    @classmethod
    def get_member_by_tel(cls, tel):
        get_all_member = []
        for member in mysql.members:
            if member['tel'] == tel:
                get_all_member.append(member)
                break
            elif member['tel'].endswith(tel):
                get_all_member.append(member)
        return get_all_member

    @classmethod
    def get_member_by_uid(cls, uid):
        get_all_member = []
        for member in mysql.members:
            if member['id'] == uid:
                get_all_member.append(member)
                break
        return get_all_member

    @classmethod
    def add_member(cls, tel):
        new_member = {'tel': tel, 'disc': 1}
        new_member['id'] = str(len(mysql.members) + 1)
        mysql.members.append(new_member)
        return new_member

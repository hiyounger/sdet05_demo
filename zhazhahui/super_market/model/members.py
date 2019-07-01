# encoding:utf-8
from zhazhahui.super_market.db import mysql


class Member():
    @classmethod
    def get_all_member(cls):
        return mysql.members

    @classmethod
    def get_member_by_tel(cls, tel):
        member_list = []
        for member in mysql.members:
            if member['tel'] == tel:
                member_list.append(member)
                break
            elif member['tel'].endswith(tel):
                member_list.append(member)
        return member_list

    @classmethod
    def get_members_by_uid(cls, uid):
        member_list = []
        for member in mysql.members:
            if member["id"] == uid:
                member_list.append(member)
                break
        return member_list

    @classmethod
    def add_member(cls, tel):
        new_member = {'tel': tel, 'discount': '1'}
        new_member['uid'] = str(len(mysql.member) + 1)
        mysql.member.append(new_member)
        return new_member

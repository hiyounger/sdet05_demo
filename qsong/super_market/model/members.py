# -*- encoding:utf-8 -*-

from qsong.super_market.db import mysql


class Member():

    @classmethod
    def get_all_members(cls):
        return mysql.members

    @classmethod
    def get_members_by_tel(cls, tel):
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
            if member['id'] == uid:
                member_list.append(member)
                break
        return member_list

    @classmethod
    def add_member(cls, tel):
        new_member = {'tel':tel,'discount':'1'}
        new_member['uid'] = str(len(mysql.members) + 1)
        mysql.members.append(new_member)
        return new_member

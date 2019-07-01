# -*- encoding:utf-8 -*-
from yuanhongxu.super_market.db import mysql


class member():
    @classmethod
    def get_all_member(cls):
        return mysql.member

    @classmethod
    def get_member_by_tel(cls, tel):
        member_list = []
        for m in mysql.member:
            if m["tel"] == tel:
                member_list.append(m)
                break
            elif m["tel"].endswith(tel):
                member_list.append(m)
        return member_list

    @classmethod
    def get_member_by_uid(cls, uid):
        member_list = []
        for m in mysql.member:
            if m["id"] == uid:
                member_list.append(m)
                break
        return member_list

    @classmethod
    def add_member(cls, tel):
        new_member = {"tel": tel, "disc": 1, "status": "active", "jifen": 0}
        new_member["id"] = str(len(mysql.member) + 1)
        mysql.member.append(new_member)
        return (new_member)

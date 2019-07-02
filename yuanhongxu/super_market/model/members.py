# -*- encoding:utf-8 -*-
from yuanhongxu.super_market.db import mysql


class member():
    @classmethod
    def get_all_member(cls):
        member_dis = {"members": mysql.member}
        return member_dis

    @classmethod
    def get_member_by_tel(cls, tel):
        member_list = []
        for m in mysql.member:
            if m["tel"] == tel:
                member_list.append(m)
                break
            elif m["tel"].endswith(tel):
                member_list.append(m)
        traget_members = {
            "count": len(member_list),
            "member": member_list
        }
        return traget_members

    @classmethod
    def get_member_by_uid(cls, uid):
        member_list = []
        for m in mysql.member:
            if m["uid"] == uid:
                member_list.append(m)
                break
        traget_members = {
            "count": len(member_list),
            "member": member_list
        }
        return traget_members

    @classmethod
    def add_member(cls, tel):
        new_member = {"tel": tel, "disc": 1, "status": "active", "jifen": 0}
        new_member["uid"] = str(len(mysql.member) + 1)
        mysql.member.append(new_member)
        return (new_member)

    @classmethod
    def update_member(cls, uid, new_user_info):
        for i in range(len(mysql.member)):
            if mysql.member[i]["uid"] == uid:
                for key in new_user_info.keys():
                    mysql.member[i][key] = new_user_info[key]
                return mysql.member[i]
        return {}

    @classmethod
    def update_member_jifen(cls, uid, jifen):
        for i in range(len(mysql.member)):
            if mysql.member[i]["uid"] == uid:
                jifen_befor = mysql.member[i]["jifen"]
                jifen_after = jifen_befor + int(jifen)
                mysql.member[i]["jifen"] = jifen_after
                ret_dic = {
                    "uid": mysql.member[i]["uid"],
                    "tel": mysql.member[i]["tel"],
                    "jifen_befor": jifen_befor,
                    "jifen_after": jifen_after,
                    "jifen": jifen
                }
                return ret_dic

    @classmethod
    def inactive_member(cls, uid):
        for i in range(len(mysql.member)):
            if mysql.member[i]["uid"] == uid:
                mysql.member[i]["status"] = "inactive"
                ret_dic = {
                    "uid": mysql.member[i]["uid"],
                    "tel": mysql.member[i]["tel"],
                    "status": "inactive",
                    "disc": 1,
                    "jifen": 0
                }
                return ret_dic

    @classmethod
    def filter_member_by_score(cls, jifen):
        member_list = []
        for member in mysql.member:
            if str(member["jifen"]) >= jifen:
                member_list.append(member)
        ret_dic = {
            "count": len(member_list),
            "member": member_list
        }
        return ret_dic

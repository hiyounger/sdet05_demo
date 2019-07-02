# -*- encoding:utf-8 -*-

from qsong.super_market.db import mysql


class Member():

    @classmethod
    def get_all_members(cls):
        member_dic = {
            'members': mysql.members
        }
        return member_dic

    @classmethod
    def get_members_by_tel(cls, tel):
        member_list = []
        for member in mysql.members:
            if member['tel'] == tel:
                member_list.append(member)
                break
            elif member['tel'].endswith(tel):
                member_list.append(member)
        target_members = {
            'count': len(member_list),
            'members': member_list
        }
        return target_members

    @classmethod
    def get_members_by_uid(cls, uid):
        member_list = []
        for member in mysql.members:
            if member['uid'] == uid:
                member_list.append(member)
                break
        target_members = {
            'count': len(member_list),
            'members': member_list
        }
        return target_members

    @classmethod
    def add_member(cls, tel):
        new_member = {'tel':tel,'discount':'1'}
        new_member['uid'] = str(len(mysql.members) + 1)
        mysql.members.append(new_member)
        return new_member

    @classmethod
    def update_member_info(cls, uid, new_user_info):
        # 根据UID，以及传入的new_user_info 对现有用户信息进行修改
        for i in range(len(mysql.members)):
            if mysql.members[i]['uid'] == uid:
                for key in new_user_info.keys():
                    mysql.members[i][key] = new_user_info[key]
                return mysql.members[i]
        return {}

    @classmethod
    def update_member_score(cls,uid, score):
        for i in range(len(mysql.members)):
            if mysql.members[i]['uid'] == uid:
                score_before = mysql.members[i]['score']
                score_after = score_before + int(score)
                mysql.members[i]['score'] = score_after

                ret_dic = {
                    'uid': mysql.members[i]['uid'],
                    'tel': mysql.members[i]['tel'],
                    'score_before': score_before,
                    'score_after': score_after,
                    'score_change': score,
                }
                return ret_dic






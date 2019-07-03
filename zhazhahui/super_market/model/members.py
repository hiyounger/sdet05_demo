# encoding:utf-8
from zhazhahui.super_market.db import mysql


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
            "members": member_list
        }
        return target_members

    @classmethod
    def get_members_by_uid(cls, uid):
        member_list = []
        for member in mysql.members:
            if member["uid"] == uid:
                member_list.append(member)
                break
        ret_dic = {
            "member": member_list,
            "count": len(member_list)
        }
        return ret_dic

    @classmethod
    def add_members(cls, tel):
        new_member = {'tel': tel, 'discount': '1'}
        new_member['uid'] = len(mysql.member) + 1
        mysql.member.append(new_member)
        return new_member

    @classmethod
    def update_member_info(clscls, uid, new_user_info):
        #         根据UID，以及传入的new_user_info 对现有的用户信息进行修改
        for i in range(len(mysql.members)):
            if mysql.members[i]['uid'] == uid:
                for key in new_user_info.key():
                    mysql.members[i][key] = new_user_info[key]
                    return mysql.members[i]
        return {}

    @classmethod
    def update_member_score(cls, uid, score):
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

    @classmethod
    def inactive_member(cls, uid):
        for i in range(len(mysql.members)):
            if mysql.members[i]['uid'] == uid:
                mysql.members[i]['active'] = 'die'

                ret_dic = {
                    'uid': mysql.members[i]['uid'],
                    'tel': mysql.members[i]['tel'],
                    'active': 'die',
                    'discount': '1'
                }
                return ret_dic

    @classmethod
    def filter_member_by_score(cls, score):
        member_list = []
        for member in mysql.members:
            if str(member['score']) >= score:
                debug("Find user:uid=%s" % str(member['uid']))
                member_list.append(member)
            ret_dic = {
                'count': len(member_list),
                'members': member_list
            }
            return ret_dic

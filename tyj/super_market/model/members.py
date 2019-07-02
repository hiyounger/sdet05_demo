# encoding:utf-8
from tyj.super_market.db import mysql


class get_members():
    @classmethod
    def all_member(cls):
        member_dic = {
            'member': mysql.members
        }
        return member_dic

    @classmethod
    def get_member_by_tel(cls, tel):
        get_all_member = []
        for member in mysql.members:
            if member['tel'] == tel:
                get_all_member.append(member)
                break
            elif member['tel'].endswith(tel):
                get_all_member.append(member)
        target_member = {
            'count': len(get_all_member),
            'member': get_all_member
        }
        return target_member

    @classmethod
    def get_member_by_uid(cls, uid):
        get_all_member = []
        for member in mysql.members:
            if member['id'] == uid:
                get_all_member.append(member)
                break

        get_member = {
            'count': len(get_all_member),
            'member': get_all_member
        }
        return get_member

    @classmethod
    def add_member(cls, tel):
        new_member = {'tel': tel, 'disc': 1}
        new_member['id'] = str(len(mysql.members) + 1)
        mysql.members.append(new_member)
        return new_member

    @classmethod
    def update_member_info(cls, id, new_member_info):
        # 根据ID以及新传入的new_member_info的信息，对现有用户信息进行修改
        for i in range(len(mysql.members)):
            if mysql.members[i]['id'] == id:
                for key in new_member_info.keys():
                    mysql.members[i]['id'] = new_member_info[key]
                return mysql.members[i]
            return {}

    @classmethod
    def update_member_score(cls, id, score):
        for i in range(len(mysql.members)):
            if mysql.members[i]['id'] == id:
                score_before = mysql.members[i]['score']
                score_after = score_before + int(score)
                mysql.members[i]['score'] = score_after

                ret_dic = {
                    'id': mysql.members[i]['id'],
                    'tel': mysql.members[i]['tel'],
                    'score_before': score_before,
                    'score_after': score_after,
                    'score_change': score
                }
                return ret_dic

    @classmethod
    def inactive_member(cls, id):
        for i in range(len(mysql.members)):
            if mysql.members[i]['id'] == id:
                mysql.members[i]['active'] = '0'

                ret_dic = {
                    'id': mysql.members[i]['id'],
                    'tel': mysql.members[i]['tel'],
                    'active': '0',
                    'dics': '1'
                }
                return ret_dic
    @classmethod
    def filter_member_by_score(cls,score):
        member_list = []
        for member in mysql.members:
            if str(member['score'])>=score:
                member_list.append(member)

                ret_dic = {
                    'count':len(member_list),
                    'members':member_list
                }
                return ret_dic

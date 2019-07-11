# encoding:utf-8
from zhangjun_demo.super_maket.db import mysql


class Member():
    @classmethod
    def get_all_members(cls):
        member_dic = {
            'members': mysql.members
        }
        return member_dic

    @classmethod
    def get_member_list(cls, tel):
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
    def get_members_by_id(cls, id):
        member_list = []
        for member in mysql.members:
            if member['id'] == id:
                member_list.append(member)
                break
        target_members = {
            'count': len(member_list),
            'members': member_list
            }
        return target_members
        #     else:
        #         a= {'你的输入有误':'请重新输入！'}
        #         return a

    @classmethod
    def add_vip(cls, user_tel):
        new_id = str(len(mysql.members) + 1)
        new_discount = 1.0
        dic = {'id': new_id, 'tel': user_tel, 'discount': new_discount, 'score': 100, 'active': 1}
        mysql.members.append(dic)
        return dic

    @classmethod
    def update_member(cls, id, new_user_info):
        for i in range(len(mysql.members)):
            if mysql.members[i]['id'] == id:
                for key in new_user_info.key():
                    mysql.members[i][key] = new_user_info[key]
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
                    'score_change': score,
                }
                return ret_dic

    @classmethod
    def inactive_members(cls, id):
        for i in range(len(mysql.members)):
            if mysql.members[i]['id'] == id:
                mysql.members[i]['active'] = '0'
                ret_dic = {
                    'id': mysql.members[i]['id'],
                    'tel': mysql.members[i]['tel'],
                    'active': '0',
                    'discount': 1.0,
                }
                return ret_dic
    @classmethod
    def filter_member_by_score(cls,score):
        member_list=[]
        for member in mysql.members:
            if str(member['score'])>=score:
                member_list.append(member)
        ret_dic = {
            'count':len(member_list),
            'member':member_list
                }
        return ret_dic

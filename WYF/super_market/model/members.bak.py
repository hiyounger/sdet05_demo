# coding:utf-8
from WYF.super_market.db import mysql


class Member():
    @classmethod
    def get_all_members(cls):
        member_dic={
            'members':mysql.members
        }
        return member_dic

    @classmethod
    def get_member_last_four(cls, tel):
        member_list = []
        for member in mysql.members:
            if member['tel'] == tel:
                member_list.append(member)
                break
            elif member['tel'].endswith(tel):
                member_list.append(member)
        target_members={
            'count':len(member_list),
            'members':member_list
        }
        return target_members

    @classmethod
    def get_member_by_id(cls, uid):
        member_list = []
        for member in mysql.members:
            if str(member['uid']) == uid:
                member_list.append(member)
                break
        print(member_list)
        tar_members={
            'count': len(member_list),
            'members': member_list
        }
        return tar_members

    @classmethod
    def add_member(cls,tel):
        new_member = {'tel':tel,'discount':1}
        new_member['uid']=int(len(mysql.members)+1)
        mysql.members.append(new_member)
        return new_member
    @classmethod
    def update_member(cls,uid,new_member):
        for i in range(len(mysql.members)):
            if str(mysql.members[i]['uid'])== uid:
                for key in new_member.keys():
                    mysql.members[i][key]=new_member[key]
                return mysql.members[i]
        return {}
    @classmethod
    def update_member_jifen(cls,uid,jifen):
        for i in range(len(mysql.members)):
            if str(mysql.members[i]['uid']) == uid:
                jifen_before=mysql.members[i]['jifen']
                jifen_after=jifen_before+int(jifen)
                mysql.members[i]['jifen']=jifen_after
                ret_dic ={
                    'uid':mysql.members[i]['uid'],
                    'tel': mysql.members[i]['tel'],
                    'jifen_before':jifen_before,
                    'jifen_after': jifen_after,
                    'jifen_change': jifen
                }
                return ret_dic

    @classmethod
    def delete_member(cls,uid):
        for i in range(len(mysql.members)):
            if str(mysql.members[i]['uid']) == uid:
                mysql.members[i]['state'] ='0'
                mysql.members[i]['discount'] = '1'
                ret_dic = {
                    'uid': mysql.members[i]['uid'],
                    'tel': mysql.members[i]['tel'],
                    'state': '0',
                    'discount': mysql.members[i]['discount']
                }
                return ret_dic
    @classmethod
    def filter_member_by_jifen(cls,jifen):
        member_list=[]
        for member in  mysql.members:
            if str(member['jifen'])>=jifen:
                member_list.append(member)
        ret_dic = {
            'count': len(member_list),
            'members': member_list
        }
        return ret_dic







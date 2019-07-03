# encoding:utf-8
from liu.supermarket.DB import MySQL


class Member:
    @classmethod

    def get_all_members(cls):
        members_dic={
            'members':MySQL.members
        }
        return members_dic

    @classmethod
    def get_member_by_tel(cls,tel):
        member_list = []
        for member in MySQL.members:
            if member['tel']==tel:
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
    def get_member_by_uid(cls,uid):
        print("--->",uid)
        member_list = []
        for member in MySQL.members:
            print member
            if member['id']==uid:
                member_list.append(member)
                break
        print(member_list)
        target_members = {
            'count': len(member_list),
            'members': member_list
        }
        return target_members
    @classmethod
    def add_member_by_tel(cls,utel):
        new_member={'tel':utel,'disc':1.0,'active':1}
        new_member['id'] = str(len(MySQL.members) + 1)
        MySQL.members.append(new_member)
        return new_member
    @classmethod
    def update_member_info(cls,uid,new_user_info):
        for i in range(len(MySQL.members)):
            if MySQL.members[i]['id']==uid:
                for key in new_user_info.keys():
                    MySQL.members[i][key]=new_user_info[key]
                return MySQL.members[i]
        return {}
    @classmethod
    def update_member_score(cls,uid,score):
        for i in range(len(MySQL.members)):
            if MySQL.members[i]['uid']==uid:
                score_before =  MySQL.members[i]['score']
                score_after = score_before + int(score)
                MySQL.members[i]['score'] = score_after
                ret_dic = {
                    'uid':MySQL.members[i]['uid'],
                    'tel':MySQL.members[i]['tel'],
                    'score_before':score_before,
                    'score_after':score_after,
                    'score_change':score,
                }
                return ret_dic

    @classmethod
    def inactive_member(cls,uid):
        for i in range(len(MySQL.members)):
            if MySQL.members[i]['uid'] == uid:
                MySQL.members[i]['active']='0'

                ret_dic = {
                    'uid':MySQL.members[i]['uid'],
                    'tel': MySQL.members[i]['tel'],
                    'active':'0',
                    'disc':'1'
                }
                return ret_dic
    @classmethod
    def filter_member_by_score(cls,score):
        member_list = []
        for member in MySQL.members:
            if str(member['score']) >= score:
                member_list.append(member)
        ret_dic = {
            'count': len(member_list),
            'member': member_list
        }
        return ret_dic


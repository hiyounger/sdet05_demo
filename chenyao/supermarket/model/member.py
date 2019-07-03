# encoding:utf-8
from chenyao.supermarket.db import member
class Members:
    @classmethod
    def show_members(self):
        # out_all = '编号\t\t手机号\t折扣\t积分\n'
        # for mem in members:
        #     out_all += "%s\t%s\t%s\t%s\n" % (mem['id'], mem['tel'], mem['disc'], mem['score'])
        # return out_all
        members_dic = {
            'members': member.members
        }
        return members_dic
    @classmethod
    def show_members_tel(cls, tel):
        members_list = []
        for mem in member.members:
            if mem['tel'] == tel:
                members_list.append(mem)
                break
            elif mem['tel'].endswith(tel):
                members_list.append(mem)
        target_members = {
            'count': len(members_list),
            'members': members_list
        }
        return target_members
    @classmethod
    def show_members_uid(cls, uid):
        members_list = []
        for mem in member.members:
            if mem['uid'] == uid:
                members_list.append(mem)
                break
        target_uid = {
            'return_code': 200,
            'msg_uid': 'return uid succes',
            'members': members_list
        }
        return target_uid
    @classmethod
    def add_member(cls, tel):
        new_member = {'tel': tel, 'disc': 1, 'score': 0}
        new_member['uid'] = str(len(member.members) + 1)
        member.members.append(new_member)
        return new_member

    @classmethod
    def update_member(cls, uid, new_member_info):
        # 根据uid，以及传入的new_member-info对现有用户信息进行修改
        for i in range(len(member.members)):
            if member.members[i]['uid'] == uid:
                for key in new_member_info.keys():
                    member.members[i][key] = new_member_info[key]
                return member.members[i]
        return {}
    @classmethod
    def update_member_score(cls,uid,score):
        for i in range(len(member.members)):
            if member.members[i]['uid'] == uid:
                score_before=member.members[i]['score']
                score_after =score_before + int(score)
                member.members[i]['score']=score_after

                tet_dict={
                    'uid':member.members[i]['uid'],
                    'tel':member.members[i]['tel'],
                    'score_before':score_before,
                    'score_after' :score_after,
                    'score_change':score
                }
                return tet_dict

    @classmethod
    def inactive_member(cls,uid):
        for i in range(len(member.members)):
            if member.members[i]['uid'] == uid:
               member.members[i]['active'] ='0'
               tet_dict = {
                   'uid': member.members[i]['uid'],
                   'tel': member.members[i]['tel'],
                   'active': '0',
                   'discount': 1,
               }
               return tet_dict
    @classmethod
    def filter_member_by_score(cls,score):
        member_list=[]
        for mem in member.members:
            if str(mem['score'])>=score:
                member_list.append(mem)
        tet_dict={
            'count':len(member_list),
            'members':member_list
        }
        return tet_dict

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

# #获取折扣
# class MembersHelp():
#     @classmethod
#     def get_member_disc(cls,u_tel):
#         for member in members:
#             if member['tel'] == u_tel:
#                 return member['disc']
#         return 1.0
# #新增
#     @classmethod
#     def add_members_vip(cls,u_tel):
#         for member in members:
#             if member['tel']==u_tel:
#                 print('账号已注册')
#                 return False
#         id = len(members)+1
#         member={'id':id,"tel":u_tel,'disc':1}
#         members.append(member)
#         print("注册成功")
#
# #获取所有会员列表
#     @classmethod
#     def get_member_list(cls,u_tel):
#         for member in members:
#             if member['tel']==members['tel']:
#                 print(member)
#
# #根据手机号后4位获取会员信息
#     @classmethod
#     def get_vip_list(cls,u_tel):
#         for member in members:
#             a=float(member['tel'])
#             if u_tel==a:
#                 print(member)
#
# #根据手机号注销会员（会员）
#     @classmethod
#     def logout_member(cls,u_tel):
#         member={'id':id,"tel":u_tel,'disc':1,'status':0}
#         for member in members:
#             if member['tel'] == u_tel:
#                 member['status']==0
#                 return 'Logout Success'
#         return False
#
# #修改会员信息
#     @classmethod
#     def update_member(cls,u_tel):
#         for member in members:
#             if member['tel']==u_tel:
#                 new_tel=input('请输入新手机号：%d')
#                 member['tel']==new_tel
#                 new_disc=('请输入新的会员折扣：%d')
#                 member['disc']==new_disc
#                 print('修改成功！')
#         else:
#             print('请先注册会员！')
#
# #会员累积购物积分
#     @classmethod
#     def accu_vip(cls,u_tel,total):
#         for member in members:
#             if u_tel == member['tel']and member['status']==1:
#                  total+=total
#
#         @classmethod
#         def Cumulative_members_jifen(cls, tel, sum):
#             for mem in members:
#                 if str(tel) == mem['tel'] and mem['state'] == 1:
#                     mem['jifen'] += sum
#                     if mem['jifen'] < 1000:
#                         print(mem['jifen'] == 1)
#                     elif mem['jifen'] >= 1000 and mem['jifen'] < 1500:
#                         print(mem['jifen'] == 0.98)
#                     elif mem['jifen'] >= 1500 and mem['jifen'] < 2000:
#                         print(mem['jifen'] == 0.9)
#                     elif mem['jifen'] >= 2000:
#                         print(mem['jifen'] == 0.8)
#                     return mem['discount']
#             print('对不起您不是会员，无法进行积分累计')
#             return False

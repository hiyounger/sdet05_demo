# encoding:utf-8
members=[{'id':'1','tel':'18812345678','disc':0.9,'score':100,'active':1},
{'id':'2','tel':'18712345679','disc':0.8,'score':200,'active':1},
{'id':'3','tel':'18612345671','disc':0.7,'score':300,'active':1},
{'id':'4','tel':'18612345670','disc':0.7,'score':400,'active':1}]

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
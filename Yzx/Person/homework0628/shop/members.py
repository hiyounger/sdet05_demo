#encoding:utf-8
# members=[
#     {'id':'1','tel':'18845871680','disc':0.9,'state':1,'points':0000},
#     {'id':'2','tel':'18845095099','disc':0.1,'state':1,'points':0000}
# ]
# class Members():
#     @classmethod
#     def get_disc_by_tell(cls,tel):
#         for member in members:
#             if tel == member['tel']:
#                 print member['disc']
#                 return member['disc']
#         return 1.0
#     #新增
#     @classmethod
#     def add_member_by_tell(cls,tel):
#         for mem in members:
#             if mem['tel']==tel:
#                 print ("已注册，注册失败")
#                 return False
#         id=len(members)+1
#         member={'id':id,'tel':tel,'disc':1,'state':1}
#         members.append(member)
#         print ('注册成功')
#         return 1
# # add=Members()
# # add.add_member_by_tell('18845871680')
# # add.add_member_by_tell('111')
# #获取所有会员列表全部信息
#     @classmethod
#     def get_members_all(cls):
#         for mem in members:
#             print ("会员编号：%s\t电话%s\t折扣%s\t状态%s\t"%(mem['id'],mem['tel'],mem['disc'],mem['state']))
#         return 1
# # all=Members()
# # all.get_members_all()
# #根据手机号的后四位获取会员信息
#     @classmethod
#     def get_mermber_by_tell_last_four(cls,tel_last_four):
#         for mem in members:
#             i=float(mem['tel'])
#             a=i%10000
#             if tel_last_four==a:
#                 print ("会员编号：%s\t电话%s\t折扣%s\t状态%s\t"%(mem['id'],mem['tel'],mem['disc'],mem['state']))
#                 return 1
#         return False
# # last_four=Members()
# # last_four.get_mermber_by_tell_last_four(5099)
# #根据手机号注销会员
#     @classmethod
#     def del_member_by_tell(cls,tel):
#         for mem in members:
#             if str(tel)==mem['tel']:
#                 mem['state']=0
#                 print ("删除成功")
#                 return 1
#         print ("不存在该用户")
#         return False
# # del_by_tel=Members()
# # del_by_tel.del_member_by_tell(18845871680)
# #修改会员信息（手机号，折扣）
#     @classmethod
#     def modify_member_by_tel(cls,tel,disc):
#         for mem in members:
#             if str(tel)==mem['tel']:
#                 mem['disc']=disc
#                 print mem
#                 return 1
#         print ("该手机未注册")
#         return False
# # member_modify=Members()
# # member_modify.modify_member_by_tel(18845871680,0.2)
# # member_modify.modify_member_by_tel(1884587168,0.2)
# #会员可累积购物积分
#     @classmethod
#     def accumulated_shopping_points(cls,tel,sum):
#         for mem in members:
#             if str(tel)==mem['tel']:
#                 print ("找到会员，开始累计积分。")
#                 mem['points']+=sum
#                 if mem['points']<1000:
#                     mem['disc']=1
#                 elif mem['points']>=1000 and mem['points']<3000:
#                     mem['disc']=0.98
#                 elif mem['points']>=3000 and mem['points']<5000:
#                     mem['disc'] = 0.98
#                 else:
#                     mem['disc'] = 0.90
#                 print mem['disc']
#                 return mem['disc']
#         print ("未找到该手机注册的会员，无法累计积分")
#         return False
# # accumulated=Members()
# # accumulated.accumulated_shopping_points(18845871680,10000)
# # accumulated.accumulated_shopping_points(111,1000)
#
#
#
#
#encoding:utf-8
members=[
    {'id':'1','tel':'18845871680','disc':0.9,'state':1,'points':0000},
    {'id':'2','tel':'18845095099','disc':0.1,'state':1,'points':0000}
]
class Members():
    @classmethod
    def get_disc_by_tell(cls,tel):
        for member in members:
            if tel == member['tel']:
                print member['disc']
                return member['disc']
        return 1.0
    #新增
    @classmethod
    def add_member_by_tell(cls,tel):
        for mem in members:
            if mem['tel']==tel:
                print ("已注册，注册失败")
                return False
        id=len(members)+1
        member={'id':id,'tel':tel,'disc':1,'state':1,'points':0}
        members.append(member)
        print ('注册成功')
        return 1
# add=Members()
# add.add_member_by_tell('18845871680')
# add.add_member_by_tell('111')
#获取所有会员列表全部信息
    @classmethod
    def get_members_all(cls):
        for mem in members:
            print ("会员编号：%s\t电话%s\t折扣%s\t状态%s\t积分"%(mem['id'],mem['tel'],mem['disc'],mem['state'],mem['points']))
        return 1
# all=Members()
# all.get_members_all()
#根据手机号的后四位获取会员信息
    @classmethod
    def get_mermber_by_tell_last_four(cls,tel_last_four):
        for mem in members:
            i=float(mem['tel'])
            a=i%10000
            if tel_last_four==a:
                print ("会员编号：%s\t电话%s\t折扣%s\t状态%s\t积分%s"%(mem['id'],mem['tel'],mem['disc'],mem['state'],mem['points']))
                return 1
        return False
# last_four=Members()
# last_four.get_mermber_by_tell_last_four(5099)
#根据手机号注销会员
    @classmethod
    def del_member_by_tell(cls,tel):
        for mem in members:
            if str(tel)==mem['tel']:
                mem['state']=0
                print ("删除成功")
                return 1
        print ("不存在该用户")
        return False
# del_by_tel=Members()
# del_by_tel.del_member_by_tell(18845871680)
#修改会员信息（手机号，折扣）
    @classmethod
    def modify_member_by_tel(cls,tel,disc):
        for mem in members:
            if str(tel)==mem['tel']:
                mem['disc']=disc
                print mem
                return 1
        print ("该手机未注册")
        return False
# member_modify=Members()
# member_modify.modify_member_by_tel(18845871680,0.2)
# member_modify.modify_member_by_tel(1884587168,0.2)
#会员可累积购物积分
    @classmethod
    def accumulated_shopping_points(cls,tel,sum):
        for mem in members:
            if str(tel)==mem['tel'] and mem['state']==1:
                print ("找到会员，开始累计积分。")
                mem['points']+=sum
                if mem['points']<1000:
                    mem['disc']=1
                elif mem['points']>=1000 and mem['points']<3000:
                    mem['disc']=0.98
                elif mem['points']>=3000 and mem['points']<5000:
                    mem['disc'] = 0.98
                else:
                    mem['disc'] = 0.90
                print mem['disc']
                return mem['disc']
        print ("未找到该手机注册的会员，无法累计积分")
        return False
# accumulated=Members()
# accumulated.accumulated_shopping_points(18845871680,10000)
# accumulated.accumulated_shopping_points(111,1000)





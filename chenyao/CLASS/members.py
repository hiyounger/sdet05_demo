# encoding:utf-8
members=[
    {'id':'1','tel':13312345671,'disc':0.9,'score':0},
    {'id':'2','tel':13312345672,'disc':0.8,'score':0},
    {'id':'3','tel':13312345673,'disc':0.7,'score':0},
    {'id':'4','tel':13312345674,'disc':0.6,'score':0}
]
# tel = raw_input('请输入手机号：')

class MemberHelper(object):
    #定义一个可以获取会员信息的办法
    @classmethod
    def get_member_discount(cls,tel):
        for member in members:
            if member['tel']==tel:
                return member['disc']
        return 1.0
    #1.新增
    @classmethod
    def add_member_by_tel(self,tel):
        for member in members:
            if member['tel']==tel:
               # print('手机号：%s'%tel)
               print('该手机号已注册')
               return False
            id=len(members)+1
            member={'id':id,'tel':tel,'disc':1.0,'score':0}
            members.append(member)
            # print('手机号：%s'%tel)
            print('注册成功')
            return 1
    #2.获取所有会员列表
    @classmethod
    def members_all(cls):
        out_all='编号\t\t手机号\t折扣\t积分\n'
        for mem in members:
            out_all+="%s\t%s\t%s\t%s\n"%(mem['id'],mem['tel'],mem['disc'],mem['score'])
        return out_all
    #3.根据手机号的后4位获取会员信息
    @classmethod
    def member_get(cls,tel_last):
        for mem in members:
            if tel_last==float(mem['tel'])%10000:
               # print('根据手机后4位:%s获取会员信息'%tel_last)
               print("%s\t%s\t%s\t%s"%(mem['id'],mem['tel'],mem['disc'],mem['score']))
               return 1
        # print('根据手机后4位:%s' % tel_last)
        print('该用户不是会员')
        return False
    #4.根据手机号注销会员（保留）
    @classmethod
    def member_delete(cls,tel_del,disc):
        for mem in members:
            if tel_del==int(mem['tel']):
               # print("手机号：%s"%tel_del)
               print('删除成功')
               return 1
        # print('手机号：%s'%tel_del)
        print('不存在该用户')
        return False
    #5.修改会员信息（手机号，折扣）
    @classmethod
    def member_mod(cls,tel_mod,disc):
        for mem in members:
           if tel_mod==int(mem['tel']):
               # print('手机号：%s'%tel_mod)
               # print("%s\t%s\t%s\t%s" % (mem['id'], mem['tel'], mem['disc'], mem['score']))
               print("%s\t%s\t%s\t%s"%(mem['id'], mem['tel'], disc, mem['score']))
               print('修改会员信息成功')
               return 1
               # print("%s\t%s\t%s\t%s\n" % (mem['id'], 12312345678, mem['disc'], mem['score']))
        # print('手机号：%s'%tel_mod)
        print('该用户未注册')
        return False
    #6.会员可累计的购物积分
    @classmethod
    def score_acc(cls,tel_acc,disc,score):
        for mem in members:
            if tel_acc==int(mem['tel']):
               # print('手机号：%s'%mem['tel'])
               print("%s\t%s\t%s\t%s"%(mem['id'],mem['tel'],disc,score))
               print('累计积分成功')
               return 1
# tel = raw_input('请输入手机号：')
# add=MemberHelper()
# add.add_member_by_tel(tel)
# add.add_member_by_tel('13720158814')
# print
# all=MemberHelper()
# print(all.members_all())
# print
# last=MemberHelper()
# last.member_get(int(tel)%10000)
# last.member_get(2222)
# print
# dele=MemberHelper()
# dele.member_delete(13312345671,1.0)
# dele.member_delete(13312345670,1.0)
# print
# mod=MemberHelper()
# mod.member_mod(13312345671,0.5)
# mod.member_mod(13312345675,0.5)
# print
# acc=MemberHelper()
# acc.score_acc(13312345671,2000)




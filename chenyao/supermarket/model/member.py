# encoding:utf-8

from chenyao.supermarket.db import member

class Members:
    @classmethod
    def show_members(self):
        # out_all = '编号\t\t手机号\t折扣\t积分\n'
        # for mem in members:
        #     out_all += "%s\t%s\t%s\t%s\n" % (mem['id'], mem['tel'], mem['disc'], mem['score'])
        # return out_all
        return member.members
    @classmethod
    def show_members_tel(cls,tel):
        members_list=[]
        for mem in member.members:
            if mem['tel']==tel:
                members_list.append(mem)
                break
            elif mem['tel'].endswith(tel):
                members_list.append(mem)
        return members_list
    @classmethod
    def show_members_uid(cls,uid):
        members_list=[]
        for mem in member.members:
            if mem['id']==uid:
                members_list.append(mem)
                break
        return members_list
    @classmethod
    def add_member(cls,tel):
        new_member={'tel':tel,'disc':1,'score':0}
        new_member['id']=str(len(member.members)+1)
        member.members.append(new_member)
        return new_member


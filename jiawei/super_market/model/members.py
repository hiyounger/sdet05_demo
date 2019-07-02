# encoding:utf-8
from jiawei.super_market.db import mysql


class Member():

    @classmethod
    def get_all_member(cls):
        # vip_msg = ("会员编号   会员电话       享受折扣 会员状态   会员积分\n")
        # for member in members:
        #     vip_msg += "%s\t   %s\t     %s\t      %s\t       %s\n" % (
        #         member['uid'], member['tel'], member['disc'], member['state'], member['itg'])
        # print vip_msg
        return mysql.members

    @classmethod
    def get_member_by_tel(cls, tel):
        member_list = []
        for member in mysql.members:
            if member['tel'] == 'tel':
                member_list.append(member)
                break
            elif member['tel'].endswith(tel):
                member_list.append(member)
        return member_list

    @classmethod
    def get_member_by_uid(cls, uid):
        member_list = []
        for member in mysql.members:
            if member['tel'] == uid:
                member_list.append(member)
                break

        return member_list

# -*- encoding:utf-8 -*-

# 定义会员的信息
members = [
    {'uid':'1', 'tel':'13312345678', 'disc': 0.90},
    {'uid':'2', 'tel':'13312345679', 'disc': 0.95}
]


class MemberHelper():

    # 定义一个获取会员信息的方法
    @classmethod
    def get_memeber_discount(cls, user_tel):
        for member in members:
            if member['tel'] == user_tel:
                return member['disc']
        return 1.0

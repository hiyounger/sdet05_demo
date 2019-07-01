# -*- encoding:utf-8 -*-

# 现有的会员数据列表
members = [
    {'id': '1', 'tel':"18812345671", 'discount': '0.98'},
    {'id': '2', 'tel':"18812345672", 'discount': '0.9'},
    {'id': '3', 'tel':"18812345673", 'discount': '0.8'}
]

# 根据会员的电话号码，获取指定会员的折扣信息
tel = '18812345672'
for member in members:
    if member['tel'] == tel:
        print(member['discount'])

# 新录入一个 tel为18812345674， discount：0.95
members.append({'id': '4', 'tel':"18812345674", 'discount': '0.95'})

# 获取当前会员的数量
print(len(members))
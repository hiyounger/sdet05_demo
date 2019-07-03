# encoding:utf-8

# 现有会员数据列表
list=[
    {'id':'1','tel':'18812345671','zhekou':'0.98'},
    {'id':'2','tel':'18812345672','zhekou':'0.9'},
    {'id':'3','tel':'18812345673','zhekou':'0.8'}
]
# 根据会员电话，获取会员折扣
tel='18812345671'
for a in list:
    if a['tel']==tel:
        print (a['zhekou'])

# 新录入一个会员
list.append({'id':'4','tel':'18812345674','zhekou':'0.95'})

# 获取当前会员数量
print (len(list))
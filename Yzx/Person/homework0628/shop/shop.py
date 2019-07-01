#encoding:utf-8
from members import Members
members=[
    {'id':'1','tel':'18845871680','disc':0.9},
    {'id':'2','tel':'18845095099','disc':0.1}
]
shop_list=[]
pay_list=[]
#根据手机号码获取会员折扣
def get_disc_by_tell(tel):
    for member in members:
        if tel==member['tel']:
            print member['disc']
            return member['disc']
    return 1.0
#商品价格
def input_price():
    while True:
        try:
            price = raw_input("请输入商品的价格或者输入Q退出")
            return float(price)
        except:
            if price=="Q":
                return "Q"
            print('输入错误，请重新输入')
#将价格导入支付账单中，并计算折扣后的价格
def pay_list_cal(shop_list,disc):
    sum=0
    for i in range(len(shop_list)):
        temp=[i+1,shop_list[i],shop_list[i]*disc]
        pay_list.append(temp)
        sum+=shop_list[i]*disc
    pay_lists=[pay_list,sum]
    return pay_lists
#输出格式
def out_way(new_pay_list):
    msg="商品ID\t单价\t折扣价格\n"
    for i in new_pay_list[0]:
        msg+="%s\t\t%s\t%s\n"%(i[0],i[1],i[2])
    msg+="-----------------\n"
    msg+="总价:\t%s"%new_pay_list[1]
    return  msg

tel=raw_input("输入你的手机号码：")
disc=get_disc_by_tell(tel)
while True:
#输入商品，Q退出输入
    price=input_price();
    if price=="Q":
        break
    else:
        #保存商品的单价
        shop_list.append(price)
new_pay_list=pay_list_cal(shop_list,disc)
out_msg=out_way(new_pay_list)
print out_msg




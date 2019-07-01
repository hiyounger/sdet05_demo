#encoding:utf-8
from members import Members
from cilt import scilt
def sale():
    shop_list=[]
    tel=raw_input("输入你的手机号码：")
    disc=Members.get_disc_by_tell(tel)
    while True:
    #输入商品，Q退出输入
        price=scilt.input_price();
        if price=="Q":
            break
        else:
            #保存商品的单价
            shop_list.append(price)
    new_pay_list=scilt.pay_list_cal(shop_list,disc)
    out_msg=scilt.out_way(new_pay_list)
    print out_msg
if __name__=='__main__':
    sale()



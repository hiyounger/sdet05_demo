# coding:UTF-8

from members import MemberHelper
from client import SalesClient

def saling():
    user_tel =raw_input("请提供手机号：")
    user_disc=MemberHelper.get_member_discount(user_tel)

    product_list=[]
    while True:
        prod_info = SalesClient.get_product_input()
        if prod_info=="Q":
            break
        else:
            product_list.append(prod_info)


    pay_list,pay_total=SalesClient.calculator_payment(product_list,user_disc)

    output=SalesClient.format_out_msg(pay_list,pay_total)
    print output
if __name__ == '__main__':
    saling()
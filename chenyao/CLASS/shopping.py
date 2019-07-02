# encoding:utf-8
from members import  MemberHelper
from saleclient import  Saleclient

tel = int(raw_input('请输入手机号：'))
add=MemberHelper()
add.add_member_by_tel(tel)
print
all=MemberHelper()
print(all.members_all())
last=MemberHelper()
last.member_get(int(tel)%10000)
print
dele=MemberHelper()
dele.member_delete(tel,1.0)
print
mod=MemberHelper()
mod.member_mod(tel,0.5)
print
acc=MemberHelper()
acc.score_acc(tel,0.8,2000)
all=MemberHelper()
print
# print(all.members_all())
# tel=raw_input('请输入手机号：')
def saling():
    #1.获取用户手机号,并通过手机号获取用户的折扣额度
    # tel=raw_input('请提供手机号:')
    disc=MemberHelper.get_member_discount(tel)

    #2.录入商品信息
    pro_list = []
    while True:
        pro_info=Saleclient.get_pro_input()
        if pro_info=='Q':
            break
        else:
            pro_list.append(pro_info)

    #3.计算商品的结算清单
    pay_list, pay_total = Saleclient.calculator_payment(pro_list, disc)

    #4.格式化输出内容
    output=Saleclient.format_out_msg(pay_list,pay_total)

    #5.输出
    print(output)

if __name__ == '__main__':
    saling()




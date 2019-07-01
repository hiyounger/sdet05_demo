#encoding:utf-8

#导包
from member import MemberUtils
from client import SalesClient

def saling():
    #1.获取用户手机号，并通过手机号获取用户折扣
    userTel=raw_input("请输入手机号：")
    logoutOrPay=int(input("请选择注销还是结算：1.修改，2.注销，输入其他进行结算："))
    userDiscount= MemberUtils.getMemberDisc(userTel,logoutOrPay)
    newMember = []
    if userDiscount==1:
        newMember = {}
        int(raw_input("该用户目前不是会员如需添加请输入1:"))
        newMember=MemberUtils.AddMember(userTel,newMember)
        print newMember
        MemberUtils.querMember(newMember, userTel)
        MemberUtils.queryMemberAll(newMember)
    #2.录入商品信息
    productList = []
    while 1:
        productInfo=SalesClient.getProductInput()
        print ("%s"%productInfo)
        if productInfo=="t":
            break
        else:
            print ("已添加到商品列表")
            productList.append(productInfo)

    #3.商品的结束清单
    payList,payTotal=SalesClient.payMenu(productList,userDiscount)


    #4.格式化输出
    outPut = SalesClient.formatOut(payList, payTotal)
    print outPut
    newMember=SalesClient.Integral(payTotal, newMember, userTel)
    MemberUtils.AllMember(newMember)
if __name__=='__main__':
    saling()
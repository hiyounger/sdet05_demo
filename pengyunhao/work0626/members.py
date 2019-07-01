#encoding:utf-8

"""
#现有的会员数据列表
members=[{"id":"1","tel":"18812345671","discount":"0.98"},
         {"id":"2","tel":"18812345672","discount":"0.9"},
         {"id":"3","tel":"18812345673","discount":"0.8"}]

#根据会员的电话号码，获取指定会员的折扣信息
tel="18812345671"
for member in members:
    if member["tel"]==tel :
        print member["discount"]

#新录入一个tel：18812345671，discount：0.95的会员
members.append({"id":"4","tel":"18812345674","discount":"0.95"})

#获取当前会员的数量
print len(members)
"""
"""
根据客户会员类型，打不同的折扣，并计算顾客的购物总价
会员卡：
黑金卡：8折，白金卡：9折，金卡95折，银卡98折
输入：
卡片类型
购物金额
如输入：Q，停止用户输入，并计算输出总价
"""

memberCard={"黑金卡":"0.8","白金卡":"0.9","金卡":"0.95","银卡":"0.98"}
while 1:
    try:
        memberNumber=int(input("请输入卡片类型代码：1=黑金卡、2=白金卡、3=金卡、4=银卡，："))
        money=int(input("请输入金额："))
        begin=str(raw_input("输入字母't'开始计算总价："))
        if begin=="t":
            if memberNumber==1:
                totle=money*0.8
                print ("您是黑金卡，以为您打8折，折后价为%.2f元"%totle)
            elif memberNumber==2:
                totle=money*0.9
                print ("您是白金卡，以为您打9折，折后价为%.2f元"%totle)
            elif memberNumber==3:
                totle=money*0.95
                print ("您是金卡，以为您打95折，折后价为%.2f元"%totle)
            elif memberNumber==4:
                totle=money*0.98
                print ("您是黑金卡，以为您打98折，折后价为%.2f元"%totle)
            else:
                totle=money
                print ("您不是会员，应付%.2f元"%totle)
        else:
            print ("输入有误，请输入字母't'开始计算总价")
            print

    except:
        print ("输入有误，请输入数字")
        print


#encoding:utf-8

#导包
from member import MemberUtils

#1获取用户手机号，并通过手机号获取用户折扣
userTel=raw_input("请输入手机号：")
userDiscount= MemberUtils.getMemberDisc(userTel)

#获取用户输入的商品信息
def getProductInput():

    while 1:
        try:
            userInput=raw_input("请输入商品的价格果实t进行结算：")
            return float(userInput)
        except ValueError:
            if userInput=='t':
                return 't'
            print ("输入错误，请重新输入")
productList=[]
while 1:
    productInfo=getProductInput()
    print ("%s"%productInfo)
    if productInfo=="t":
        break
    else:
        print ("已添加到商品列表")
        productList.append(productInfo)

#依据输入的商品列表，计算商品的结算清单及总价
def payMenu(productList,userDiscount):
    payList=[]
    payTotal=0
    for i in range(len(productList)):
        payMenuList=[i+1,productList[i],productList[i]*userDiscount]
        payList.append(payMenuList)
        payTotal+=payMenuList[1]*userDiscount
    return payList,payTotal
payList,payTotal=payMenu(productList,userDiscount)

#格式化输出内容
def formatOut(payList,payTotal):
    outMsg="商品id\t原价\t\t折后价\n"
    print outMsg
    for product in payList:
        outMsg +="%s\t\t%s\t%s\n"%(product[0],product[1],product[2])
        print outMsg
    outMsg +="-----------------------\n"
    print outMsg
    outMsg +="总价：%s"%(payTotal)
    print outMsg
    return outMsg
    print outMsg

outPut = formatOut(payList, payTotal)
print
print outPut

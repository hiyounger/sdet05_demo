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
    print ("zzzzzzzzzzzzzzzzzz",productList,userDiscount)
    for i in range(len(productList)):
        payMenuList=[i+1,productList[i],productList[i]*userDiscount]
        print ("ggggg",payMenuList)
        payList.append(payMenuList)
        payTotal+=payMenuList[1]*userDiscount
        print ("grrrrrrrrrr", payTotal)
    return payList,payTotal
payList,payTotal=payMenu(productList,userDiscount)
print (payList,payTotal)
#格式化输出内容
def formatOut(payList,payTotal):
    outMsg="商品id\t原价\t\t折后价\n"
    print (outMsg)
    for product in payList:
        outMsg +="%s\t\t%s\t%s\n"%(product[0],product[1],product[2])
        print (outMsg)
    outMsg +="-----------------------\n"
    print (outMsg)
    outMsg +="总价：%s"%(payTotal)
    print (outMsg)
    return outMsg
    print (outMsg)

outPut = formatOut(payList, payTotal)
print
print outPut

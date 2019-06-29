#encoding:utf-8

class SalesClient():
    #获取用户输入的商品信息
    @classmethod
    def getProductInput(cls):
        while 1:
            try:
                userInput=raw_input("请输入商品的价格按t进行结算：")
                return float(userInput)
            except ValueError:
                if userInput=='t':
                    return 't'
                print ("输入错误，请重新输入")


    #依据输入的商品列表，计算商品的结算清单及总价
    @classmethod
    def payMenu(cls,productList,userDiscount):
        payList=[]
        payTotal=0
        for i in range(len(productList)):
            payMenuList=[i+1,productList[i],productList[i]*userDiscount]
            payList.append(payMenuList)
            payTotal+=payMenuList[1]*userDiscount
        return payList,payTotal

    #格式化输出内容
    @classmethod
    def formatOut(cls,payList,payTotal):
        outMsg="商品id\t原价\t\t折后价\n"
        for product in payList:
            outMsg +="%s\t\t%s\t%s\n"%(product[0],product[1],product[2])
        outMsg +="-----------------------\n"
        outMsg +="总价：%s"%(payTotal)
        return outMsg

    @classmethod
    def Integral(cls,payTotal,newMember,userTel):
        userTel=str(userTel)
        if payTotal >= 5000:
            for i in newMember:
                if userTel == i["tel"]:
                    i["discount"] = 0.9
                    print i
            return i

        elif payTotal>=3000:
            t=-1
            for i in newMember:
                t+=1
                if userTel==i["tel"]:
                    newMember = i
                    newMember["discount"]=0.95
                print "-----------",newMember
            return newMember


        elif payTotal>=1000:
            for i in newMember:
                if userTel==i["tel"]:
                    i["discount"]=0.98
                    print i
            return i
        return newMember


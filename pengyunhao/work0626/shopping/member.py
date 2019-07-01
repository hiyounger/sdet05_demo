#encoding:utf-8

#定义会员信息

member = [{"id": 1, "tel": "1234", "discount": 0.9}]
#定义一个获取会员信息的方法
class MemberUtils():
    @classmethod
    def getMemberDisc(cls,userTel,logoutOrPay):
        if logoutOrPay==1:
            update=input("请输入需要修改的信息:1.编号，2.手机号，3.折扣：")
            if update==1:
                newID=input("请输入编号:")
                for m in member:
                    m["id"]=newID
                    print "修改成功"
                    print m
            elif update==2:
                newTel=str(input("请输入手机号:"))
                for m in member:
                    m["tel"]=newTel
                    print "修改成功"
                    print m
            elif update==2:
                newDiscount=input("请输入折扣:")
                for m in member:
                    m["discount"]=newDiscount
                    print "修改成功"
                    print m
            else:
                print ("输入错误")
        elif logoutOrPay==2:
            for m in member:
                print m
                if m["tel"]==userTel:
                    status=m["status"]="1"
                    print status
                    m["discount"]=1;
                    print "注销成功"
                    print m
        else:
            for m in member:
                if m["tel"]==userTel:
                    return m["discount"]
                    print m["discount"]

        return 1.0
    # @classmethod
    # def getNewMemberDiscount(cls,NewMemberDiscount):
    #     return NewMemberDiscount

    @classmethod
    def AddMember(cls,userTel,newMember):
        newMember={}
        a=1
        id = "id"
        tel = "tel"
        discountKey = "discount"
        discountValue = 1
        for i in member:
            a+=1
            newMember = {id:a,tel:userTel,discountKey:discountValue}
            member.append(newMember)
            newMember=member
            print ("添加成功，持续消费以提升会员等级")
            print member
            break
        return newMember

    @classmethod
    def queryMemberAll(cls,newMember):
        print ("以下是所有会员列表：")
        return newMember
        print newMember

    @classmethod
    def querMember(cls,newMember,userTel):
        userTel=str(userTel)
        memberTel=[]
        print ("一共查到如下会员信息：")
        for i in newMember:
            memberTel.append( i["tel"])
        for i in range(len(memberTel)):
            if memberTel[i][len(memberTel[0])-4:len(memberTel[0])]==userTel:
                print newMember[i]


    @classmethod
    def AllMember(cls,allMember):
        member.append(allMember)
        print "1111",member
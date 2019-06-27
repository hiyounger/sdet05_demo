#encoding:utf-8

#定义会员信息
member=[{"id":"1","tel":"1234","discount":0.9}]
member=[{"id":"1","tel":"12345","discount":0.8}]
#定义一个获取会员信息的方法
class MemberUtils():
    @classmethod
    def getMemberDisc(self,userTel):
        for m in member:
            if m["tel"]==userTel:
                return m["discount"]
        return 1.0

userDiscount=MemberUtils().getMemberDisc("12345")
print userDiscount
userDiscount2=MemberUtils()
print userDiscount2.getMemberDisc("324")
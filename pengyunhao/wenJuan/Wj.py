#encoding:utf-8

class wenJuan():

    count=0
    totalScore=0
    ClsanswerList=[]

    def __init__(self,wechat_id):
        self.userName= wechat_id
        wenJuan.count+=1

    def setQuestings(self):
        return ("q1,q2,q3,q4")

    def answer(self,a1,a2,a3,a4):
        self.answerList=[a1,a2,a3,a4]
        self.score=100
        wenJuan.totalScore+=self.score
        wenJuan.ClsanswerList.append(self.answerList)

    @classmethod
    def getAnswerListById(cls,id):
        targetAnswerList=[]
        for ans in wenJuan01.ClsanswerList:
            targetAnswerList.append(ans[id-4])
        return targetAnswerList


wenJuan01=wenJuan("Tom")
wenJuan01.answer("A","A","A","A")
print wenJuan01.answerList
print wenJuan01.score

wenJuan02=wenJuan("jerry")
wenJuan02.answer("A","B","B","B")
print wenJuan02.answerList
print wenJuan02.score



print wenJuan.count
print wenJuan.totalScore
print "---------------------"
print (wenJuan.getAnswerListById(1))
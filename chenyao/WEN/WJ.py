#encoding:utf-8

class wenjuan():
    count=0
    total=0
    answer_list=[]
    def __init__(self,wechat_id):
        self.name=wechat_id
        wenjuan.count+=1
    def set_question(self):
        return 'Q1,Q2,Q3,Q4'
    def answer_question(self,a1,a2,a3,a4):
        self.answer_list=[a1,a2,a3,a4]
        wenjuan.answer_list.append(self.answer_list)
        self.score=100
        wenjuan.total+= self.score
    @classmethod
    def get_answer_id(self,id):
        answer_id=[]
        for ans in wenjuan.answer_list:
            answer_id.append(ans[id-1])
        return answer_id

wj1=wenjuan('001')
wj1.answer_question('A','B','C','D')
print(wj1.answer_list)
print(wj1.score)

wj2=wenjuan('002')
wj2.answer_question('a','b','c','d')
print(wj2.answer_list)
print(wj2.score)
print('-----------------')
print(wenjuan.count)
print(wenjuan.total)
print(wenjuan.get_answer_id(3))
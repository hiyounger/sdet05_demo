class Wenjuan():
    answer_list = []
    count=0
    total=0
    def __init__(self,wechat_id):
        self.name=wechat_id
        Wenjuan.count+=1
    def set_question(self):
        return "Q1,Q2,Q3,Q4"
    def get_answer(self,a1,a2,a3,a4):
        self.answer_list=[a1,a2,a3,a4]
        Wenjuan.answer_list.append(self.answer_list)
        self.score=100
        Wenjuan.total+=self.score
    @classmethod
    def get_answer_id(cls,id):
        answer_id=[]
        for i in Wenjuan.answer_list:
            answer_id.append(i[id-1])
        return answer_id



wj1=Wenjuan('001')
wj1.get_answer('A','A','C','C')
print wj1.answer_list
print wj1.score

wj2=Wenjuan('001')
wj2.get_answer('A','B','C','D')
print wj2.answer_list
print wj2.score

print Wenjuan.count
print  Wenjuan.total

print Wenjuan.get_answer_id(2)

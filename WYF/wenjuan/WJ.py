# coding:utf-8
class WJ():
    cont=0
    total_score=0
    total_anwser_list=[]

    def __init__(self,weixin_id):
        self.name=weixin_id
        WJ.cont+=1

    def wj_question(self,Q1,Q2,Q3,Q4):
        # self.question_list=[Q1,Q2,Q3,Q4]
        return 'Q1','Q2','Q3','Q4'

    def wj_anwser(self,a1,a2,a3,a4):
        self.anwser_list=[a1,a2,a3,a4]
        WJ.total_anwser_list.append(self.anwser_list)
        self.score=100
        WJ.total_score+=self.score
    @classmethod
    def get_anwser_list_by_id(self,id):
        target_anwser_list =[]
        for ans in WJ.total_anwser_list:
            target_anwser_list.append(ans[id-1])
        return target_anwser_list

id1=WJ('001')
id1.wj_anwser('A','B','C','D')
print(id1.anwser_list)
print(id1.score)
id2=WJ('002')
id2.wj_anwser('A','A','B','D')
print(id2.anwser_list)
print(id2.score)

print(WJ.cont)
print(WJ.total_score)
print(WJ.get_anwser_list_by_id(2))
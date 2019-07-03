# -*- encoding:utf-8 -*-

class WenJuan():

    counter = 0
    total_score = 0
    total_answer_list = []

    def __init__(self, wechat_id):
        self.name = wechat_id
        WenJuan.counter += 1

    def set_questions(self):
        return "Q1, Q2, Q3, Q4"

    def answer_questions(self, a1, a2, a3, a4):
        self.answer_list = [a1, a2, a3, a4]
        self.score = 100
        WenJuan.total_score += self.score
        WenJuan.total_answer_list.append(self.answer_list)

    @classmethod
    def get_answer_list_by_id(cls, id):
        target_answer_list = []
        for ans in WenJuan.total_answer_list:
            target_answer_list.append(ans[id-1])
        return target_answer_list


wj1 = WenJuan('0x001')
wj1.answer_questions('A','A','B','C')
print(wj1.answer_list)
print(wj1.score)

wj2 = WenJuan('0x002')
wj2.answer_questions('A','A','B','B')
print(wj2.answer_list)
print(wj2.score)

print(WenJuan.counter)
print(WenJuan.total_score)
print(WenJuan.get_answer_list_by_id(4))
# -*- encoding:utf-8 -*-

class WenJuan():

    counter = 0

    def __init__(self):
        print("WenJuan 被初始化了，counter+1")
        WenJuan.counter += 1

    def get_questions(cls):
        print("Q1\nQ2\nQ3")

    @classmethod
    def get_wj_counter(cls):
        return cls.counter


wj1 = WenJuan()
print(wj1.get_questions())

wj2 = WenJuan()
print(wj2.get_questions())

wj3 = WenJuan()
print(wj3.get_questions())

print(WenJuan.get_wj_counter())

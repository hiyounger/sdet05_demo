# -*- encoding:utf-8 -*-

#Task 1: 打印小星星


# Task2: 小明、小明
name = "xiaoming"

def change_name(new_name):
    global name
    name = new_name
    print name

print(name)
change_name("XiaoHong")
print(name)
# -*- encoding:utf-8 -*-

import random

# 1. 生成随机数
random_numer = random.randint(0, 100)

counter = 0

# 2. 进入猜数字循环
while True:

    user_input = int(raw_input("请输入一个数字: "))
    counter += 1

    if user_input == random_numer:
        print("恭喜你猜对了，猜了%d次" % counter)
        break
    elif user_input > random_numer:
        print("猜大了")
    else:
        print("猜小了")
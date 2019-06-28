# coding:utf-8

import random
random_number=random.randint(0,100)
b=0
while True:
    while True:
              try:
                 a=int(input("请输入一个数字"))
                 b+=1
                 break
              except:
                 print("输入错误")
    if a==random_number:
        print("恭喜你猜对了，猜了%d次"%b)
        break
    elif a>random_number:
        print("猜大了")
    else:
        print("猜小了")


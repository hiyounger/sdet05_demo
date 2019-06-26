# coding:utf-8
import random
random_numer=random.randint(0,100)
counter=0
while True:
    counter+=1
    a = int(input("请输入数字："))
    if a == random_numer:
     print ("猜对了,猜了%d次"%counter)
     break
    elif a>random_numer:
        print ("猜大了：")
    else:
        print ("猜小了：")















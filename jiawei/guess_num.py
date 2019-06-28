#encoding:utf-8
import random
i=random.randint(0,100)
print(i)
a=0
while True:

    while True:
          try:
              c=int(input("请输入猜测的数字:\n"))
              break

          except:
              print("输入有误，请重新输入！")
    a+=1
    if c==i:
        print("猜对了！一共猜了%d"%a)
        break
    elif c<i:
        print("猜小了！")
    elif c>i:
        print("猜大了！")
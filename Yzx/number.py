#encoding:utf-8
import random
number=random.randint(0,100)
count=0
while True:
    try:
        num1=int(input("输入你猜测的数字："))
    except:
        print "请输入0到100以内的整数"
        continue
    if num1 ==number:
        count+=1
        print ("恭喜你猜对了，一共猜测了%d次"%count)
        break
    elif num1>number:
        count+=1
        print ("猜测大了")
    else:
        count += 1
        print ("猜测小了")




# encoding:utf-8
import random
random_number=random.randint(0,100)
print(random_number)
count=0
# b=int(input('请输入数字：'))
while True:
    try:
        b = int(input("输入你猜测的数字："))
    except:
        print "请输入0到100以内的整数"
        continue
    if b==random_number:
        count+=1
        print('恭喜你，猜对了！一共猜了%d次'%count)
        break
    elif b>random_number:
        count+=1
        print('猜大了')
    else:
        count+=1
        print('猜小了')




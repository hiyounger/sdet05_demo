#   coding:utf-8

import  random
random_numder = random.randint(0,100)
print (random_numder)
a = 0
while True:
    while True:
        try:
            num1=int(input("输入你猜测的数字："))
            a += 1
            break
        except:
            print "请输入0-100以内的数"
    if num1 < random_numder:
        print ('猜小了')
    elif num1 > random_numder:
        print ('猜大了')
    else:
        num1 == num1
        print ('恭喜你猜对了，一共猜了%d次' % (a))
        break

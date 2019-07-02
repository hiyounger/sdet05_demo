#encoding:utf-8
import random
random_num=random.randint(0,101)
print(random_num)
c=0
while True:
    while True:
        try:
          b = int(input('输入一个数字来玩游戏吧!'))
          break
        except:
          print('请重新输入')
    c+=1
    if b==random_num:
        print('恭喜你猜对了，猜了%d次'%(c))
        break
    if b>random_num:
        print('猜大了，再猜一次吧！')
    else:
        print('猜小了，再猜一次吧！')
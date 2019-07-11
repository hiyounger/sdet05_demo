#encoding:utf-8
import random
random_number=random.randint(0,100)
count=0
while True:
    while True:
        try:
          i = int(input('请输入你认为正确的数字：\n'))
          break
        except:
            print ('你的输入有误')
    count=count+1
    if random_number==i:
        print ('恭喜你，你答对了！你一共猜了%d次'%(count))
        break
    if i>random_number:
            print ('你的答案太大了，再来一次')
    if i<random_number:
            print ('你的答案太小了，再来一次')
#encoding:utf-8
food=['武昌鱼','鲍鱼','燕窝','满汉全席','人参果','蟠桃','仙丹']
while True:
    try:
        print ('你今天吃了什么？')
        a=int(input())
        break
    except:
        print ('你的输入有误，请重新输入！')
for f in food:
    print (f)

for i in range(0,11,2):
    if i==0:
        pass
    else:
        print (i)
print (range(0,11,2))


# encoding:utf-8

while True:
    try:
        a=float(input('请输入利润(万元):'))
        break
    except:
        print('请输入数字')

week=['星期一','星期二','星期三','星期四','星期五','星期六','星期天']
for w in week:
    print(w)

for i in range(0,11):
    print(i)

for i in range(0,11,2):
    if i==0:
        pass
    else:
        print(i)

print(range(0,11,2))




#coding:utf-8

week=["星期一","星期二","星期三","星期四","星期五","星期六","星期日"]

for i in week:
    print (i)


for i in range(0,11,2):
    if i==0:
        pass
    else:
        print(i)

print (range(0,11,2))

while True:
    try:
        a=int(raw_input("请输入利润"))
        break
    except:
        print("输入有误")
print ("你输入的利润是%d"%(a))
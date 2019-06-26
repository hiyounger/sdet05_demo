#encoding: utf-8

week=["星期一","星期二","星期三","星期四","星期五","星期六","星期日"]
for day in week:
    print (day)

for i in range(0,15,2):
    if i == 0:
        pass
    else:
        print(i)

print(range(0,15,2))

while True:
    try :
        a=int(input("请输入一个数字："))
        break
    except:
        print("请输入数字")

print(a)

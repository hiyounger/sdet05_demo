# coding:utf-8
#1.打印列表的每一个元素
week=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
for i in week:
    print(i)
print()
#2.规定起始，终止位，步长进行遍历

for i in range(0,11,2):
    if i==0:
        pass
    else:
        print(i)
print()

#3.生成规定起始，终止位，步长的列表
print(range(1,10,2))
print()

#4.获取用户输入，直到用户输入的是一个数值
while True:
    try:
        a=int(raw_input("请输入一个数值"))
        break
    except:
        print("输入错误")
print(a)



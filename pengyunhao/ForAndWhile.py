#encoding:utf-8

#打印列表中的元素
name=["zhangsan","lisi","Tom","Rose","Jack"]
for n in name:
    print (n)

#规定起始位，终止位，步长进行遍历
for i in range(0,11,3):
    print (i)

#生成规定起始位，终止位，步长的列表
print (range(0,11,2))

#获取用户输入，知道用户输入的是一个数值
while 1:
    try:
        a=float(input("请输入利润："))
        break
    except:
        print ("请输入数字")
print (a)
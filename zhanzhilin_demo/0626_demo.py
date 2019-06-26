# coding:utf-8

# 打印列表中的每一个元素
week=str()
week=["星期一","星期二","星期三","星期四","星期五","星期六","星期日"]
for w in week:
    print(w)


# 规定起始、终止位、步长进行遍历
for a in range(1,13,3):
    if a==1:
        pass
    else:
        print (a)


# 生成规定起始、终止位、步长列表
print (range(1,23,3))

# 获取用户输入，直到用户输入的是一个数值
while True:
    try:
        a=str(input("输入字符："))
        break
    except:
        print ("请输入字符")
print (a)










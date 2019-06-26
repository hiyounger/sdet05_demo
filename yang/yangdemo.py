#encoding:utf-8

# 打印列表中的一个元素
list=['周星驰','周润发','张学友','黎明']

for l in list:
    print(l)

# 规定起始，终止位，步长
for i in range(0,11,2):
    if i==0:
        pass
    else:
        print(i)
#生成规定起始，终止位，步长列表
print(range(0,11,2))

# 获取用户输入，直到用户输入的是一个数值

while True:
    try:
        a = float(input("请输入利润："))
        break
    except:
        print("请输入数字")
print(a)



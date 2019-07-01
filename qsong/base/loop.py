# -*- encoding:utf-8 -*-
# 1. 打印列表中的每一个元素
week = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']

for w in week:
    print(w)
# 2. 规定起始、终止位、步长进行遍历
for i in range(0, 11, 2):
    if i == 0:
        pass
    else:
        print(i)

# 3. 生成规定起始、终止位、步长的列表
print(range(0, 11, 2))

# 4. 获取用户输入，直到用户输入的是一个数值
while True:
    try:
        a = float(input("请输入利润（万元）："))
        break
    except:
        print("请输入数字")
print(a)


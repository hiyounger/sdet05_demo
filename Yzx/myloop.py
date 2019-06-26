# encoding:utf-8
week=['1','2','3','4','5','6','7']
for i in week:
    print (i),
print
for i in range(0 , 11 ,2):
    print (i),
print
print (type(range(0,11,2)))
print (range(0,23,2))

while 1:
    try:
        age = int(input("请输入你的年龄："))
        break
    except:
        print ("请输入正确的格式")
print ("你的年龄是：%s岁"%age)
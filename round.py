# coding:utf-8
#while循环用户输入输入，直到获取值是数字
while True:
   try:
      a=int(input("请输入利润："))
      break
   except:
       print ("请重新输入")
print(a)

#for循环打印表中元素
print("")
shuai=["陈冠希","彭于晏","吴彦祖","金城武",]
for b in shuai:
    print(b)

#range函数生成规定起始，终止位，步长的列表
print("")
print(range(1,10,2))

#for循环range函数进行履历
print("")
for i in range(0,13,2):
    if i==0:
        pass
    else:
        print(i)
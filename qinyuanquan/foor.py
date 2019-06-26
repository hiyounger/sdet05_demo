#  coding:utf-8

week = ['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
for w in  week:
    print (w)


for a in range(0,10,2):
    if a==0:
        pass
    else:
       print (a)


print (range(0,10,2))

# while True:
#     try:
#         i = float(input("请输入利润（万元）："))
#         break
#     except:
#         print ("请输入数字")
# print (a)


while True:
    try:
      year = int(input("请输入年份："))
      break
    except:
      print ("请输入年份")

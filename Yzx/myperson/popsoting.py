#encoding:utf-8

# 建立一个popsorting.py 的文件，对列表进行排序：[6,8,10,1,7,3,9]
list1=[6,8,10,1,7,3,9]
for i in range(len(list1)):
    temp=0
    for j in range(len(list1)):
        if list1[j]>list1[i]:
            temp=list1[i]
            list1[i]=list1[j]
            list1[j]=temp
print list1
# 编写一个listsorting方法，接收一个list参数，返回该list参数的排序结果
def listsorting(list):
    for i in range(len(list1)):
        temp = 0
        for j in range(len(list)):
            if list[j]>list[i]:
                temp=list[i]
                list[i]=list[j]
                list[j]=temp
    return list
print (listsorting(list1))

# 编写一个listsorting方法，接收一个list参数和sort参数(desc, asc)，返回该list参数的对应排序结果
def listsorting(list , sort):
    if sort=='desc':
        for i in range(len(list1)):
            temp = 0
            for j in range(len(list)):
                if list[j] > list[i]:
                    temp = list[i]
                    list[i] = list[j]
                    list[j] = temp
        return list
    elif sort=='asc':
        for i in range(len(list1)):
            temp = 0
            for j in range(len(list)):
                if list[j] < list[i]:
                    temp = list[i]
                    list[i] = list[j]
                    list[j] = temp
        return list
print (listsorting(list1,'desc'))
print (listsorting(list1,'asc'))

# 增强listsorting()方法，对传入的参数进行判断，是否是列表，列表内容是否都是数字
def listsorting(sort,list):
    try:
        for i in range(len(list)):
            list[i]=int(list[i])
    except :
        return "列表中存在非数字"
    if sort=='desc':
        for i in range(len(list1)):
            temp = 0
            for j in range(len(list)):
                if list[j] > list[i]:
                    temp = list[i]
                    list[i] = list[j]
                    list[j] = temp
        return list
    elif sort=='asc':
        for i in range(len(list1)):
            temp = 0
            for j in range(len(list)):
                if list[j] < list[i]:
                    temp = list[i]
                    list[i] = list[j]
                    list[j] = temp
        return list
print listsorting('desc',list1)
print listsorting('desc',['q1',1,2,7,4,6,2])
# coding:utf-8
# 1、对list进行排序
# pop_list=[6,8,10,1,7,3,9]

# pop_list.sort()
#
# print pop_list

# 2、编写一个listsorting方法，接收一个list参数，返回该list参数的排序结果
def listsorting(list):
    for a in range(len(list)):
        for b in range(0,len(list)-a-1):
            if list[b]>list[b+1]:
                list[b],list[b+1]=list[b+1],list[b]
list = [6, 8, 10, 1, 7, 3, 9]
listsorting(list)
print list

# 3、编写一个listsorting方法，接收一个list参数和sort参数(desc, asc)，返回该list参数的对应排序结果
def listsorting(list,sort):
    for a in range(len(list)):
        for b in range(0,len(list)-a-1):
            if list[b]>list[b+1]:
                list[b],list[b+1]=list[b+1],list[b]
















# encoding:utf-8


# list = [6,8,10,1,7,3,9]
# list.sort()
# print list

#
# def listsorting():
#     list = [6, 8, 10, 1, 7, 3, 9]
#     a = len(list)
#     for i in range(a - 1):
#         for n in range(i + 1, a):
#             if list[i] > list[n]:
#                 list[i], list[n] = list[n], list[i]
#     print list

list = [6, 8, 10, 1, 7, 3, 9]
list1 = []
c=len(list)
for a in range(len(list)-1):
    for b in range(a+1,len(list)):
        if list[b]>list[a]:
            list[b],list[b+1]=list[b+1],list[b]
print list1

    # return list.sort()

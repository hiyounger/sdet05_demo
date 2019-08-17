# coding:utf-8
list = [2, 1, 7, 3, 9, 5, 4, 8, 0, 3, 4]

for i in range(len(list)):
    for j in range(i, len(list)):
        if list[i] > list[j]:
            min = list[j]
            list[j] = list[i]
            list[i] = min
    print (list)

print (list)

print "=============================================="

list = [2, 1, 7, 3, 9, 5, 4, 8, 0, 3, 4]

for i in range(len(list)):
    for j in range(len(list) - 1):
        if list[j] > list[j + 1]:
            min = list[j + 1]
            list[j + 1] = list[j]
            list[j] = min
    print (list)

print (list)

#-*- encoding:utf-8 -*-
#第一题
start_list=[6,8,10,1,7,3,9]
for i in range(len(start_list)-1):
    for i in range(len(start_list)-1):
        if start_list[i]>start_list[i+1]:
            max=start_list[i]
            start_list[i]=start_list[i+1]
            start_list[i+1]=max
print start_list

#第二题
def listsorting(list):
    for i in range(len(list) - 1):
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                max = list[i]
                list[i] = list[i + 1]
                list[i + 1] = max

    return (list)

print (listsorting(start_list))

#第三题
def listsorting(list,sort):
    if sort=="asc":
        for i in range(len(list) - 1):
            for i in range(len(list) - 1):
                if list[i] > list[i + 1]:
                    max = list[i]
                    list[i] = list[i + 1]
                    list[i + 1] = max
        return (list)
    if sort=="desc":
        for i in range(len(list) - 1):
            for i in range(len(list) - 1):
                if list[i] < list[i + 1]:
                    min = list[i]
                    list[i] = list[i + 1]
                    list[i + 1] = min
        return (list)

print (listsorting(start_list,"asc"))
print (listsorting(start_list,"desc"))

#第五题（未做完）
def listsorting5(list,sort):
    print (type(list))
    if list!="<type 'list'>":
        return ("")
    if sort=="asc":
        for i in range(len(list) - 1):
            for i in range(len(list) - 1):
                if list[i] > list[i + 1]:
                    max = list[i]
                    list[i] = list[i + 1]
                    list[i + 1] = max
        return (list)
    if sort=="desc":
        for i in range(len(list) - 1):
            for i in range(len(list) - 1):
                if list[i] < list[i + 1]:
                    min = list[i]
                    list[i] = list[i + 1]
                    list[i + 1] = min
        return (list)

print (listsorting5(start_list,"asc"))
print (listsorting5(start_list,"desc"))

#第四题
class popsoting ():
    @classmethod
    def listsorting(cls,list, sort):
        if sort == "asc":
            for i in range(len(list) - 1):
                for i in range(len(list) - 1):
                    if list[i] > list[i + 1]:
                        max = list[i]
                        list[i] = list[i + 1]
                        list[i + 1] = max
            return (list)
        if sort == "desc":
            for i in range(len(list) - 1):
                for i in range(len(list) - 1):
                    if list[i] < list[i + 1]:
                        min = list[i]
                        list[i] = list[i + 1]
                        list[i + 1] = min
            return (list)








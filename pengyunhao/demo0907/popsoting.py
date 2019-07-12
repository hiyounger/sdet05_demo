#encoding:utf-8

#list=[6,8,10,1,7,3,9]

def listsorting(list,desc_or_asc):
    if isinstance(list,list):
        if desc_or_asc=="desc":
            for i in range(len(list)):
                for j in range(len(list)-1):
                    if list[j]>list[j+1]:
                        a=list[j]
                        list[j]=list[j+1]
                        list[j+1]=a
            print list
            return list
        else:
            for i in range(len(list)):
                for j in range(len(list)-1):
                    if list[j]<list[j+1]:
                        a=list[j]
                        list[j]=list[j+1]
                        list[j+1]=a
            print list
            return list




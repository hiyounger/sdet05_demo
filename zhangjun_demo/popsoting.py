#encoding:utf-8

# 对字典进行排序：[6,8,10,1,7,3,9]
#
# 先转换成列表：
# a=3
# print (type(a))
a=[6,8,10,1,7,3,9]
# a=list(a)
#再排序：
for i in range(len(a)-1):
    for j in range(len(a)-1-i):
        if a[j]>a[j+1]:
            tem=a[j]
            a[j]=a[j+1]
            a[j+1]=tem
print (a)
#默认正序：
a.sort()
print (a)

class HomeWork:
    def listsorting(self,a):
        for i in range(len(a) - 1):
            for j in range(len(a) - 1 - i):
                if a[j] > a[j + 1]:
                    tem = a[j]
                    a[j] = a[j + 1]
                    a[j + 1] = tem
        return a
    def listsort(self,a,sort):
        if sort=='asc':
            for i in range(len(a) - 1):
                for j in range(len(a) - 1 - i):
                    if a[j] > a[j + 1]:
                        tem = a[j]
                        a[j] = a[j + 1]
                        a[j + 1] = tem
                return  a
        elif sort=='desc':
            for i in range(len(a) - 1):
                for j in range(len(a) - 1 - i):
                    if a[j] < a[j + 1]:
                        tem = a[j]
                        a[j] = a[j + 1]
                        a[j + 1] = tem
                return  a

con=HomeWork()
a=[6,8,10,1,7,3,9]
print (con.listsorting(a))
print (type(a))

print (con.listsort(a,'desc'))

def Sort(a):
    try:
        type(a)=='list'
    except:
        print ('你输入的非列表')
    for nun in range(a):
         if type(a)=='int':
            print ()
         else:
             print ('列表有非数字')




#encoding:utf-8
for i in range(1,10):
     for j in range(1,i+1):
         print ('*'),
     print


name='小明'
def change_name(new_name):
    # global name
    name=new_name
    print (name)
print (name)
change_name('小张')
print (name)


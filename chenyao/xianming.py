# encoding:utf-8
name='xiaoming'
def change_name(new_name):
    global name
    name=new_name
    print(name)

print(name)
change_name('xiaohong')
print(name)


#encoding:utf-8
# for i in range(5):
#     for i in range(i+1):
#         print('*'),
#     print

name="小明"
def change_name(new_name):
    global name
    name=new_name
    print(name)
print(name)
change_name("小刚")
print(name)
# coding:UTF-8
# for循环打印星星
# for i in range(5):
#     for i in range(i+1):
#       print "*"  ,
#     print

# 作用域
name="彭于晏"
def change_name(new_name):
    global name
    name=new_name
    print name

print(name)
change_name("陈冠希")
print(name)
#coding:utf-8

for i in range(10):
    for i in range(i+1):
        print ("*"),
    print

name="xiaowei"
def change_name(new_name):
    # global name
    name=new_name
    print (name)

print (name)
change_name("xiaozhang")
print (name)
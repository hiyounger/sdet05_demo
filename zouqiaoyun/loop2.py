# coding:utf-8

for i in range(5):
      for j in range(i+1):
          print("*"),
      print

name="xiaoming"

def change_name(newname):
    global name
    name=newname
    print(name)
print(name)
change_name("xiaohong")
print(name)
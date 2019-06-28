#   coding:utf-8

neme = "xiaoming"

def change_name (new_name):
    global neme
    new_name = neme
    print neme

print (neme)
change_name("xiaohong")
print (neme)


for i in range(5):
    for i in range(i+1):
        print ('*'),
    print


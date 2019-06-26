#encoding: utf-8
# for i in range(9):
#     for x in range(i+1):
#         print ("*"),
#     print

name="xiaobai"
def change_name(new_name):
    # global name
    name=new_name
    print name
print (name)
change_name("xiaohei")
print(name)
for i in range(6):
    for i in range(i+1):
        print "*",
    print


name="Tom"
def ChangeName(Nname):
    global name
    name = Nname
    print name
print name
ChangeName("Jarry")
print name

a=1
print type(a)
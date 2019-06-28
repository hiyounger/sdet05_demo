#coding:utf-8

kehus=[
    {"id":"1","tel":"18812344321","zhekou":"9"},
    {"id":"2","tel":"18812344322","zhekou":"8"},
    {"id":"3","tel":"18812344323","zhekou":"9.8"}
]
tel="18812344321"
for i in kehus:
    if i["tel"]==tel:
        print(i["zhekou"])

kehus.append({"id":"4","tel":"18812344324","zhekou":"8"})

print (len(kehus))

# coding:utf-8

members=[
    {"id":"1","tel":"18902371234","discount":"0.95"},
    {"id":"2","tel":"18302531239","discount":"0.98"},
    {"id":"3","tel":"13503321236","discount":"0.80"}
]

tel="18302531239"
for member in members:
    if member["tel"]==tel:
        print(member["discount"])
members.append({"id":"4","tel":"12590178902","discount":"0.75"})
print(len(members))
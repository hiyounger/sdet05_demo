#encoding:utf-8
members=[
    {'id':001,'tel':'15912345678','discount':'0.8'},
    {'id':002,'tel':'15912345679','discount':'0.85'},
    {'id':003,'tel':'15912345670','discount':'0.9'}
]
tel='15912345678'
for member in members:
    if member["tel"]==tel:
        print(member['discount'])

members.append({'id':004,'tel':'15912345671','discount':'0.95'})
print(len(members))

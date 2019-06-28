#   coding:utf-8

members = [
    {'id':'1','tel':"18812345671",'discount':'0.98'},
    {'id':'2','tel':"18812345672",'discount':'0.9'},
    {'id':'3','tel':"18812345673",'discount':'0.8'},
]

tel = '18812345672'
for member in members:
    if member['tel'] == tel:
        print (member['discount'])

members.append({'id':'4','tel':"18812345674",'discount':'0.95'})

print (len(members))
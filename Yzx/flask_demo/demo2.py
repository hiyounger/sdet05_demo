#encoding:utf-8
from flask import Flask
members=[
    {'id':'1','tel':'18845871680','disc':0.9,'state':1,'points':0000},
    {'id':'2','tel':'18845095099','disc':0.1,'state':1,'points':0000}
]
app=Flask('__mian__')
@app.route('/')
@app.route('/<members1>')
def get_members_all(members1):
    members1 = '编号\t\t手机号\t折扣\t积分\n'
    for mem in members:
        members1 += "%s\t%s\t%s\t%s\n" % (mem['id'], mem['tel'], mem['disc'], mem['score'])
    return str(members1)
if __name__=='__main__':
    app.run()

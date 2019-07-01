#encoding:utf-8
from flask import Flask
from Yzx.Person.homework0628.shop.members import Members
members=[
    {'id':'1','tel':'18845871680','disc':0.9,'state':1,'points':0000},
    {'id':'2','tel':'18845095099','disc':0.1,'state':1,'points':0000}
]
app=Flask('__main__')
@app.route('/')
def say_hellow_flask():
    return 'Hellow Flask'
@app.route('/hellow')
@app.route('/hellow/<name>')
def say_hellow_world(name='World'):
    return "Hellow %s"%name
# @app.route('/members')
# def get_members():
#      Members.get_members_all()

@app.route('/du')
@app.route('/du/<out_all>')
def get_members_all(out_all=None):
    # list=[]
    # for mem in members:
    #     out_members=("会员编号：%s\t电话%s\t折扣%s\t状态%s\t积分" % (mem['id'], mem['tel'], mem['disc'], mem['state'], mem['points']))
    #     list.append(out_members)
    # return list
    out_all = '编号\t\t手机号\t折扣\t积分\n'
    for mem in members:
        out_all += "%s\t%s\t%s\t%s\n" % (mem['id'], mem['tel'], mem['disc'], mem['score'])
    return str(out_all)
if __name__=='__main__':
    app.run()
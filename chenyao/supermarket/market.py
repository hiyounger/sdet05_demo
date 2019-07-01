# encoding:utf-8

from flask import Flask,request
from chenyao.supermarket.model.member import Members

app=Flask('__main__')

@app.route('/')
def say_hello():
    return 'hello Flask'

@app.route('/file')
@app.route('/file/<name>')
def say_hello2(name='world'):
    return 'hello %s'%name
# @app.route('/')
# @app.route('/<out_all>')
# def members_all(out_all=None):
#     out_all='编号\t\t手机号\t折扣\t积分\n'
#     for mem in members:
#         out_all+="%s\t%s\t%s\t%s\n"%(mem['id'],mem['tel'],mem['disc'],mem['score'])
#     return out_all
@app.route('/members',methods=['GET','POST'])
@app.route('/members/<condition>')
def show_members(condition=None):
    if request.method=='GET':
        if condition==None:
            members_list=str(Members.show_members())
        else:
            if condition.startswith('tel_'):
                tel=condition.split('_')[-1]
                members_list = str(Members.show_members_tel(tel))
            else:
                uid=condition.split('_')[-1]
                members_list = str(Members.show_members_uid(uid))
        return members_list
    else:
        tel=request.form['tel']
        new_member=Members.add_member(tel)
        return str(new_member)

if __name__ == '__main__':
    app.run()
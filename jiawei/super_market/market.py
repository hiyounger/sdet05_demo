# encoding:utf-8
from flask import Flask
from jiawei.super_market.model.members import Member

app = Flask('__main__')


# @app.route('/')
# def say_hello():
#     return('hello mayun')

# @app.route('/hello')
# @app.route('/hello/<name>')
# def sel_mem(name='world'):
#     return "hello %s"% name


@app.route("/member")
@app.rout('/member/<condition>')
def get_all_members(condition=None):
    if condition == None:
        member_list = str(Member.get_all_member())
    else:
        if condition.startswith('tel_'):
            tel = condition.split('_')[-1]
            member_list = str(Member.get_member_by_tel(tel))
        else:
            uid = condition.split('_')[-1]
            member_list = str(Member.get_member_by_uid(uid))
    return member_list


if __name__ == '__main__':
    app.run()

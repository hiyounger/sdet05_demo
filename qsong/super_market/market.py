# -*- encoding:utf-8 -*-

from flask import Flask, request

from qsong.super_market.model.members import Member

app = Flask('__main__')


@app.route('/')
def say_hello():
    return "Hello Flask"


@app.route("/member", methods=['GET', 'POST'])
@app.route('/member/<condition>')
def get_all_members(condition=None):
    if request.method == 'GET':
        if condition == None:
            member_list = str(Member.get_all_members())
        else:
            if condition.startswith("tel_"):
                tel = condition.split("_")[-1]
                member_list = str(Member.get_members_by_tel(tel))
            else:
                uid = condition.split("_")[-1]
                member_list = str(Member.get_members_by_uid(uid))
        return member_list
    else:
        tel = request.form['tel']
        new_member = Member.add_member(tel)
        return str(new_member)


if __name__ == '__main__':
    app.run()

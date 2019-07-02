# -*- encoding:utf-8 -*-

from flask import Flask, request, jsonify

from qsong.super_market.model.members import Member

app = Flask('__main__')

@app.route('/jsontest')
def json_test():
    ret_dic = {
        'return_code': '200',
        'msg': 'get member list success',
        'members':[{'id': '1', 'tel': "18812345672", 'discount': 0.95},
                   {'id': '2', 'tel': "18812345673", 'discount': 0.9},
                   {'id': '3', 'tel': "18812345674", 'discount': 0.9},
                   {'id': '4', 'tel': "18812345671", 'discount': 0.8},
                   {'id': '5', 'tel': "18811345671", 'discount': 0.8}
                   ]
    }
    return jsonify(ret_dic)


@app.route('/')
def say_hello():
    return "Hello Flask"




@app.route("/member", methods=['GET', 'POST'])
@app.route('/member/<condition>', methods=['GET', 'PUT','PATCH'])
def get_all_members(condition=None):
    if request.method == 'GET':
        if condition == None:
            member_list = Member.get_all_members()
            member_list['return_code'] = 200
            member_list['return_msg'] = '获取用户成功'
        else:
            if condition.startswith("tel_"):
                tel = condition.split("_")[-1]
                member_list = Member.get_members_by_tel(tel)
                member_list['return_code'] = 200
                member_list['return_msg'] = 'Get Member by tel success'
            else:
                uid = condition.split("_")[-1]
                member_list = Member.get_members_by_uid(uid)
                member_list['return_code'] = 200
                member_list['return_msg'] = 'Get Member by uid success'
        return jsonify(member_list)
    elif request.method == 'POST':
        tel = request.form['tel']
        new_member = Member.add_member(tel)
        return jsonify(new_member)
    elif request.method == 'PUT':
        uid = condition.split("_")[-1]
        tel = request.form['tel']
        discount = request.form['discount']
        active = request.form['active']
        user_info = {'tel':tel, 'discount':discount, 'active':active}
        ret_dic = Member.update_member_info(uid, user_info)
        if len(ret_dic.keys()) == 0:
            ret_dic['return_code'] = 404
            ret_dic['return_msg'] = 'Update user by user info failed'
        else:
            ret_dic['return_code'] = 200
            ret_dic['return_msg'] = 'Update user by user info success'
        return jsonify(ret_dic)
    elif request.method == 'PATCH':
        uid = condition.split("_")[-1]
        score = request.form['score']
        ret_dic = Member.update_member_score(uid, score)
        ret_dic['return_code'] = 200
        ret_dic['return_msg'] = 'Update user score success'
        return jsonify(ret_dic)
    else:
        ret_dic = {'return_code':'200', 'return_msg':'什么也没做'}
        return jsonify(ret_dic)


if __name__ == '__main__':
    app.run()

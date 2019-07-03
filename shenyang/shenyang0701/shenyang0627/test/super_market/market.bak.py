# coding:utf-8

from flask import Flask, request, jsonify

from shenyang.shenyang0701.shenyang0627.test.super_market.model import members

app = Flask('__main__')


@app.route('/')
def say_word():
    return "丢雷楼某"


@app.route('/jsontest')
def json_test():
    ret_dic = {
        'return_code': '200',
        'msg': 'get member list success',
        'members': [{'uid': '1', 'tel': '13912345671', 'disc': 0.8},
                    {'uid': '2', 'tel': '13912345672', 'disc': 0.9},
                    {'uid': '3', 'tel': '13912345673', 'disc': 0.95},
                    {'uid': '4', 'tel': '13912345674', 'disc': 0.98}
                    ]
    }
    return jsonify(ret_dic)


@app.route('/member', methods=['GET', 'POST'])
@app.route('/member/<condition>', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
def get_all_members(condition=None):
    if request.method == 'GET':
        if condition == None:
            member_list = members.Member.get_all_members()
            member_list["return_code"] = 200
            member_list['return_msg'] = 'Get Member list success'
        else:
            if condition.startswith('tel_'):
                tel = condition.split('_')[-1]
                member_list = members.Member.get_members_by_tel(tel)
                member_list['return_code'] = 200
                member_list['return_msg'] = 'Get Member by tel success'
            else:
                uid = condition.split('_')[-1]
                member_list = members.Member.get_members_by_uid(uid)
                member_list['return_code'] = 200
                member_list['return_msg'] = 'Get Member by uid success'
        return jsonify(member_list)

    elif request.method == 'POST':
        tel = request.form['tel']
        new_member = members.Member.add_member(tel)
        return jsonify(new_member)

    elif request.method == 'PUT':
        uid = condition.split('_')[-1]
        tel = request.form['tel']
        discount = request.form['discount']
        active = request.form['active']
        user_info = {'tel': tel, 'discount': discount, 'active': active}
        ret_dic = members.Member.update_member_info(uid, user_info)
        if len(ret_dic.keys()) == 0:
            ret_dic['return_code'] = 404
            ret_dic['return_msg'] = "Update user bu user info failed"

        else:
            ret_dic['return_code'] = 200
            ret_dic['return_msg'] = 'Update user by user info success'
        return jsonify(ret_dic)

    elif request.method == 'PATCH':
        uid = condition.split("_")[-1]
        score = request.form['score']
        ret_dic = members.Member.update_member_score(uid, score)
        ret_dic['return_code'] = 200
        ret_dic['return_msg'] = "Update user score success"
        return jsonify(ret_dic)

    elif request.method == 'DELETE':
        uid = condition.split("_")[-1]
        ret_dic = members.Member.inactive_member(uid)
        ret_dic['return_code'] = 200
        ret_dic['return_msg'] = 'Inactive user success'
        return jsonify(ret_dic)


    else:
        ret_dic = {'return_code': '200', 'return_msg': '什么也没做'}
        return jsonify(ret_dic)


if __name__ == '__main__':
    app.run(port=5001)

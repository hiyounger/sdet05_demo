# encoding:utf-8
from flask import Flask, request, jsonify
from zhazhahui.super_market.tools.logger import debug
from zhazhahui.super_market.model.members import Member

app = Flask(__name__)


@app.route('/')
def json_test():
    ret_dic = {
        'return_code': '200',
        'msg': 'get member list success',
        'member': [
            {'uid': '1', 'tel': '13312345678', 'disc': 0.9, 'state': "live", 'itg': 5080},
            {'uid': '2', 'tel': '13312345679', 'disc': 0.85, 'state': "live", 'itg': 10880},
            {'uid': '3', 'tel': '13312345670', 'disc': 0.95, 'state': "live", 'itg': 3500},
            {'uid': '4', 'tel': '13419591290', 'disc': 0.98, 'state': "die", 'itg': 1300},
            {'uid': '5', 'tel': '13412345678', 'disc': 0.9, 'state': "live", 'itg': 5080}
        ]
    }
    return jsonify(ret_dic)


#
# @app.route("/member")
# # @app.route("/member/<tel>")
# def get_all_members(tel=None):
#     if tel == None:
#         member_list = str(Member.get_all_member())
#     else:
#         member_list = str(Member.get_members_by_tel(tel))
#     return member_list

@app.route('/filter/score')
def filter_member_by_score():
    score = request.args['le']
    debug('Get request args score=' + str(score))
    ret_dic = Member.filter_member_by_score(score)
    ret_dic['return_code'] = 200
    ret_dic['return_msg'] = 'Fliter uesr success'
    return jsonify(ret_dic)


@app.route("/member", methods=['GET', 'POST'])
@app.route("/member/<condition>", methods=['GET', 'PUT', 'PATCH', 'DELETE'])
def get_all_members(condition=None):
    if request.method == 'GET':
        if condition == None:
            member_list = Member.get_all_members()
            member_list['return_code'] = 200
            member_list['return_msg'] = 'Get Member list Success'

        else:
            # print("condition: %s" % condition)
            if condition.startswith("tel_"):
                tel = condition.split("_")[-1]
                member_list = Member.get_members_by_tel(tel)
                member_list['return_code'] = 200
                member_list['return_msg'] = 'Get Member by tel Success'
            else:
                uid = condition.split("_")[-1]
                member_list = Member.get_members_by_uid(uid)
                member_list['return_code'] = 200
                member_list['return_msg'] = 'Get Member by uid Success'
        return jsonify(member_list)

    elif request.method == "POST":
        tel = request.form["tel"]
        newmember = Member.add_member(tel)
        return jsonify(newmember)

    elif request.method == 'PUT':
        uid = condition.split("_")[-1]
        tel = request.form['tel']
        discount = request.form['discount']
        active = request.form['active']
        user_info = {'tel': tel, 'discount': discount, 'active': active}
        ret_dic = Member.update_member_info(uid, user_info)
        if len(ret_dic.key()) == 0:
            ret_dic['return_code'] = 404
            ret_dic['return_msg'] = 'Update user by user info failed'
        else:
            ret_dic['return_code'] = 200
            ret_dic['return_msg'] = 'Update user by user info success'
        return jsonify(ret_dic)

    elif request.method == "PATCH":
        uid = condition.split("_")[-1]
        score = request.form["score"]
        ret_dic = Member.update_member_score((uid, score))
        ret_dic['return_code'] = 200
        ret_dic['return_msg'] = 'Update user score success'
        return jsonify(ret_dic)

    elif request.method == "DELETE":
        uid = condition.split("_")[-1]
        ret_dic = Member.incative_member(uid)
        ret_dic['return_code'] = 200
        ret_dic['return_msg'] = 'Inactive user success'
        return jsonify(ret_dic)
    else:
        ret_dic = {'return_code': '200', 'return_msg': '什么也不做'}

        return jsonify(ret_dic)


if __name__ == '__main__':
    app.run()

# 对这一段不理解
# member_list['return_code'] = 200
# member_list['return_msg'] = 'Get Member by uid Success'

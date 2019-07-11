# encoding:utf-8
from flask import Flask, request, jsonify
from zhangjun_demo.super_maket.model.members_zj import Member

app = Flask('__main__')


@app.route('/members', methods=['GET', 'POST'])
@app.route('/members/<condition>', methods=['GET', 'PUT', 'PATCH', 'DELECT'])
# @app.route('/filter/score')
# def filter_member_by_score():
#     score=request.args['le']
#     ret_dic=Member.filter_member_by_score(score)
#     ret_dic['return_code'] = 200
#     ret_dic['return_msg'] = 'Get Member by id success'
#     return jsonify(ret_dic)

def get_all_members(condition=None):
    if request.method == 'GET':
        if condition == None:
            member_list = Member.get_all_members()
            member_list['return_code'] = 200
            member_list['return_msg'] = 'Get Member list success'
        else:
            if condition.startswith('tel_'):
                tel = condition.split('_')[-1]
                member_list = Member.get_member_list(tel)
                member_list['return_code'] = 200
                member_list['return_msg'] = 'Get Member list success'
            else:
                id = condition.split('_')[-1]
                member_list = Member.get_members_by_id(id)
                member_list['return_code'] = 200
                member_list['return_msg'] = 'Get Member by id success'

        return jsonify(member_list)
    elif request.method == 'POST':
        tel = request.form['tel']
        new_member = Member.add_vip(tel)
        return jsonify(new_member)
    elif request.method == 'PUT':
        id = condition.split('_')[-1]
        tel = request.form['tel']
        discount = request.form['discount']
        active = request.form['active']
        print (id)
        user_info = {'tel': tel, 'discount': discount, 'active': active}
        ret_dic = Member.update_member(id, user_info)
        if len(ret_dic.keys()) == 0:
            ret_dic['return_code'] = 404
            ret_dic['return_msg'] = 'Get Member by id failed'
        else:
            ret_dic['return_code'] = 200
            ret_dic['return_msg'] = 'Get Member by id success'
        return jsonify(ret_dic)
    elif request.method == 'PATCH':
        id = condition.split("_")[-1]
        score = request.form['score']
        ret_dic = Member.update_member_score(id, score)
        ret_dic['return_code'] = 200
        ret_dic['return_msg'] = 'Update user score success'
        return jsonify(ret_dic)
    elif request.method == 'DELECT':
        id = condition.split("_")[-1]
        ret_dic = Member.inactive_members(id)
        ret_dic['return_code'] = 200
        ret_dic['return_msg'] = 'Update delect active success'
        return jsonify(ret_dic)
    else:
        ret_dic = {'return_code': '200', 'return_msg': '什么也没做'}
        return jsonify(ret_dic)


if __name__ == '__main__':
    app.run()

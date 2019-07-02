# encoding:utf-8
from flask import Flask, request, jsonify
from chenyao.supermarket.model.member import Members

app = Flask('__main__')
@app.route('/')
def say_hello():
    return 'hello Flask'
@app.route('/file')
@app.route('/file/<name>')
def say_hello2(name='world'):
    return 'hello %s' % name
# @app.route('/')
# @app.route('/<out_all>')
# def members_all(out_all=None):
#     out_all='编号\t\t手机号\t折扣\t积分\n'
#     for mem in members:
#         out_all+="%s\t%s\t%s\t%s\n"%(mem['id'],mem['tel'],mem['disc'],mem['score'])
#     return out_all
@app.route('/jsontest')
def json_test():
    json_set = {
        'rerurn_code': '200',
        'msg': 'succes',
        'members': [
            {'id': '1', 'tel': '13312345671', 'disc': 0.9, 'score': 0},
            {'id': '2', 'tel': '13312345672', 'disc': 0.8, 'score': 0},
            {'id': '3', 'tel': '13312345673', 'disc': 0.7, 'score': 0},
            {'id': '4', 'tel': '13312345674', 'disc': 0.6, 'score': 0},
            {'id': '5', 'tel': '13311145671', 'disc': 0.9, 'score': 0}
        ]
    }
    return jsonify(json_set)

@app.route('/members', methods=['GET', 'POST'])
@app.route('/members/<condition>', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
def show_members(condition=None):
    if request.method == 'GET':
        if condition == None:
            members_list = Members.show_members()
            return jsonify(members_list)
        else:
            if condition.startswith('tel_'):
                tel = condition.split('_')[-1]
                members_list = Members.show_members_tel(tel)
                return jsonify(members_list)
            else:
                uid = condition.split('_')[-1]
                members_list = Members.show_members_uid(uid)
                return jsonify(members_list)
        return jsonify(members_list)
    elif request.method == 'POST':
        tel = request.form['tel']
        new_member = Members.add_member(tel)
        return jsonify(new_member)
    elif request.method == 'PUT':
        uid = condition.split('_')[-1]
        tel = request.form['tel']
        discount = request.form['disc']
        active = request.form['active']
        user_info = {'tel': tel, 'disc': discount, 'active': active}
        tet_dict = Members.update_member(uid, user_info)
        if len(tet_dict) == 0:
            tet_dict['result_code'] = 404
            tet_dict['result_msg'] = 'update user by user_info failed'
        else:
            tet_dict['result_code'] = 200
            tet_dict['result_msg'] = 'update user by uid succes'
        return jsonify(tet_dict)
    elif request.method == 'PATCH':
        uid = condition.split('_')[-1]
        score = request.form['score']
        tet_dict = Members.update_member_score(uid, score)
        tet_dict['result_code'] = 200
        tet_dict['result_msg'] = 'update user by score succes'
        return jsonify(tet_dict)
    elif request.method == 'DELETE':
        uid = condition.split('_')[-1]
        tet_dict = Members.inactive_member(uid)
        tet_dict['result_code'] = 200
        tet_dict['result_msg'] = 'inactive user  succes'
        return jsonify(tet_dict)
    else:
        tet_dict = {'result_code': 200, 'result_msg': '没有进行操作'}
        return jsonify(tet_dict)

@app.route('/filter/score')
def filter_member_by_score():
    score = request.args['le']
    tet_dict = Members.filter_member_by_score(score)
    tet_dict['result_code'] = 200
    tet_dict['result_msg'] = 'Filter user  succes'
    return jsonify(tet_dict)

if __name__ == '__main__':
    app.run()

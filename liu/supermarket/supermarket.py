# encoding:utf-8
from flask import Flask, request,jsonify
from liu.supermarket.model.members import Member

app = Flask('__main__')

@app.route('/hello')
def say_hello():
    return 'hello Flask'


app = Flask('__main__')


@app.route('/members', methods=['GET', 'POST','PUT','PATCH','DELETE'])
@app.route('/members/<condition>', methods=['GET', 'POST','PUT','PATCH','DELETE'])
def get_all_members(condition=None):
    if request.method == 'GET':
        if condition == None:
            member_list = Member.get_all_members()
            member_list['return_code'] = 200
            member_list['return_msg'] = 'get member list success'
        else:
            if condition.startswith('tel_'):
                tel = condition.split('_')[-1]
                member_list = Member.get_member_by_tel(tel)
                member_list['return_code'] = 200
                member_list['return_msg'] = 'get member by tel success'
            else:
                uid = condition.split('_')[-1]
                member_list = Member.get_member_by_uid(uid)
                member_list['return_code'] = 200
                member_list['return_msg'] = 'get member by uid success'
        return jsonify(member_list)
    elif request.method == 'PUT':
        uid = condition.split('_')[-1]
        tel = request.form['tel']
        disc = request.form['disc']
        active = request.form['active']
        new_user_info = {'tel':tel,'disc':disc,'active':active}
        ret_dic = Member.update_member_info(uid, new_user_info)
        if len(ret_dic) == 0:
            ret_dic['return_code'] = 404
            ret_dic['return_msg'] = 'Update user by user info failed '
        else:
            ret_dic['return_code'] = 200
            ret_dic['return_msg'] = 'Update user by user info success'
        return jsonify(ret_dic)
    elif request.method == 'PATCH':
        uid = condition.split('_')[-1]
        score = request.form['score']
        ret_dic = Member.update_member_score(uid,score)
        ret_dic['return_code'] = 200
        ret_dic['return_msg'] = 'Update user score success'
        return jsonify(ret_dic)
    elif request.method == 'DELETE':
        uid = condition.split('_')[-1]
        ret_dic = Member.inactive_member(uid)
        ret_dic['return_code'] = 200
        ret_dic['return_msg'] = 'Inactive user success'
        return jsonify(ret_dic)
    else:
        if request.method == 'POST':
            tel = request.form['tel']
            new_member=Member.add_member_by_tel(tel)
            return jsonify(new_member)


@app.route('/jsonify')
def json_test():
    ret_dic={
        'return_code':200,
        'msg':'get member list success',
        'members':[{'id':'1','tel':'18812345678','disc':0.9,'active':1},
                   {'id':'2','tel':'18712345678','disc':0.8,'active':1},
                   {'id':'3','tel':'18612345671','disc':0.7,'active':1}]
    }
    return jsonify(ret_dic)
@app.route('/filter/score')
def filter_member_by_score():
    score = request.args['le']
    ret_dic = Member.filter_member_by_score(score)
    ret_dic['return_code'] = 200
    ret_dic['return_msg'] = 'Filter user success'
    return jsonify(ret_dic)

if __name__ == '__main__':
    app.run()

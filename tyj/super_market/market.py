# encoding:utf-8
from flask import Flask, request,jsonify
from tyj.super_market.model.members import get_members

app = Flask('__main__')

@app.route('/members', methods=['GET', 'POST'])
@app.route('/members/<condition>',methods=['GET','PUT','PATCH'])
def get_all_members(condition=None):
    if request.method == 'GET':
        if condition == None:
            get_all_member = get_members.all_member()
            get_all_member['return_code'] =200
            get_all_member['return_msg'] = '获取所有用户成功'
        else:
            if condition.startswith("tel_"):
                tel = condition.split("_")[-1]
                get_all_member = get_members.get_member_by_tel(tel)
                get_all_member['return_code'] =200
                get_all_member['return_msg'] = 'Get All Member by tel success'
            else:
                uid = condition.split('_')[-1]
                get_all_member = get_members.get_member_by_uid(uid)
                get_all_member['return_code'] =200
                get_all_member['return_msg'] = 'Get All Member by uid success'
        return jsonify(get_all_member)
    elif request.method =='POST':
        tel =request.form['tel']
        new_member = get_members.add_member(tel)
        return jsonify(new_member)
    elif request.method =='PUT':
        id =condition.split("_")[-1]
        tel = request.form['tel']
        disc = request.form['disc']
        active =request.form['active']
        user_info ={"tel":tel,"disc":disc,"active":active}
        ret_dic = get_members.update_member_info(id,user_info)
        if len(ret_dic.keys()) == 0:
            ret_dic['return_code'] = 404
            ret_dic['return_msg'] = 'Update user by user info failed'
        else:
            ret_dic['return_code'] = 200
            ret_dic['return_msg'] = 'Update user by user info success'
        return jsonify(ret_dic)
    elif request.method == 'PATCH':
        id = condition.split("_")[-1]
        score = request.form['score']
        ret_dic =get_members.update_member_score(id,score)
        ret_dic['return_code'] = 200
        ret_dic['return_msg'] = 'Update user score succes'
        return jsonify(ret_dic)
    elif request.method == 'DELETE':
        id=condition.split('_')[-1]
        ret_dic =get_members.inactive_member(id)
        ret_dic['return_code'] = 200
        ret_dic['return_msg'] = 'Inactive user succes'
        return jsonify(ret_dic)
    else:
        ret_dic = {'return_code':'200','return_msg':'啥也没干'}
        return jsonify(ret_dic)



@app.route('/filter/score')
def filter_member_by_score():
    score = request.args['le']
    ret_dic = get_members.filter_member_by_score(score)
    ret_dic['return_code'] = 200
    ret_dic['return_msg'] = 'Filter user succes'
    return jsonify(ret_dic)



@app.route("/jsontest")
def jsontest():
    ret_dic = {
        'return_code': '200',
        'msg':'get member list success',
        'members':[{'id': '1', 'tel': '13112345670', 'disc': 0.98},
                   {'id': '2', 'tel': '13112345671', 'disc': 0.9},
                   {'id': '3', 'tel': '13112345672', 'disc': 0.8},
                   {'id': '4', 'tel': '13112345673', 'disc': 0.8},
                   {'id': '5', 'tel': '13212345671', 'disc': 0.8}
                    ]
    }
    return jsonify(ret_dic)

if __name__ == '__main__':
        app.run()

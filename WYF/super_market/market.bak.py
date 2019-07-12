# __encoding:utf-8__

from flask import Flask, request,jsonify
from WYF.super_market.model.members.bak import Member

app = Flask('__main__')
@app.route('/jsontest')
def json_test():
    ret_dic={
        'return_code':200,
        'msg':'get member list success',
        'members':[
        {'id': 1, 'tel': '18812345671', 'discount': 0.98, 'state': 1, 'jifen': 1000},
        {'id': 2, 'tel': '18812345672', 'discount': 0.9, 'state': 1, 'jifen': 1500},
        {'id': 3, 'tel': '18812345673', 'discount': 0.8, 'state': 1, 'jifen': 2000},
        {'id': 4, 'tel': '18832145673', 'discount': 0.8, 'state': 1, 'jifen': 2000}
    ]
    }
    return jsonify(ret_dic)


# @app.route('/')
# def hello_word():
#     return 'hello work'
#
# @app.route('/xiaojiejie')
# @app.route('/xiaojiejie/<name>')
# def hello_xiaojiejie(name='xiaogege'):
#     return ('hello %s'%name)

@app.route('/member', methods=['GET', 'POST'])
@app.route('/member/<condition>',methods=['GET', 'PUT','PATCH','DELETE'])
@app.route('/filter/jifen')
def filter_member():
    jifen=request.args['le']
    ret_dic=Member.filter_member_by_jifen(jifen)
    ret_dic['return_code'] = 200
    ret_dic['return_msg'] = 'filter user success'
    return jsonify(ret_dic)

def get_members_all(condition=None):
    if request.method == 'GET':
        if condition == None:
            members_list = Member.get_all_members()
            members_list['return_code']=200
            members_list['return_msg']='Get member list success'
        else:
            if condition.startswith('tel_'):
                tel = condition.split('_')[-1]
                members_list = Member.get_member_last_four(tel)
                members_list['return_code'] = 200
                members_list['return_msg'] = 'Get member list success'
            else:
                uid = condition.split('_')[-1]
                print("uid = " + uid)
                members_list = Member.get_member_by_id(uid)
                members_list['return_code'] = 200
                members_list['return_msg'] = 'Get member list success'

        return jsonify(members_list)
    elif request.method == 'POST':
        tel = request.form['tel']
        new_member = Member.add_member(tel)
        return jsonify(new_member)
    elif request.method == 'PUT':
        uid = condition.split('_')[-1]
        tel = condition.split('_')[-1]
        discount = request.form['discount']
        state = request.form['state']
        user_info={'tel':tel,'discount':discount,'state':state}
        ret_dic=Member.update_member(uid,user_info)
        if len(ret_dic.keys())==0:
            ret_dic['return_code'] = 404
            ret_dic['return_msg'] = 'Update user failed'
        else:
            ret_dic['return_code'] = 200
            ret_dic['return_msg'] = 'Update user success'
        return jsonify(ret_dic)
    elif request.method == 'PATCH':
        uid = condition.split('_')[-1]
        jifen = request.form['jifen']
        ret_dic=Member.update_member_jifen(uid,jifen)
        ret_dic['return_code']=200
        ret_dic['return_msg'] = 'Update user success'
        return jsonify(ret_dic)
    elif request.method == 'DELETE':
        uid = condition.split('_')[-1]
        ret_dic = Member.delete_member(uid)
        ret_dic['return_code'] = 200
        ret_dic['return_msg'] = 'Update user success'
        return jsonify(ret_dic)

    else:
        ret_dic={'return_code':200,'return_msg':'什么都没做'}
        return jsonify(ret_dic)






if __name__ == '__main__':
    app.run()

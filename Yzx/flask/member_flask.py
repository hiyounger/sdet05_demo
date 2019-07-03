# encoding:utf-8
from flask import Flask, request, jsonify
from Yzx.flask.tools.logger import info,debug,error
from Yzx.flask.model.member import Mermbers


app = Flask('__mian__')


@app.route('/')
def hell():
    return 'hello'


@app.route('/json1')
def json_test():
    json_list = {
        'return_code': 200,
        'msg': "return member_list successful",
        'members': [
            {'id': '1', 'tel': '18845871680', 'disc': 0.9, 'state': 1, 'points': 0000},
            {'id': '2', 'tel': '18845095099', 'disc': 0.1, 'state': 1, 'points': 0000},
            {'id': '3', 'tel': '18845195099', 'disc': 0.1, 'state': 1, 'points': 0000}
        ]
    }
    return jsonify(json_list)


@app.route('/members', methods=['GET', 'POST'])
@app.route('/members/<condition>', methods=['GET', 'PUT','PATCH','DELETE'])
def get_all_members(condition=None):
    if request.method == "GET":
        if condition == None:
            get_all_members_list = Mermbers.get_members()
            # get_all_members_list['msg']='return members  successful'
        else:
            if condition.startswith( 'tel_'):
                tel = condition.split('_')[-1]
                print debug(tel)
                get_all_members_list = Mermbers.get_members_by_tel(tel)
                # get_all_members_list['msg'] = 'return members by tel successful'
            else:
                uid = condition.split('_')[-1]
                get_all_members_list = Mermbers.get_member_by_uid(uid)
                # get_all_members_list['msg'] = 'return members by uid successful'
        return jsonify(get_all_members_list)
    elif request.method == "POST":
        tel = request.form['tel']
        new_mem = Mermbers.add_member(str(tel))
        return jsonify(new_mem)
    elif request.method == "PUT":
        uid = condition.split('_')[-1]
        disc = request.form['disc']
        tel = request.form['tel']
        state = request.form['state']
        user_info = {'disc': disc, 'tel': tel, 'state': state}
        update_member = Mermbers.update_member_by_id(uid, user_info)
        if len(update_member) == 0:
            update_member['return_code'] = 404
            update_member['return_msg'] = "update member by id false"
        else:
            update_member['return_code'] = 202
            update_member['return_msg'] = "update member by id sucessful"
        return jsonify(update_member)
    elif request.method == "PATCH":
        uid = condition.split('_')[-1]
        points=request.form['points']
        return_dic_list=Mermbers.update_member_points(uid,points)
        return_dic_list['return_code'] = 200
        return_dic_list['return_msg'] = "update member by id sucessful"
        return jsonify(return_dic_list)
    elif request.method == "DELETE":
        uid = condition.split('_')[-1]
        return_dic_delete=Mermbers.delete_member_by_id(uid)
        return_dic_delete['return_code']=200
        return_dic_delete['return_msg']='delete member by id sucessful'
        return jsonify(return_dic_delete)
    else:
        return_dic = {'return_msg': '什么都没有做'}
        return jsonify(return_dic)

@app.route('/filter/score')
def find_score():
    score=request.args['le']
    print debug(score)
    return_find=Mermbers.find_socre_big(score)
    return_find['return_code'] = 200
    return_find['return_msg'] = 'find member  sucessful'
    return jsonify(return_find)

if __name__ == '__main__':
    app.run()

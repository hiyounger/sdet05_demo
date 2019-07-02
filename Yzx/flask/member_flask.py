# encoding:utf-8
from flask import Flask, request, jsonify
from Yzx.flask.model.member import Mermbers

app = Flask('__mian__')


@app.route('/')
def hell():
    return 'hello'


@app.route('/json1')
def json_test():
    json_list = {
        'return_code':200,
        'msg':"return member_list successful",
        'members': [
            {'id': '1', 'tel': '18845871680', 'disc': 0.9, 'state': 1, 'points': 0000},
            {'id': '2', 'tel': '18845095099', 'disc': 0.1, 'state': 1, 'points': 0000},
            {'id': '3', 'tel': '18845195099', 'disc': 0.1, 'state': 1, 'points': 0000}
        ]
    }
    return jsonify(json_list)


@app.route('/members', methods=['GET', 'POST'])
@app.route('/members/<condition>')
def get_all_members(condition=None):
    if request.method == "GET":
        if condition == None:
            get_all_members_list = Mermbers.get_members()
        else:
            if condition.startswith == 'tel_':
                tel = condition.split('_')[-1]
                get_all_members_list = Mermbers.get_members_by_tel(tel)
            else:
                uid = condition.split('_')[-1]
                get_all_members_list = Mermbers.get_member_by_uid(uid)
        return jsonify(get_all_members_list)
    else:
        tel = request.form['tel']
        new_mem = Mermbers.add_member(tel)
        return jsonify(new_mem)


# @app.route('/members')
# @app.route('/members/<tel>')
# def get_all_members(tel=None):
#     if tel==None:
#         get_all_members_list = Mermbers.get_members()
#     else:
#         get_all_members_list=Mermbers.get_members_by_tel(tel)
#     return str(get_all_members_list)


if __name__ == '__main__':
    app.run()

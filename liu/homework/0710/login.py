# encoding:utf-8
from flask import Flask, jsonify, request

app = Flask(__name__)

Member = {'uid':1,'username':'xiaoming',"password":'123456'}

@app.route('/')
def index():
    return 'Hellow Flask'

@app.route('/register',method=['POST'])
def member_add():
    username = request.form['name']
    member_list=[]
    for member in Member:
        if member['usernamer'] == username:
            member_list.append(member)
            ret_dic = {
                'member':member_list
            }
        else:
            ret_dic={
                "error_code" :401,
                "error_msg" : "用户已存在"
            }
    return jsonify(ret_dic)

@app.route('/getmember',method=['GET'])
def get_member_by_uid(uid):
    target_uid =request.args['uid']
    if id ==Member['uid']:





if __name__ == '__main__':
    app.run()

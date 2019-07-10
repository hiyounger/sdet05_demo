# encoding:utf-8
from flask import Flask, jsonify, request
from tyj.popsoting.stu0710 import Dict,db

app = Flask('__name__')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:111111@127.0.0.1:3306/supermarket"
db.init_app(app)

# 连接根目录
@app.route('/')
def index():
    return 'see u next class'
@app.route('/initdb', methods=['POST'])
def init_db():
    db.create_all()
    ret_dic = {
        'return_code': 200,
        'return_msg': 'Init db success'
    }
    return jsonify(ret_dic)

 # 添加会员
@app.route('/register',methods='[POST]')
def addmember():
    username = request.form['username']
    password = request.form['password']
    if username in Dict.username:
        ret_dic = {
            "error_code": 401, "error_msg": "用户已存在"
        }
        return jsonify(ret_dic)
    else:
        return






if __name__ == '__main__':
    app.run()
# -*- encoding:utf-8 -*-
from flask import Flask, jsonify, request
from tyj.super_market.model.member import db, Member
app = Flask(__name__)


# 配置数据库连接
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:111111@127.0.0.1:3306/supermarket"
db.init_app(app)


@app.route('/')
def index():
    return 'Hello Flask'


@app.route('/initdb', methods=['POST'])
def init_db():
    db.create_all()
    ret_dic = {
        'ret_code': '200',
        'ret_msg': 'Init db success'
    }
    return jsonify(ret_dic)


@app.route('/member', methods=['POST'])
def member_actions():
    # 1.处理创建
    if request.method == 'POST':
        tel = request.form['tel']
        mem_info = Member.add_member(tel)
        ret_dic = {"return_code": 200, "return_msg": "add member success",
                   "member": mem_info
                   }
        return ret_dic


if __name__ == '__main__':
    app.run()

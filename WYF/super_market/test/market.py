# coding:utf-8
from flask import Flask, jsonify, request
from WYF.super_market.model.member import db,Member


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@127.0.0.1:3306/supermarket"
db.init_app(app)



@app.route('/')
def index():
    return "<h1>Hello</h1>"


@app.route('/initdb', methods=['POST'])
def init_db():
    db.create_all()

    ret_dic = {"ret_code": "200", "ret_msg": "创建数据库成功"}
    return jsonify(ret_dic)


@app.route('/member',methods=['POST'])
def member_actions():
    # 1、处理创建
    if request.method=='POST':
        tel=request.form['tel']
        mem_info=Member.add_member(tel)

        ret_dic={
            "ret_code": "200",
            "ret_msg": "添加数据库成功",
            'member':mem_info
        }

        return jsonify(ret_dic)



if __name__ == '__main__':
    app.run(port=7000)

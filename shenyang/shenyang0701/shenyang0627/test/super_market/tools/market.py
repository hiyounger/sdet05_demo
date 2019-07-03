# coding:utf-8

from flask import Flask, jsonify, request
from model.member import db, Member

app = Flask(__name__)
# 配置数据库连接
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@192.168.8.52:3306/chenguanxi"
db.init_app(app)


@app.route('/')
def index():
    return "Hello Flask"


@app.route('/initdb', methods=['POST'])
def init_db():
    db.create_all()
    ret_dic = {
        "return_code":"200",
        "return_msg":"Init db success"
    }
    return jsonify(ret_dic)

@app.route('/member', methods=['POST'])
@app.route('/member/<condition>', methods=['GET', 'PATCH'])
def member_actions(condition=None):
    #1. 处理创建
    if request.method == 'POST':
        tel = request.form['tel']
        mem_info = Member.add_member(tel)

        ret_dic = {
            "return_code":200,
            "return_msg": "add member success",
            "member": mem_info
        }

        return jsonify(ret_dic)
    elif request.method == 'GET':
        if condition.startswith("tel_"):
            tel = condition.split("_")[-1]
            ret_dic = Member.search_by_tel(tel)
            ret_dic['return_code'] = 200
            ret_dic['return_msg'] = "Get Member by tel success"

            return jsonify(ret_dic)
    elif request.method == 'PATCH':
        uid = int(condition.split("_")[-1])
        score = int(request.form['score'])
        ret_dic = Member.update_member_score(uid, score)
        ret_dic['return_code'] = 200
        ret_dic["return_msg"] = "update score success"
        return jsonify(ret_dic)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

#encoding:utf-8
from flask import Flask,jsonify
from zhangjun_demo.super_maket.model.member import db


app = Flask (__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@127.0.0.1:3306/supermarket"
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



if __name__ == '__main__':
    app.run(port=8000)

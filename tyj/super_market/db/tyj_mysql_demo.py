# -*- encoding:utf-8 -*-

from flask import Flask, jsonify ,request
from flask_sqlalchemy import SQLAlchemy

# 1. 实例化一个Flask 对象
app = Flask(__name__)

# 2. 实例化一个flask_sqlalchemy对象， 用于操作数据库
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:111111@127.0.0.1:3306/supermarket"
db = SQLAlchemy(app)

# 3. 声明一个数据库中的表
class Student(db.Model):
    s_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_no = db.Column(db.String(10), unique=True)
    s_name = db.Column(db.String(16))
    s_age = db.Column(db.Integer, default=0)

    __tablename__ = "student"


@app.route('/initdb', methods=['POST'])
def init_db():
    db.create_all()
    db.session.commit()
    ret_dic = {"ret_code":"200", "ret_msg":"创建数据库成功"}
    return jsonify(ret_dic)

@app.route('/add_student',methods=['POST'])
def add_student():
    stu = Student()
    stu.s_no = request.form['s_no']
    stu.s_name = request.form['s_name']
    stu.s_age = request.form['s_age']

    db.session.add(stu)
    db.session.commit()

    ret_dic = {'ret_code':'200','ret_msg':'添加学生列表成功','student':{'s_id':stu.s_id,'s_no':stu.s_no,'s_name':stu.s_name,'s_age':stu.s_age}}
    return jsonify(ret_dic)


if __name__ == '__main__':
    app.run()






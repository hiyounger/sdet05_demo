# -*- encoding:utf-8 -*-

from flask import Flask, jsonify, request
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


# 创建一个数据库
@app.route('/initdb', methods=['POST'])
def init_db():
    db.create_all()
    db.session.commit()
    ret_dic = {"ret_code": "200", "ret_msg": "创建数据库成功"}
    return jsonify(ret_dic)


# 添加学生信息
@app.route('/add_student', methods=['POST'])
def add_student():
    stu = Student()
    stu.s_no = request.form['s_no']
    stu.s_name = request.form['s_name']
    stu.s_age = request.form['s_age']

    db.session.add(stu)
    db.session.commit()

    ret_dic = {'ret_code': '200', 'ret_msg': '添加学生列表成功',
               'student': {'s_id': stu.s_id, 's_no': stu.s_no, 's_name': stu.s_name, 's_age': stu.s_age}}
    return jsonify(ret_dic)


# 查询所有学生信息
@app.route('/all_students')
def get_all_students():
    db.query = Student.query.all()
    student_list = []
    for stu in db.query:
        student_info = {'s_id': stu.s_id, 's_no': stu.s_no, 's_name': stu.s_name, 's_age': stu.s_age}
        student_list.append(student_info)
        ret_dic = {
            'ret_code': '200',
            'ret_msg': '查询学生信息成功',
            'count': len(student_list),
            'student': student_list
        }
        return jsonify(ret_dic)


# 通过编号查询指定学生信息
@app.route('/search')
def search_student():
    # /search?no=001     (查询学生编号为001的学生信息)
    target_no = request.args['no']
    db_ret = Student.query.filter(Student.s_no == target_no)

    student_list = []
    for stu in db_ret:
        student_info = {'s_id': stu.s_id, 's_no': stu.s_no, 's_name': stu.s_name, 's_age': stu.s_age}
        student_list.append(student_info)
    ret_dic = {
        'ret_code': '200',
        'ret_msg': '查询学生信息成功',
        'count': len(student_list),
        'student': student_list
    }
    return jsonify(ret_dic)


# 修改学生信息
@app.route('/update', methods=['PUT'])
def update_student_info():
    stu_no = request.form['s_no']
    stu_name = request.form['s_name']
    stu_age = request.form['s_age']

    target_student = Student.query.filter(Student.s_no == stu_no)[0]
    target_student.s_no = stu_no
    target_student.s_name = stu_name
    target_student.s_age = stu_age
    db.session.commit()
    ret_dic = {
        'ret_code': '200',
        'ret_msg': '修改学生信息成功',
        's_no': target_student.s_no, 's_name': target_student.s_name, 's_age': target_student.s_age
    }
    return ret_dic

# 根据学号删除学生信息
@app.route('/delete', methods=['DELETE'])
def delete_student():
    stu_no = request.form['s_no']
    stu = Student.query.filter(Student.s_no == stu_no)[0]
    db.session.delete(stu)
    db.session.commit()
    ret_dic = {
        'ret_code': '200',
        'ret_msg': '删除学生信息成功',
        'student': {
            's_id': stu.s_id, 's_no': stu.s_no, 's_name': stu.s_name, 's_age': stu.s_age}
    }
    return jsonify(ret_dic)


if __name__ == '__main__':
    app.run()

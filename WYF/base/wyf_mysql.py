# coding:utf-8
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@127.0.0.1:3306/supermarket"
db = SQLAlchemy(app)


class Student(db.Model):
    s_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_num = db.Column(db.String(10), unique=True)
    s_name = db.Column(db.String(16))
    s_age = db.Column(db.Integer, default=0)

    __tablename__ = "student"


@app.route('/')
def index():
    return "<h1>Hello</h1>"


@app.route('/initdb', methods=['POST'])
def init_db():
    db.create_all()
    db.session.commit()
    ret_dic = {"ret_code": "200", "ret_msg": "创建数据库成功"}
    return jsonify(ret_dic)


@app.route('/add_student', methods=['POST'])
def add_student():
    stu = Student()
    stu.s_num = request.form['s_num']
    stu.s_name = request.form['s_name']
    stu.s_age = request.form['s_age']

    db.session.add(stu)
    db.session.commit()

    ret_dic = {'ret_code': '200', 'ret_msg': '添加信息成功',
               'student': {'s_id': stu.s_id, 's_num': stu.s_num, 's_name': stu.s_name, 's_age': stu.s_age}}
    return jsonify(ret_dic)


@app.route('/all_student')
def get_all_student():
    db_query = Student.query.all()
    student_list = []
    for stu in db_query:
        student_info = {'s_id': stu.s_id, 's_num': stu.s_num, 's_name': stu.s_name, 's_age': stu.s_age}
        student_list.append(student_info)

    ret_dic = {'ret_code': '200', 'ret_msg': '查询信息成功',
               'student': student_list, 'count': len(student_list)}
    return jsonify(ret_dic)


@app.route('/select')
def select_student():
    target = request.args['s_num']
    db_ret = Student.query.filter(Student.s_num == target)

    student_list = []
    for stu in db_ret:
        student_info = {'s_id': stu.s_id, 's_num': stu.s_num, 's_name': stu.s_name, 's_age': stu.s_age}
        student_list.append(student_info)

    ret_dic = {'ret_code': '200', 'ret_msg': '查询信息成功',
               'student': student_list, 'count': len(student_list)}
    return jsonify(ret_dic)


@app.route('/update', methods=['PUT'])
def update_student():
    stu_num = request.form['s_num']
    stu_name = request.form['s_name']
    stu_age = request.form['s_age']

    target_stu = Student.query.filter(Student.s_num == stu_num)[0]
    target_stu.s_num = stu_num
    target_stu.s_name = stu_name
    target_stu.s_age = stu_age

    s_list = [
        {'s_id': target_stu.s_id, 's_num': target_stu.s_num,
         's_name': target_stu.s_name, 's_age': target_stu.s_age}]

    ret_dic = {'ret_code': '200', 'ret_msg': '修改信息成功',
               'student': s_list,
               'count': len(s_list)}

    return jsonify(ret_dic)


@app.route('/delete', methods=['DELETE'])
def delete_student():
    stu_num = request.form['s_num']

    target_stu = Student.query.filter(Student.s_num == stu_num)[0]

    db.session.delete(target_stu)
    db.session.commit()

    s_list = [
        {'s_id': target_stu.s_id, 's_num': target_stu.s_num,
         's_name': target_stu.s_name, 's_age': target_stu.s_age}]

    ret_dic = {'ret_code': '200', 'ret_msg': '删除信息成功',
               'student': s_list,
               'count': len(s_list)}

    return jsonify(ret_dic)


if __name__ == '__main__':
    app.run(port=8000)

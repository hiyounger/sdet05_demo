# coding:utf-8

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@127.0.0.1:3306/market"
db = SQLAlchemy(app)


class student(db.Model):
    s_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_no = db.Column(db.String(10), unique=True)
    s_name = db.Column(db.String(16))
    s_age = db.Column(db.Integer, default=0)

    __tablename__ = "student"


@app.route('/initdb', methods=['POST'])
def init_db():
    db.create_all()
    db.session.commit()
    ret_dic = {"ret_code": "200", "ret_msg": "创建数据库成功"}
    return jsonify(ret_dic)


@app.route("/add_student", methods=["POST"])
def add_student():
    stu = student()
    stu.s_age = request.form["s_age"]
    stu.s_name = request.form["s_name"]
    stu.s_no = request.form["s_no"]
    db.session.add(stu)
    db.session.commit()
    ret_dic = {
        "ret_code": 200,
        "ret_msg": "新增学生成功",
        "s_id": stu.s_id,
        "s_name": stu.s_name,
        "s_no": stu.s_no,
        "s_age": stu.s_age
    }
    return jsonify(ret_dic)


@app.route("/search", methods=["GET"])
def select_student():
    target_no = request.args["no"]
    db_ret = student.query.filter(student.s_id == target_no)

    student_list = []
    for i in db_ret:
        student_info = {
            "s_id": i.s_id,
            "s_name": i.s_name,
            "s_no": i.s_no,
            "s_age": i.s_age
        }
        student_list.append(student_info)

    ret_dic = {
        "ret_code": 200,
        "ret_msg": "新增学生成功",
        "student": student_list,
        "count": len(student_list)
    }
    return jsonify(ret_dic)


@app.route("/all_student")
def select_all_student():
    db_query = student.query.all()
    student_list = []
    for stu in db_query:
        student_info = {
            "s_id": stu.s_id,
            "s_name": stu.s_name,
            "s_no": stu.s_no,
            "s_age": stu.s_age
        }
        student_list.append(student_info)

    ret_dic = {
        "ret_code": 200,
        "ret_msg": "查询所有学生成功",
        "student": student_list,
        "count": len(student_list)
    }
    return jsonify(ret_dic)


@app.route("/update", methods=["put"])
def update_student():
    stu_no = request.form["s_no"]
    stu_age = request.form["s_age"]
    stu_name = request.form["s_name"]

    target_student = student.query.filter(student.s_no == stu_no)[0]
    target_student.s_no = stu_no
    target_student.s_age = stu_age
    target_student.s_name = stu_name
    db.session.commit()

    ret_dic = {
        "ret_code": 200,
        "ret_msg": "更改学生信息成功",
        "student": {
            "s_id": target_student.s_id,
            "s_name": target_student.s_name,
            "s_no": target_student.s_no,
            "s_age": target_student.s_age}
    }
    return jsonify(ret_dic)


@app.route("/delete", methods=["DELETE"])
def delete_student():
    stu_no = request.form["s_no"]
    target_student = student.query.filter(student.s_no == stu_no)[0]
    db.session.delete(target_student)
    db.session.commit()

    ret_dic = {
        "ret_code": 200,
        "ret_msg": "删除学生信息成功",
        "student": {
            "s_id": target_student.s_id,
            "s_name": target_student.s_name,
            "s_no": target_student.s_no,
            "s_age": target_student.s_age}
    }
    return jsonify(ret_dic)


if __name__ == '__main__':
    app.run()

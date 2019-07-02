# -*- encoding:utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@127.0.0.1:3306/helloflask"

class Student(db.Model):
    s_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_name = db.Column(db.String(16), unique=True)
    s_age = db.Column(db.Integer, default=1)

    __tablename__ = "student"

@app.route("/createdb")
def create_db():
    db.create_all()
    return "CT database success"

@app.route('/add_student')
def add_student():
    s = Student()
    s.s_name = 'XM'
    s.s_age = 1

    db.session.add(s)
    db.session.commit()
    return "add student success"

@app.route('/get_all')
def get_all_student():
    students = Student.query.all()
    print(students)
    for stu in students:
        print stu.s_name
    return str(students[0])

@app.route('/get_by_id/<uid>')
def get_by_id(uid):
    students = Student.query.filter_by(s_id=uid)
    print(students)
    for stu in students:
        print stu.s_name
    return str(students)

@app.route('/update_by_id/<uid>')
def update_by_id(uid):
    student = Student.query.filter_by(s_id=uid).first()
    student.s_name = 'XH'
    db.session.commit()
    return str(student)

@app.route('/delete_by_id/<uid>')
def delete_by_id(uid):
    student = Student.query.filter_by(s_id=uid).first()
    db.session.delete(student)
    db.session.commit()
    return str(student)




@app.route("/dropdb")
def drop_db():
    db.drop_all()
    return "DP database success"

if __name__ == '__main__':
    app.run()




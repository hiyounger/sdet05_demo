#encoding:utf-8

from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy


#实例化一个Flask对象
app=Flask(__name__)

#实例化一个flask_sqlalchemy对象，用于操作数据库
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] ="mysql+pymysql://root:root@192.168.8.52:3306/pengyunhao"
db=SQLAlchemy(app)

#声明一个数据库中的表
class Student(db.Model):
    s_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    s_no=db.Column(db.String(10),unique=True)
    s_name=db.Column(db.String(16))
    s_age = db.Column(db.Integer, default=0)

    __tablename__="student"

@app.route("/initdb",methods=["POST"])
def initdb():
    db.create_all()
    db.session.commit()
    returnDict={"msg":"create table success"}
    return jsonify(returnDict)

@app.route("/add",methods=["POST"])
def addStudent():
    stu=Student()
    stu.s_no=request.form["s_no"]
    stu.s_name=request.form["s_name"]
    stu.s_age=request.form["s_age"]
    db.session.add(stu)
    db.session.commit()
    returnDict={"msg":"add success","student":{"s_id":stu.s_id,"s_no":stu.s_no,"s_name":stu.s_name,"s_age":stu.s_age}}
    return jsonify(returnDict)

@app.route("/query")
def queryStudeng():
    request_no=request.args["s_no"]
    #查询是否符合过滤条件
    dbrequest=Student.query.filter(Student.s_no==request_no)
    studentList=[]
    for stu in dbrequest:
        student={"s_id":stu.s_id,"s_no":stu.s_no,"s_name":stu.s_name,"s_age":stu.s_age}
        studentList.append(student)
    returnDict={
            "msg":"query success",
            "count":len(studentList),
            "student":studentList
        }
    return jsonify(returnDict)

@app.route("/queryall")
def quetyAll():
    dbrequest=Student.query.all()
    studentList=[]
    for stu in dbrequest:
        student={"s_id":stu.s_id,"s_no":stu.s_no,"s_name":stu.s_name,"s_age":stu.s_age}
        studentList.append(student)
    returnDict={
        "msg": "query success",
        "count": len(studentList),
        "student": studentList
    }
    return jsonify(returnDict)

@app.route("/update",methods=["PUT"])
def updateStudentByNo():
    s_no=request.form["s_no"]
    s_name=request.form["s_name"]
    s_age=request.form["s_age"]

    requestStudent=Student.query.filter(Student.s_no==s_no).first()
    requestStudent.s_no=s_no
    requestStudent.s_name=s_name
    requestStudent.s_age=s_age
    db.session.commit()

    return "update success"

@app.route("/delete",methods=["DELETE"])
def deleteByNo():
    s_no=request.form["s_no"]
    stu = Student.query.filter(Student.s_no == s_no).first()
    db.session.delete(stu)
    db.session.commit()

    returnDict={
        "msg":"delete success",
        "student":{"s_id":stu.s_id,"s_no":stu.s_no,"s_name":stu.s_name,"s_age":stu.s_age}
        }
    return jsonify(returnDict)


if __name__=="__main__":
    app.run(port=8000)
#encoding:utf-8

from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from model.members import db,Member

#实例化一个Flask对象
app=Flask(__name__)


#实例化一个flask_sqlalchemy对象，用于操作数据库
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] ="mysql+pymysql://root:root@127.0.0.1:3306/pyh"
db.init_app(app)

@app.route("/")
def index():
    return "hello flask"

@app.route("/initdb",methods=["POST"])
def initdb():
    db.create_all()
    return "success initdb"

@app.route("/member",methods=["POST","GET"])
@app.route("/member/<condition>",methods=["GET","PATCH"])
def memberMethons(condition=None):
    if condition==None and request.method=="GET":
        returnDict=Member.queryAll()
        return jsonify(returnDict)
    elif request.method=="POST":
        tel=request.form["tel"]
        newMenber=Member.addMember(tel)
        returnDict={
            "return_code": 200,
            "return_msg": "add member success",
            "member": newMenber
        }
        return jsonify(returnDict)
    elif request.method=="GET":
        if condition.startswith("tel_"):
            tel=condition.split("_")[-1]
            returnDict=Member.queryBytel(tel)
            returnDict["return_code"]=200
            returnDict['return_msg'] = "Get Member by tel success"
            return jsonify(returnDict)
    elif request.method=="PATCH":
        uid=int(condition.split("_"-1))
        score=int(request.form["score"])
        returnDict=Member.updateScore(uid,score)
        returnDict['return_code'] = 200
        returnDict["return_msg"] = "update score success"
        return jsonify(returnDict)
if __name__=="__main__":
    app.run(host="0.0.0.0",port=80,debug=True)

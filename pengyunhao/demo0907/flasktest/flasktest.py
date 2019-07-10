#encoding:utf-8

from flask import Flask,jsonify,request
from pengyunhao.demo0907.flasktest.user import user
app=Flask(__name__)

@app.route("/register",methods=["Post"])
def adduser():
    if request.method=="POST":
        username=str(request.form["username"])
        password=request.form["password"]
        returnData=user.addUser(username,password)
        return jsonify(returnData)
@app.route("/getmember",methods=["GET"])
def getMember():
    if request.method=="GET":
        uid=int(request.form["uid"])
        returnData=user.allUser(uid)
        return jsonify(returnData)

if __name__ == '__main__':
    app.run()

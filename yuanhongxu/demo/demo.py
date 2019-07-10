#-*- encoding:utf-8 -*-

from flask import Flask, request, jsonify

app = Flask("__main__")
member=[
    {"uid":1,"username":"xiaoming", "password":"123456"}
]



@app.route("/")
def sayhello():
    return ("hello")

@app.route("/register",methods=["POST"])
def add():
    username=request.form["username"]
    password=request.form["password"]
    for mem in member:
        if mem["username"]==username:
            ret_dic={"error_code": 401, "error_msg": "用户已存在"}
            return jsonify(ret_dic)

    new_member={"uid":len(member)+1,"username":username, "password":password}
    member.append(new_member)

    ret_dic={"username":username, "password":password}
    ret_dic["uid"]=len(member)
    return jsonify(ret_dic)








if __name__ == '__main__':
    app.run()
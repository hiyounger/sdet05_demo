# -*- encoding:utf-8 -*-

from flask import Flask,request
from yuanhongxu.super_market.model.members import member

app = Flask("__main__")


@app.route("/")
def sayhello():
    return "hello flask"


# @app.route("/hello")
# @app.route("/hello/<name>")
# def sayhello2(name="worle"):
#     return ("hello %s"%name)

@app.route("/member",methods=["GET","POST"])
@app.route("/member/<condition>")
def get_all_members(condition=None):
    if request.method=="GET":
        if condition == None:
            all_member_list = str(member.get_all_member())
        else:
            if condition.startswith("tel_"):
                tel = condition.split("_")[-1]
                all_member_list = str(member.get_member_by_tel(tel))
            else:
                uid = condition.split("_")[-1]
                all_member_list = str(member.get_member_by_uid(uid))
        return all_member_list
    else:
        tel=request.form["tel"]
        new_member=member.add_member(tel)
        return str(new_member)


if __name__ == "__main__":
    app.run()

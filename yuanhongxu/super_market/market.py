# -*- encoding:utf-8 -*-

from flask import Flask
from yuanhongxu.super_market.model.members import members

app = Flask("__main__")


@app.route("/")
def sayhello():
    return "hello flask"


# @app.route("/hello")
# @app.route("/hello/<name>")
# def sayhello2(name="worle"):
#     return ("hello %s"%name)

@app.route("/member")
def get_all_members():
    all_member_list = str(members.get_all_member())
    return all_member_list


if __name__ == "__main__":
    app.run()

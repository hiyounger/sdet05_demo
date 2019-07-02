# -*- encoding:utf-8 -*-

from flask import Flask, request, jsonify
from yuanhongxu.super_market.model.members import member

app = Flask("__main__")


@app.route("/")
def sayhello():
    return "hello flask"


@app.route("/jsontest")
def jsontest():
    ret_dic = {
        "return_code": 200,
        "msg": "successful",
        "members": [{'discount': 0.95, 'tel': '18812345672', 'id': '1'},
                    {'discount': 0.9, 'tel': '18812345673', 'id': '2'},
                    {'discount': 0.9, 'tel': '18812345674', 'id': '3'},
                    {'discount': 0.8, 'tel': '18812345671', 'id': '4'},
                    {'discount': 0.8, 'tel': '18811345671', 'id': '5'}]
    }
    return jsonify(ret_dic)


@app.route("/member", methods=["GET", "POST"])
@app.route("/member/<condition>", methods=["GET", "PUT", "PATCH", "DELETE"])
def get_all_members(condition=None):
    if request.method == "GET":
        if condition == None:
            all_member_list = member.get_all_member()
            all_member_list["return_code"] = 200
            all_member_list["msg"] = "Get All Member Successful"
        else:
            if condition.startswith("tel_"):
                tel = condition.split("_")[-1]
                all_member_list = member.get_member_by_tel(tel)
                all_member_list["return_code"] = 200
                all_member_list["msg"] = "Get Member By Tel Successful"
            else:
                uid = condition.split("_")[-1]
                all_member_list = member.get_member_by_uid(uid)
                all_member_list["return_code"] = 200
                all_member_list["msg"] = "Get Member By Uid Successful"
        return jsonify(all_member_list)
    elif request.method == "POST":
        tel = request.form["tel"]
        new_member = member.add_member(tel)
        return jsonify(new_member)
    elif request.method == "PUT":
        uid = condition.split("_")[-1]
        tel = request.form["tel"]
        disc = request.form["disc"]
        status = request.form["status"]
        new_user_info = {"tel": tel, "disc": disc, "status": status}
        ret_dic = member.update_member(uid, new_user_info)
        if len(ret_dic.keys()) == 0:
            ret_dic["return_code"] = 404
            ret_dic["msg"] = "Update Member Failed"
        else:
            ret_dic["return_code"] = 200
            ret_dic["msg"] = "Update Member Successful"
        return jsonify(ret_dic)
    elif request.method == "PATCH":
        uid = condition.split("_")[-1]
        jifen = request.form["jifen"]
        ret_dic = member.update_member_jifen(uid, jifen)
        ret_dic["return_code"] = 200
        ret_dic["msg"] = "Inactive Member Successful"
        return jsonify(ret_dic)
    elif request.method == "DELETE":
        uid = condition.split("_")[-1]
        ret_dic = member.inactive_member(uid)
        ret_dic["return_code"] = 200
        ret_dic["msg"] = "Inactive Member Successful"
        return jsonify(ret_dic)
    else:
        ret_dic = {"return_code": 200, "msg": "什么也没做"}
        return jsonify(ret_dic)


@app.route("/filter/jifen")
def filter_member_by_jifen():
    jifen = request.args["le"]
    ret_dic = member.filter_member_by_score(jifen)
    ret_dic["return_code"] = 200
    ret_dic["msg"] = "Filter Member Successful"
    return jsonify(ret_dic)


if __name__ == "__main__":
    app.run()

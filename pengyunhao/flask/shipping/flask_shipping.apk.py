# encoding:utf-8

from flask import Flask, request, jsonify

from pengyunhao.flask.shipping.model.members import Member
from pengyunhao.flask.shipping.db import mysql

app = Flask("__main__")


@app.route("/")
def QQ():
    return "QQ"


@app.route("/music")
@app.route("/music/<name>")
def QQmusic(name="sss"):
    return "QQmusic %s" % name


@app.route("/member")
@app.route("/member/tel")
def getAllMember(tel=None):
    if tel == None:
        memberList = Member.getAllMember()
    else:
        memberList = Member.getMemberByTel(tel)
    return jsonify(memberList)


@app.route("/member", methods=["GET", "POST","PUT","PATCH","DELETE"])
@app.route("/member/<condition>", methods=["GET", "PUT","PATCH","DELETE"])
def UpdateMember(condition=None):
    if request.method == "GET":
        if condition == None:
            memberList = Member.getAllMember()
        else:
            if condition.startswith("tel_"):
                tel = condition.split("_")[-1]
                memberList = Member.getMemberByTel(tel)
            else:
                id = condition.split("_")[-1]
                memberList = Member.getMemberByid(id)
        return jsonify(memberList)
    elif request.method == "POST":
        tel = request.form["tel"]
        print "----------------------"
        newMember = Member.AddMember(tel)
        return jsonify(newMember)
    elif request.method == "PUT":
        id = condition.split("_")[-1]
        #可以使用
        #id = request.form["id"]
        print ("id--->",id)
        tel = request.form["tel"]
        discount = request.form["discount"]
        score = request.form["score"]
        active = request.form["active"]
        newMember = {"tel": tel, "discount": discount, "score": score, "active": active}
        updateMember = Member.updateMemberByID(id, newMember)
        if len(updateMember.keys()) == 0:
            updateMember["msg"] = "not have this ID"
            return jsonify(updateMember)
        else:
            updateMember["msg"] = "success"
            return jsonify(updateMember)
    elif request.method=="PATCH":
        id=condition.split("_")[-1]
        score=request.form["score"]
        updateScoreMember=Member.updateScore(id,score)
        return jsonify(updateScoreMember)
    elif request.method=="DELETE":
        id=condition.split("_")[-1]
        updateActiveMember=Member.updateActive(id)
        return jsonify(updateActiveMember)

    else:
        updateMember = {"msg": "failed"}
        return jsonify(updateMember)


@app.route("/jsonMember")
def jsonMember():
    dictMember = {
        "returnCode": "200",
        "msg": "success",
        "member": [{"id": "1", "tel": "12346789", "discount": 0.9},
                   {"id": "2", "tel": "54354544", "discount": 0.9},
                   {"id": "3", "tel": "54544544", "discount": 0.9},
                   ]}
    return jsonify(dictMember)


if __name__ == "__main__":
    app.run()

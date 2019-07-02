#encoding:utf-8

from flask import Flask,request

from pengyunhao.flask.shipping.model.members import Member

app=Flask("__main__")

@app.route("/")
def QQ():
    return "QQ"

@app.route("/music")
@app.route("/music/<name>")
def QQmusic(name="sss"):
    return "QQmusic %s"%name

@app.route("/member")
@app.route("/member/tel")
def getAllMember(tel=None):
    if tel==None:
        memberList=str(Member.getAllMember())
    else:
        memberList=str(Member.getMemberByTel(tel))
    return memberList

@app.route("/member",methods=["GET","POST"])
@app.route("/member/<condition>")
def UpdateMember(condition=None):
    if request.method == "GET":
        if condition==None:
            memberList=str(Member.getAllMember())
        else:
            if condition.startswith("tel_"):
                tel=condition.split("_")[-1]
                memberList=str(Member.getMemberByTel(tel))
            else:
                uid=condition.split("_")[-1]
                memberList=str(Member.getMemberByUid(uid))
        return memberList
    else:
        tel=request.form["tel"]
        print "----------------------"
        newMember=Member.AddMember(tel)
        return str(newMember)


if __name__=="__main__":
    app.run()
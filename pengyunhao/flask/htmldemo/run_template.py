#encoding:utf-8

from flask import Flask,render_template,request,jsonify

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login",methods=["POST"])
def login_api():
    _username=request.form["username"]
    _password=request.form["password"]
    returnData={
        "code":200,
        "msg":"login success"
    }
    return jsonify(returnData)

if __name__=="__main__":
    app.run()

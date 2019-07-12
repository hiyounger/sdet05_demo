#-*- encoding:utf-8 -*-

from flask import Flask,render_template,request,jsonify

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index1.html")

@app.route("/login", methods=["POST"])
def login_api():
    __username = request.form["username"]
    __password = request.form["password"]
    ret_dic={
        "return_code":200,
        "return_msg": "login api successful"
    }
    return jsonify(ret_dic)



if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080)
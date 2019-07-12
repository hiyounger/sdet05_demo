#encoding:utf-8
from flask import Flask,render_template,request,jsonify

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/login',methods=['POST'])
def login_in():
    username=request.form['username']
    password=request.form['password']
    ret_dic={'return_code':200,'return_msg':"登录成功"}
    return jsonify(ret_dic)


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80)
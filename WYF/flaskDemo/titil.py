#coding:utf-8
from flask import Flask,render_template,request,jsonify

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Login',methods=['POST'])
def login_api():
    _username=request.form['username']
    _password = request.form['password']
    ret_dic={'ret_code':200,'ret_msg':'Login success'}
    return jsonify(ret_dic)

if __name__ == '__main__':
    app.run( port=8080)

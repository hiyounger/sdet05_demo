#enconding:utf-8
from flask import Flask,render_template,request,jsonify
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/login',methods=['POST'])
def login_api():
    __username=request.form['username']
    __password = request.form['password']
    ret_dic={
        "ret_code":200,
        "ret_msg":"login successed"
    }
    return jsonify(ret_dic)


if __name__=='__main__':
    app.run(host='127.0.0.1',port='5005')
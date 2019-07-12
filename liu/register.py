# encoding:utf-8
from flask import Flask,render_template ,request ,jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hello.html')

@app.route('/login',methods = ['POST'])
def login_api():
    __username = request.form['username']
    __username = request.form['username']
    ret_dic = {'return_code':200,"return_msg":"Login Success"}
    return jsonify(ret_dic)

if __name__ == '__main__':
    app.run(host="127.0.0.1",port=8080)

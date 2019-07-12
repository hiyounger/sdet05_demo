# encoding:utf-8
from flask import Flask, request,jsonify
from WYF.class_f.class_bak import db,Student

app = Flask('__main__')
db.init_app(app)
@app.route('/')
def hello_word():
     return 'hello work'
# 新增用户
@app.route('/register',methods=['POST'])
def add_student():
    if request.method == 'POST':
        username = request.form['username']
        stu_info = Student.add_student(username)
        ret_dic = {
            "return_code": 200, "return_msg": "add member success",
            "member": stu_info
        }
        if len(ret_dic)==0:
            ret_dic={"error_code": 401,
                 "error_msg": "用户已存在"
                 }
        return jsonify(ret_dic)

@app.route('/getmember<condition>' , methods=['GET'])
def get_student(condition=None):
    if request.method=='GET':
        if condition.startwith('username_'):
            username = condition.split('_')[-1]
            ret_dic = Student.get_student_by_uid(username)
            return jsonify(ret_dic)
        else:
            ret_dic = Student.get_student_by_uid('uid')
            if len(ret_dic) == 0:
                ret_dic['error_code'] = 405
                ret_dic['error_msg'] = '用户不存在'
            return jsonify(ret_dic)






if __name__ == '__main__':
    app.run()
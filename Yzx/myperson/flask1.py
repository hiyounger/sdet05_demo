# encoding:utf-8
# Falsk API阶段知识测试：
# Lv1. 建立一个flask服务py文件，注册一个录用，/register，post方法，传入用户名，密码可以注册，返
# 回注册成功的用户 json数据 {uid:1, "username":"xiaoming", "password":"123456"},
# 注册是否，返回{"error_code": 401, "error_msg": "用户已存在"}
# 数据源： 使用 dict
# Lv1.  /getmember?uid=1, GET 请求，其中uid为参数，存在返回指定uid的用户{uid:1, "username":"xiaoming", "password":"123456"}, 不存在返回{"error_code": 405, "error_msg": "用户不存在"}
# Lv2. 使用POSTMAN对该请求进行测试，要求使用runner运行，配置environment， 写test。
#       验证至少4条用例，注册成功、不成功， 获取成功、不成功
# Lv2. 验证每一个key的值，以及状态码
# Lv3. 使用python + requests + ddt对Lv1开发的API 开发自动化测试用例， 写unittest testcase。
#       验证至少4条用例，注册成功、不成功， 获取成功、不成功
from flask import Flask,request,jsonify
from Yzx.myperson.model.member_model import db ,Member
from Yzx.myperson import config
app=Flask('__main__')
# 配置数据库连接
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://%s:%s@%s:%s/%s" % (
    config.DB_USERNAME, config.DB_PASSWORD, config.DB_HOST, config.DB_PORT, config.DB_NAME)
db.init_app(app)
@app.route('/initdb', methods=['POST'])
def init_db():
    db.create_all()
    ret_dic = {
        'return_code': 200,
        'return_msg': 'Init db success'
    }
    return jsonify(ret_dic)

@app.route('/')
def app_first():
    return ('hello Flask')

@app.route('/register',methods=['POST'])
def add_member():
    username=request.form['username']
    password=request.form['password']

    ret_dic=Member.add_members_by(username,password)
    print ret_dic['member'][0]['username']
    if len(ret_dic['member'][0]['username'])==0:
        ret_dic['return_code'] = 401
        ret_dic['return_msg'] = '注册用户失败'
    else:
        ret_dic['return_code']=200
        ret_dic['return_msg']='注册用户成功'
    return jsonify(ret_dic)






if __name__ == '__main__':
    app.run(config.APP_HOST,config.APP_PORT)
#encoding:utf-8
from flask import Flask,jsonify,request
from Yzx.makert.model.member import db,Member
app=Flask(__name__)
#配置数据库连接
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@127.0.0.1:3306/supermarket"
db.init_app(app)
@app.route('/')
def index():
    return 'Hellow Flask'
@app.route('/initdb',methods=['POST'])
def init_db():
    db.create_all()
    ret_dic={
        'return_code':200,
        'return_msg':'Init db success'
    }
    return jsonify(ret_dic)
# 注册一个用户
@app.route('/members',methods=['POST'])
@app.route('/members/<condition>',methods=['GET','PATCH'])
def add_member_byTel(condition=None):
    if request.method=='POST':
        tel=request.form['tel']
        mem_info=Member.add_member(tel)

        ret_dic={
            'return_code':200,
            'return_msg':'add member success',
            'member':mem_info
        }
        return jsonify(ret_dic)
    elif request.method=='GET':
        pass

#查询用户根据手机号码

## 获取积分大于指定值的会员列表
@app.route('/filter/score')
def get_members_byscore():
    score = int(request.args['le'])
    ret_dic = Member.get_members_list_byScore(score)
    ret_dic['return_code'] = 200
    ret_dic['return_msg'] = "Filter user success"
    return jsonify(ret_dic)
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)

@app.route('/filter/score')
def get_members_byScore():
    score=request.args['le']
    ret_dict=Member.get_member_byScore(score)
    ret_dict['return_code']=200
    ret_dict['return_msg']="Filter user success"
    print (ret_dict)
    return jsonify(ret_dict)
#encoding:utf-8
from flask import Flask,jsonify,request
from ddt import ddt,file_data

app = Flask(__name__)


# @app.route('/')
# def zhuye():
#     return "helloPython"
#
#
# dict={
#     {'uid':1,'username':'zhangsan','password':'zs1234'},
#     {'uid': 2, 'username': 'lisi', 'password': 'ls1234'}
# }
# app.route('/register',methods=['POST'])
# def register():
#     member_list=[]
#     ret_username=request.form('username')
#     ret_password=request.form('password')
#     dic_ret=dict.query.filter(dict.username==ret_username)
#
#     ret_dic={
#         'ret_code':'200'
#         'ret_msg':'reister success'
#         list
#
#     }
#     app.route('/search/')
#
#     def search_member():
#         # /search?uid=1
#         target_uid = request.args['uid']
#         dict_ret = dict.query.filter(dict.uid == target_uid)
#         mem_list = []
#         for mem in dict_ret:
#             mem_info = {'uid': mem.uid, 'username': mem.username,'password': mem.password}
#             mem_list.append(mem_info)
#         ret_dic = {'ret_code': '200',
#                    'ret_msg': 'search mem_info success',
#                    'count': len(mem_list),
#                    'member':mem_list
#
#                    }
#         return jsonify(ret_dic)


if __name__ == '__main__':
    app.run(port=8000)
#encoding:utf-8
from flask import Flask, request,jsonify
from liu.supermarket.model.members import Member,db

app = Flask(__name__)
#配置数据连接
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@127.0.0.1:3306/MARKET"
db.init_app(app)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/initedb'.methods= ['POST'])



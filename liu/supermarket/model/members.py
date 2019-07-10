# encoding:utf-8
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy

class Member(db.Model):

    uid = db.Column(db.INTEGER,primary_key=True,autoincrement=True)
    tel = db.Column(db.String(11), unique=True, nullable=True)
    discount = db.Column(db.FLOAT, nullable=True, default=1)
    score = db.Column(db.INTEGER, nullable=True,default=0)
    active = db.Column(db.INTEGER,nullable=True,default=1)

    __tablename__='members'

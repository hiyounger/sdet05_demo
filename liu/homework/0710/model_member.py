# encoding:utf-8
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Member(db.model)
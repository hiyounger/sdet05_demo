# -*- encoding:utf-8 -*-

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy


class Memeber(db.Model):
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tel = db.Column(db.String(11), unique=True, nullable=False)
    disc = db.Column(db.FLOAT, nullable=False, default=1)
    score = db.Column(db.Integer, nullable=False, default=0)
    active = db.Column(db.Boolean, nullable=False, default=True)

    __tablename__ = 'members'

    @classmethod
    def add_member(cls,tel):
        mem = Memeber()
        mem.tel = tel
        db.session.add(mem)
        db.session.commit()

        return {'test':'success'}

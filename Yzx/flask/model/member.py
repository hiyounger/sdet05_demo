# encoding:utf-8
from Yzx.flask.db import mysql


class Mermbers():
    @classmethod
    def get_members(cls):
        return mysql.members

# encoding:utf-8
from flask import Flask
from Yzx.flask.model.member import Mermbers

app = Flask('__mian__')


@app.route('/')
def hell():
    return 'hello'


@app.route('/members')
def get_all_members():
    get_all_members_list = Mermbers.get_members()
    return str(get_all_members_list)


if __name__ == '__main__':
    app.run()

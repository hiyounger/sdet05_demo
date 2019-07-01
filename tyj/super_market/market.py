# encoding:utf-8
from flask import Flask
from tyj.super_market.model.members import get_members

app = Flask('__main__')


# @app.route('/')
# def hello_word():
#     return "Hello Word"

# @app.route('/test')
# def hello_word2():
#     return "Never Give Up"
#
# @app.route('/hello')
# @app.route('/hello/<name>')
# def hello_word(name='World'):
#     return 'Hello %s' % name
#
@app.route('/members',methods=['GET','POST'])
@app.route('/members/<condition>')
def get_all_members(condition=None):
    if request.method == 'GET':
        if condition == None:
            get_all_member = str(get_members.all_member())
        else:
            if condition.startswith("tel_"):
                tel = condition.split("_")[-1]
                get_all_member = str(get_members.get_member_by_tel(tel))
            else:
                uid = condition.split('_')[-1]
                get_all_member = str(get_members.get_member_by_uid(uid))
        return get_all_member
    else:
        tel = request.form['tel']
        new_member = get_members.add_members(tel)
        return str(new_member)


if __name__ == '__main__':
    app.run()

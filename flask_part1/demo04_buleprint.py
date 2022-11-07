# coding: utf8
""" 
@File: demo04_buleprint.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/7 0:11
"""

from flask import Flask, Blueprint
from news import news_bp
from news import views

app = Flask(import_name=__name__)
bp = Blueprint(name='bp', import_name=__name__)

@app.route('/')
def index():
    return 'Hello World!'

@bp.route('/bp')
def user_info():
    return 'user info'

app.register_blueprint(blueprint=bp)
app.register_blueprint(blueprint=news_bp)
if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)



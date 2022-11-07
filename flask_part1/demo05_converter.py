# coding: utf8
""" 
@File: demo05_converter.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/7 1:00
"""

from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)

# 自定义转化器
class IphoneNumber(BaseConverter):
    regex = r'^1[3-9]\d{9}'
    
app.url_map.converters['iphone_number'] = IphoneNumber

@app.route('/user/<int:user_id>')
def index(user_id):
    return user_id

@app.route('/iphone/<iphone_number:i_id>')
def get_iphone_number(i_id):
    return i_id


if __name__ == '__main__':
    app.run(debug=True)


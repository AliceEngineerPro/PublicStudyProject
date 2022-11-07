# coding: utf8
""" 
@File: demo10_add_routes.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/7 13:42
"""

from flask import Flask

app = Flask(import_name=__name__)

def index():
    return 'Hello World'


app.add_url_rule('/', 'index', index)

if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)


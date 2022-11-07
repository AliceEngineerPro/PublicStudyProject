# coding: utf8
""" 
@File: demo11_set_response.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/7 18:48
"""

from flask import Flask

app = Flask(import_name=__name__)

@app.route('/')
def index():
    return 'Hello World!', 200, {"Server": "Python3.9.13"}


if __name__ == '__main__':
    app.run(debug=True)


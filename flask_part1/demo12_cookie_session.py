# coding: utf8
""" 
@File: demo12_cookie_session.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/7 18:54
"""

from flask import Flask, make_response, request

app = Flask(import_name=__name__)

@app.route('/')
def index():
    return 'Hello World'


if __name__ == '__main__':
    app.run(debug=True)
    


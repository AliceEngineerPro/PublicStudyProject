# coding: utf8
""" 
@File: demo08_redirect.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/7 13:20
"""

from flask import Flask, redirect

app = Flask(import_name=__name__)

@app.route('/')
def index():
    return redirect(location='https://baidu.com')


if __name__ == '__main__':
    app.run()

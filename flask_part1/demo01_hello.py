# coding: utf8
""" 
@File: demo01_hello.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/6 20:34
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return 'Hello World'

if __name__ == '__main__':
    app.run()



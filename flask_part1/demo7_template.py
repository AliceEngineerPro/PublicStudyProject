# coding: utf8
""" 
@File: demo7_template.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/7 13:09
"""

from flask import Flask, render_template

app = Flask(import_name=__name__)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()


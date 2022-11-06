# coding: utf8
""" 
@File: demo3_project.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/6 22:47
"""

from flask import Flask
from set_config import DefaultConfig, ProjectConfig


def init_app(config_name):
    init = Flask(__name__)
    init.config.from_object(config_name)
    return init


app = init_app(DefaultConfig)

@app.route('/', methods=['GET'])
def index():
    return app.config.get('_NAME_SPACES')


if __name__ == '__main__':
    # debug模块可以跟踪代码的变化
    print(app.url_map)
    app.run(debug=True, port=52015)

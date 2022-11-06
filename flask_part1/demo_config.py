# coding: utf8
""" 
@File: demo_config.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/6 21:44
"""

"""
配置文件加载
1. 配置对象 -> 字典
2. 配置文件 -> 字典
3. 环境变量
"""

from flask import Flask

# 配置对象
class DefaultFlaskConfig(object):
    MYSQL_HOST = 'obj host'

app = Flask(__name__)
# 从配置对象中获取配置信息
# app.config.from_object(DefaultFlaskConfig)
# 从配置文件中获取配置信息
# app.config.from_pyfile('settings.py')
app.config.from_pyfile('settings.ini')
# 从环境变量中获取配置信息
# app.config.from_envvar('FLASK_OBJ_CONFIG', silent=True)

@app.route('/')
def index():
    return app.config.get('MYSQL_HOST')


if __name__ == '__main__':
    app.run()


# coding: utf8
""" 
@File: demo06_request.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/7 3:54
"""

from flask import Flask, request

app: Flask = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # url传参
    user_id = request.args.get('user_id')
    print(user_id)
    # 表单数据
    user = request.form.get('user')
    pwd = request.form.get('pwd')
    print(user, pwd)
    # 请求信息
    print(request.method)
    print(request.url)
    print(request.headers)
    return 'Hello World!'

    
# 获取文件
@app.route('/files', methods=['POST'])
def save_files():
    file = request.files.get('files')
    print(file)
    file.save('./images.jpg')
    return 'save success'


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)


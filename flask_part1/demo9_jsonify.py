# coding: utf8
""" 
@File: demo9_jsonify.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/7 13:33
"""

from flask import Flask, jsonify
import json

app = Flask(import_name=__name__)

@app.route('/')
def index():
    jsonify_data = {'key': 'value'}
    data = {'key_json': 'value_json'}
    json_data = json.dumps(data)
    return jsonify(jsonify_data)
    # return json_data


if __name__ == '__main__':
    app.run(debug=True)

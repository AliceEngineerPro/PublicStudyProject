# coding: utf8
""" 
@File: server.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/30 15:30
"""

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(import_name=__name__)

@app.route('/indexdata', methods=['GET', 'POST'])
def index():
    try:
        print(request.args.get('name'))
        print(request.args.get('age'))
        return jsonify({
            'code': 200,
            'msg': 'Success',
            'data': {
                'name': request.args.get('name'),
                'age': request.args.get('age')
            }
        })
    except Exception as error:
        return jsonify({
            'code': 500,
            'msg': '{}'.format(error),
            'data': None
        })
    
CORS(app, supports_credentials=True)

print(app.url_map)
app.run(
    debug=True,
    port=52015,
    host='0.0.0.0'
)



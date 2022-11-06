# coding: utf8
""" 
@File: __init__.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/7 0:27
"""

from flask import Blueprint

news_bp = Blueprint(name='news_bp', import_name=__name__, url_prefix='/v1_1011_beta')

# coding: utf8
""" 
@File: views.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/7 0:27
"""

from . import news_bp

@news_bp.route('/news')
def news_index():
    return 'news info'


# coding: utf8
""" 
@File: set_config.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/6 22:40
"""

class DefaultConfig(object):
    _NAME_SPACES = '测试环境'
    
    
class ProjectConfig(DefaultConfig):
    _NAME_SPACES = '生产环境'


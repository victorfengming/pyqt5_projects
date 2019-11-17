#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by 秋叶夏风

# 本模块的功能:<>

"""

17675270
q5LtHDDvwlWoKIpwt0SzFT4B
9TGgtfTGMXf9mw7QkzkdoKcx4236Pvxg
"""
from aip import AipImageCensor

""" 你的 APPID AK SK """
APP_ID = '17675270'
API_KEY = 'q5LtHDDvwlWoKIpwt0SzFT4B'
SECRET_KEY = '9TGgtfTGMXf9mw7QkzkdoKcx4236Pvxg'

client = AipImageCensor(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

""" 调用色情识别接口 """
result = client.imageCensorUserDefined(get_file_content('./images/1.jpg'))

for i,j in result.items():
    print(i,"--->",j)
#
# """ 如果图片是url调用如下 """
# result = client.imageCensorUserDefined('http://www.example.com/image.jpg')









'''

       ┌─┐       ┌─┐ + +
    ┌──┘ ┴───────┘ ┴──┐++
    │                 │
    │       ───       │++ + + +
    ███████───███████ │+
    │                 │+
    │       ─┴─       │
    │                 │
    └───┐         ┌───┘
        │         │
        │         │   + +
        │         │
        │         └──────────────┐
        │                        │
        │                        ├─┐
        │                        ┌─┘
        │                        │
        └─┐  ┐  ┌───────┬──┐  ┌──┘  + + + +
          │ ─┤ ─┤       │ ─┤ ─┤
          └──┴──┘       └──┴──┘  + + + +
                 神兽保佑
                代码无BUG!


'''

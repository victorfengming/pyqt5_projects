#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by 秋叶夏风

# 本模块的功能:<pyqt5主模块>


# 导入python系统类库
import sys

# 导入pyqt5类用到的类库,QApplication应用程序类,Qwidget控件的基类
from PyQt5.QtWidgets import QApplication,QWidget

# 导入生成界面类的模块
import first

# 这回不写main了
# 直接就实例化一个类,通过构造函数传入一个python的应用参数
print(sys.argv) # 这里打印出包含当前文件绝对路径名称的列表
# sys.argv就是自己的文件名称的列表
app = QApplication(sys.argv)

# 实例化界面基类
w = QWidget()

# 实例化生成的界面的类
form = first.Ui_Form()
# 将生成的窗体控件及配置载入到w控件对象汇总
form.setupUi(w)
# 使用窗体显示
w.show()
# app.exec_()表示程序界面监听事件的开始,是一个死循环
# 这里说白了是一个死循环,就像tkinter中的loop一样
sys.exit(app.exec_())


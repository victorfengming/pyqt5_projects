#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by 秋叶夏风

# 本模块的功能:<>


import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGraphicsLayout, QLineEdit, QLabel, \
    QPushButton,QBoxLayout


class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("刘金玉编程")
        self.setGeometry(app.desktop().width() / 2 - self.width() / 2, app.desktop().height() / 2 - self.height() / 2,
                         400, 300)

        lblCode = QLabel("验证码", self)
        leCode = QLineEdit(self)
        btnCode = QPushButton("验证",self)

        # 采用绝对布局

        # leCode.move(100,0)
        # btnCode.move(130,0)
        # hlayout = QHBoxLayout(self)
        # hlayout.addWidget(lblCode)
        # hlayout.addWidget(leCode)
        # hlayout.addWidget(btnCode)
        # 放一个弹簧在这里
        vlayout = QVBoxLayout(self)
        vlayout.addWidget(lblCode)
        vlayout.addWidget(leCode)
        vlayout.addWidget(btnCode)
        vlayout.addStretch(2)
        self.show()


app = QApplication(sys.argv)
mc = MyClass()
app.exec_()

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

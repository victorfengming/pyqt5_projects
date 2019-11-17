#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by 秋叶夏风

# 本模块的功能:<一个三原色>

import sys

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QFrame


class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("刘金玉编程")
        self.color = QColor(0,0,0)
        dk = app.desktop()
        self.setGeometry(dk.width()/2-self.width()/2,200,400,300)

        # 设置点击后,能记住状态
        btnRed = QPushButton("红")
        btnRed.setCheckable(True)
        btnRed.clicked[bool].connect(self.setColor)
        btnGreen = QPushButton("绿")
        btnGreen.setCheckable(True)
        btnGreen.clicked[bool].connect(self.setColor)
        btnBlue = QPushButton("蓝")
        btnBlue.setCheckable(True)
        btnBlue.clicked[bool].connect(self.setColor)

        vlo = QVBoxLayout(self)
        vlo.addWidget(btnRed)
        vlo.addWidget(btnGreen)
        vlo.addWidget(btnBlue)

        self.myframe = QFrame(self)
        hlo = QHBoxLayout(self)
        hlo.addLayout(vlo)
        hlo.addWidget(self.myframe)
        self.show()

    def setColor(self,p):
        b = self.sender()
        # 根据是否选中按钮来决定颜色的值是否拥有
        if p:
            v = 255
        else:
            v = 0
        # 根据按钮的文字来决定哪个参数被赋值为255或者0
        if b.text() == "红":
            self.color.setRed(v)
        elif b.text() == "绿":
            self.color.setGreen(v)
        elif b.text() == "蓝":
            self.color.setBlue(v)

        self.myframe.setStyleSheet("QWidget{background-color:%s}" % self.color.name())
        print(self.color.name())


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

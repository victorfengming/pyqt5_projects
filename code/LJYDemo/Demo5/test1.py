#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by 秋叶夏风

# 本模块的功能:<>


import sys

from PyQt5.QtGui import QIcon, QFont

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip

app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle("刘金玉编程")
app.setWindowIcon(QIcon("./images/车.png"))
QToolTip.setFont(QFont("隶书",40))
w.setToolTip("编程创造城市")
# 按钮
btn = QPushButton("老刘",w)
btn.move(50,50)
btn.setToolTip("你好buton")
w.show()

app.exec_()












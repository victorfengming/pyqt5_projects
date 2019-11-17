#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by 秋叶夏风

# 本模块的功能:<>


import sys

from PyQt5.QtWidgets import  QApplication,QWidget,QLineEdit,QTextEdit,QLabel,QGridLayout,QHBoxLayout,QVBoxLayout

class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("刘金玉编程")
        self.setGeometry(300,200,400,300)

        lbltitle = QLabel("标题")
        lblauthor = QLabel("作者")
        lblcontent = QLabel("内容")

        letitle = QLineEdit()
        leautor = QLineEdit()
        lecontent = QTextEdit()

        grid = QGridLayout(self)
        grid.addWidget(lbltitle,0,0)
        grid.addWidget(letitle,0,1)
        grid.addWidget(lblauthor,1,0)
        grid.addWidget(leautor,1,1)
        grid.addWidget(lblcontent,2,0)
        grid.addWidget(lecontent,2,1)

        self.show()


app = QApplication(sys.argv)
mc = MyClass()

app.exec_()













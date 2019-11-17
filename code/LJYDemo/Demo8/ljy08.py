#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by 秋叶夏风

# 本模块的功能:<>

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton,QLabel


class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("刘金玉编程")
        lb = QLabel("编程创造城市",self)
        self.resize(400,300)
        # PyQt5默认就是居中的了
        self.move(100,130)
        self.show()
        self.center()

    def center(self):
        dk = app.desktop()
        self.move(dk.width()/2-self.width()/2,dk.height()/2-self.height()/2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mc = MyClass()
    app.exec_()


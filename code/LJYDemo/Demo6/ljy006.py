#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by 秋叶夏风

# 本模块的功能:<>

import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("刘金玉编程")
        self.setGeometry(30,40,300,200)
        btn = QPushButton("关闭",self)
        btn.move(5,6)
        # 将信号发送到一个槽
        # 设置按钮的点击后关闭窗体的时间
        btn.clicked.connect(self.close)
        self.show()

app = QApplication(sys.argv)
c = MyClass()
app.exec_()






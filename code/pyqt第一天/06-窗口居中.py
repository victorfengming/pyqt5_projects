#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>

import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication

class Example(QWidget):

    def __init__(self):
        print('init方法执行')
        super().__init__()
        self.initUI()


    def initUI(self):
        print('initUI方法执行')
        self.resize(250, 150)
        self.center()
        self.setWindowTitle('Center')
        self.show()


    def center(self):
        print('center方法执行')
        qr = self.frameGeometry()
        print('qr:',qr)
        cp = QDesktopWidget().availableGeometry().center()
        print('cp:',cp)
        qr.moveCenter(cp)
        print('qr的topLeft:',qr.topLeft())
        self.move(qr.topLeft())



app = QApplication(sys.argv)
ex = Example()
app.exec()
# sys.exit(app.exec_())















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

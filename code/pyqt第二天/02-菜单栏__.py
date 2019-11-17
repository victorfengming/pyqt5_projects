#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>

import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import qApp
from PyQt5.QtWidgets import QApplication

from PyQt5.QtGui import QIcon


class Demo(QMainWindow):

    def __init__(self):
        # 重新执行父类的初始化方法(默认的一些操作)
        super().__init__()
        # 加入自定义方法
        self.initUI()

    def initUI(self):
        # 设置菜单的图标
        exitAct = QAction(QIcon('exit.png'),'&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        file_menu = menubar.addMenu('&File')
        file_menu.addAction(exitAct)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle('简单的菜单')
        self.show()





app = QApplication(sys.argv)
ex = Demo()
app.exec()











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

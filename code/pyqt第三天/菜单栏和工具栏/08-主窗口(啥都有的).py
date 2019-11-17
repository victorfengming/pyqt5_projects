#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>
import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):

        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        exitAct = QAction(QIcon('logo.png'), '退退退', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('退出应用')
        exitAct.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('文件')
        fileMenu.addAction(exitAct)

        toolbar = self.addToolBar('退出')
        toolbar.addAction(exitAct)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('代码编辑工具')
        self.show()


app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
















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

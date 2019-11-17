#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>

# 导入模块
import sys
from PyQt5.QtWidgets import  QWidget
from PyQt5.QtWidgets import  QMessageBox
from PyQt5.QtWidgets import  QApplication

# 创建一个类
class Example(QWidget):

    def __init__(self):
        super().__init__()
        # 执行自己的函数
        self.initUI()

    def initUI(self):
        self.setGeometry(300,200,250,150)
        self.setWindowTitle('消息盒子')
        self.show()

    def closeEvent(self, QCloseEvent):

        reply = QMessageBox.question(self, '消息啊哈!',"你确定你要退出了",QMessageBox.yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

app = QApplication(sys.argv)
demo = Example()
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

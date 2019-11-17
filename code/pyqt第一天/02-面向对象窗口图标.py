#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<pyqt5的第一个程序>
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we create a simple
window in PyQt5.

author: Jan Bodnar
website: zetcode.com
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Example(QWidget):

    def __init__(self):
        # 调用爸爸的init初始化魔术方法
        super().__init__()

        self.initUI()
    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('logo.png'))
        self.show()

# 这行代码表示,这个模块既可以自己执行,又可以被引用并且不执行
# if __name__ == '__main__':


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

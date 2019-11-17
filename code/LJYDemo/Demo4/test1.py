#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by 秋叶夏风

# 本模块的功能:<>

import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon

app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle("刘金玉编程")
# w.setWindowIcon(QIcon("./images/clz.png"))
w.show()

# 第二个窗体
w2 = QWidget()
# w2.setWindowIcon(QIcon("./images/车辆.png"))
w2.show()


app.setWindowIcon(QIcon("./images/水枪.png"))
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

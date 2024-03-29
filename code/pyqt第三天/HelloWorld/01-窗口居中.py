#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>

# 导入需要的包和模块
import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QDesktopWidget
# QDesktopWidget这个库提供了用户的桌面信息,包括屏幕的大小
from PyQt5.QtWidgets import QApplication

# 创建一个类
class Ex(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(250,150)
        self.center()
        # 这个方法调用我们下面写的,实现对话框居中的方法
        self.setWindowTitle('chuangkou要居中')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        # 得到了主窗口大小
        print('qr:',qr)
        cp = QDesktopWidget().availableGeometry().center()
        # 获取显示器的分辨率,然后得到中间点的位置
        print('cp:',cp)
        qr.moveCenter(cp)
        # 然后把自己的窗口的中心点放到qr的中心点
        self.move(qr.topLeft())

app = QApplication(sys.argv)
demo1 = Ex()
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

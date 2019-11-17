#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>

# 导入模块
import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QToolTip
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QApplication

from PyQt5.QtGui import QFont


# 来直接来一个类
class Demo(QWidget):    #继承自QWidget

    # 初始化魔术方法直接上
    def __init__(self):
        # 父类的方法还原
        super().__init__()
        # 执行自己的方法
        self.initUI()
    def initUI(self):
        # 这个字体的话,系统中有的都行
        QToolTip.setFont(QFont('微软雅黑',15))
        # 这个 例子中,我们创建 了一个提示框
        self.setToolTip('不信了还<b>这是一个啥玩意</b>')
        # 这个高,实在是高
        # html中的标签也能应用样式
        # 强，实在是强
        btn = QPushButton('点我',self)
        # 这个静态方法设置了提示框的字体,我们使用了15px的微软雅黑的字体
        btn.setToolTip('君不见黄河之水<br>天上来')
        # 调用setTooltip()创建提示框可以使用富文本格式的内容
        btn.resize(btn.sizeHint())
        btn.move(50,70)

        self.setGeometry(200,150,800,450)
        self.setWindowTitle('标题就是没有标题')
        # 显示
        self.show()

app = QApplication(sys.argv)
ex1 = Demo()
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

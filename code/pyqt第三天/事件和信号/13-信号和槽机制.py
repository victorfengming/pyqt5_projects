#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>

'''
事件
signals and slots 被其他人翻译成信号和槽机制，(⊙o⊙)…我这里还是不翻译好了。
所有的应用都是事件驱动的。事件大部分都是由用户的行为产生的，当然也有其他的事件产生方式，比如网络的连接，窗口管理器或者定时器等。调用应用的exec_()方法时，应用会进入主循环，主循环会监听和分发事件。
在事件模型中，有三个角色：
事件源
事件
事件目标
事件源就是发生了状态改变的对象。事件是这个对象状态改变的内容。事件目标是事件想作用的目标。事件源绑定事件处理函数，然后作用于事件目标身上。
PyQt5处理事件方面有个signal and slot机制。Signals and slots用于对象间的通讯。事件触发的时候，发生一个signal，slot是用来被Python调用的（相当于一个句柄？这个词也好恶心，就是相当于事件的绑定函数）slot只有在事件触发的时候才能调用。
'''

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import \
    (QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        lcd = QLCDNumber(self)
        print("lcd:",lcd)
        sld = QSlider(Qt.Horizontal, self)
        print("sld",sld)
        vbox = QVBoxLayout()
        print(vbox)
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        print(lcd.display)
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('信号和槽机制的')
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

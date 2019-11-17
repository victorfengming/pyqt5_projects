#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by 秋叶夏风

# 本模块的功能:<pyqt5>

import sys
from PyQt5.QtWidgets import  QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(400,300)
    w.move(200,300)
    w.setWindowTitle("刘金玉编程")
    w.show()
    sys.exit(app.exec())




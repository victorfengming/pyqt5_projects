#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by 秋叶夏风

# 本模块的功能:<>

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton


class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 200, 300, 400)
        self.setWindowTitle("刘金玉编程")
        btn = QPushButton("关闭窗体", self)
        btn.move(50, 50)
        btn.clicked.connect(self.close)
        self.show()

    def closeEvent(self, QCloseEvent):
        print("挂表按钮点击 来了")
        # 不要马上关闭
        res = QMessageBox.question(self, "消息提示tit:", "你可想好了要关闭窗体么?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if res == QMessageBox.Yes:
            print("关闭")
            QCloseEvent.accept()
        else:
            print("谢谢")
            QCloseEvent.ignore()
            QMessageBox.information(self, "消息", "谢谢!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mc = MyClass()

    app.exec_()

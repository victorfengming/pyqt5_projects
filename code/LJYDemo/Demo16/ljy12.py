import sys

from PyQt5.QtCore import Qt, QBasicTimer
from PyQt5.QtGui import QColor,QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QSlider, QProgressBar, QPushButton


class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("刘金玉编程")
        self.setGeometry(400, 100, 400, 280)

        self.lbl = QLabel("图片",self)
        self.pm = QPixmap("./img/th.jpg")
        self.lbl.setPixmap(self.pm)
        self.lbl.resize(300,200)
        self.lbl.setScaledContents(True)

        # 移除按钮
        btn1 = QPushButton("移除图片",self)
        btn1.clicked.connect(self.myRemovePic)
        btn1.move(0,240)
        # 增加图片
        btn2 = QPushButton("增加图片",self)
        btn2.move(0,220)
        btn2.clicked.connect(self.addPic)
        self.show()

    def myRemovePic(self):
        print("zhihjgid")
        self.lbl.setPixmap(QPixmap(""))

    def addPic(self):
        self.lbl.setPixmap(self.pm)



app = QApplication(sys.argv)

mc = MyClass()

app.exec_()

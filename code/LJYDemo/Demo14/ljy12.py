import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QSlider


class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("liujnikjnyubainchedng")
        self.setGeometry(400,100,400,300)
        sl = QSlider(Qt.Horizontal,self)
        sl.move(50,50)
        sl.setMinimum(0)
        sl.setMaximum(255)
        sl.valueChanged[int].connect(self.myValue)
        self.show()

    def myValue(self,a):
        my_color = QColor(0,0,0)
        my_color.setBlue(a)
        self.setStyleSheet("QWidget{background-color:%s}"% my_color.name())
        print(a)


app = QApplication(sys.argv)

mc = MyClass()

app.exec_()
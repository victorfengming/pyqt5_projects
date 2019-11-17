import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QFrame, QCheckBox


class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("liujnikjnyubainchedng")
        self.setGeometry(400,100,400,300)

        myframe1 = QFrame(self)
        myframe1.move(30,0)
        self.ck1 = QCheckBox("跳舞",myframe1)
        self.ck1.stateChanged[int].connect(self.myState)
        self.ck1.move(0,50)
        self.ck2 = QCheckBox("唱歌",myframe1)
        self.ck2.stateChanged[int].connect(self.myState)
        self.ck2.move(0,30)

        self.show()

    def myState(self,a):
        s = self.sender()
        if a == Qt.Checked:
            print(s.text())
        else:
            print("取消了")
        print(Qt)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mc = MyClass()

    app.exec_()
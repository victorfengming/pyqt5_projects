import sys

from PyQt5.QtWidgets import QApplication,QWidget,QLineEdit,QLabel

class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("liujnikjnyubainchedng")
        self.setGeometry(400,100,400,300)
        self.lbl = QLabel("显示区",self)
        self.lbl.move(50,50)

        le = QLineEdit(self)
        le.textChanged[str]()


        self.show()

app = QApplication(sys.argv)

mc = MyClass()

app.exec_()
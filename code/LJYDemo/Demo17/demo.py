import sys



from PyQt5.QtCore import Qt, QBasicTimer
from PyQt5.QtGui import QColor,QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QSlider, QProgressBar, QPushButton, QComboBox, QFrame


class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle("liujinr")
        self.setGeometry(300,100,400,300)

        myframe1 = QFrame(self)
        myframe1.move(50,50)
        lbl_1 = QLabel("省",myframe1)
        lbl_1.move(0,3)
        combox_1 = QComboBox(myframe1)
        combox_1.move(20,0)

        # 省份
        combox_1.addItem("请选择省份")
        combox_1.addItem("浙江")
        combox_1.addItem("江苏")
        combox_1.addItem("安徽")
        combox_1.addItem("北京")
        combox_1.activated[str].connect(self.myActived)
        # 这个[str]就像java中的泛型,可以指定传递数据的数据类型


        lbl_1 = QLabel("市",myframe1)
        lbl_1.move(110,3)
        # 市级别
        self.combox_2 = QComboBox(myframe1)
        self.combox_2.move(125, 0)

        # 市份
        # self.combox_2.addItem("请选择市份")
        # self.combox_2.addItem("沈阳")
        # self.combox_2.addItem("大连")
        # self.combox_2.addItem("西城")
        # self.combox_2.addItem("海淀")

        self.show()


    def myActived(self,s):
        if s == "浙江":
            self.combox_2.addItem("杭州")
            self.combox_2.addItem("宁波")
            self.combox_2.addItem("温州")
            print(s)
        elif s == "江苏":
            self.combox_2.addItem("苏州")
            self.combox_2.addItem("无锡")
            self.combox_2.addItem("扬州")
            self.combox_2.addItem("南京")


app = QApplication(sys.argv)

mc = MyClass()

app.exec_()
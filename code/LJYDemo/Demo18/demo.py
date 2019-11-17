import sys



# 实现一个日历控件
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QCalendarWidget, QLabel, QVBoxLayout, QApplication, QWidget
from PyQt5.QtCore import QDate, Qt


class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle("liujinr")
        self.setGeometry(300,100,400,300)

        cal = QCalendarWidget()
        cal.clicked[QDate].connect(self.myCalender)
        self.lbl = QLabel("这里显示日期")
        self.lbl.setFont(QFont("华文行楷",20))

        # 盒子模型
        vlo = QVBoxLayout(self)
        vlo.addWidget(cal)
        vlo.addWidget(self.lbl)


        self.show()

    def myCalender(self,d):
        mydate = QDate(d)
        self.lbl.setText(mydate.toString("yyyy-MM-dd"))
        # self.lbl.setText(mydate.toString(Qt.ISODate))
        print(mydate.toString())



if __name__ == '__main__':

    app = QApplication(sys.argv)
    mc = MyClass()
    app.exec_()
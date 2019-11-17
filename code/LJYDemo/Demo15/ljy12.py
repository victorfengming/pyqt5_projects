import sys

from PyQt5.QtCore import Qt, QBasicTimer
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QSlider, QProgressBar, QPushButton


class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("刘金玉编程")
        self.setGeometry(400, 100, 400, 300)
        # 载入进度条
        self.pgb = QProgressBar(self)  # 类对象的初始化
        self.pgb.move(50, 50)  # 将进度条移动到指定的位置
        self.pgb.resize(300, 20)  # 设置进度条宽高

        # 配置一个值表示进度条的当前进度
        self.pv = 0

        # 声明一个时钟控件
        self.timer1 = QBasicTimer()

        # 设置进度条的范围
        self.pgb.setMinimum(0)  # 设置最小值
        self.pgb.setMaximum(100)  # 设置最大值
        self.pgb.setValue(0)  # 设置当前进度

        # 载入按钮
        self.btn = QPushButton("开始", self)
        self.btn.move(50, 100)
        self.btn.clicked.connect(self.myTimerState)

        self.show()

    def myTimerState(self):
        if self.timer1.isActive():  # 检测是否开启
            self.timer1.stop(50, self)
            self.btn.setText("开始")  # 这里的按钮的状态显示的是按钮下次的行为
        else:
            self.timer1.start(50, self)
            self.btn.setText("停止")

    def timerEvent(self, e):
        if self.pv == 100:
            self.tiemr1.stop()
            self.btn.setText("完成")
        else:
            self.pv += 1
            self.pgb.setValue(self.pv)  # 设置当前进度


app = QApplication(sys.argv)

mc = MyClass()

app.exec_()

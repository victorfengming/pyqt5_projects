import sys


from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QCalendarWidget, QLabel, QVBoxLayout, QApplication, QWidget, QMenu, QMenuBar, QMainWindow, \
    QMessageBox, QAction
from PyQt5.QtCore import QDate, Qt


class MyClass(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle("liujinr")
        self.setGeometry(300,100,400,300)
        # 之制作菜单
        # 利用窗体本身有的菜单栏功能进行载入
        my_menu = self.menuBar()    # 总菜单栏的返回对象
        file_menu = my_menu.addMenu("文件")   # 文件菜单的返回对象
        actNewWin = QAction("新家舱体",self)
        actNewWin.triggered.connect(self.myNewWin)
        file_menu.addAction(actNewWin)
        recent_file = file_menu.addMenu("最近的")  # 最新的菜单项的返回对象
        recent_file.addAction("文件1")
        recent_file.addAction("文件2")



        # my_menu.addAction("新建")
        my_menu.addAction("运行")
        my_menu.addAction("调试")
        actHelp = QAction("帮助",self)
        actHelp.triggered.connect(self.ljyHelp)
        # actHelp = QAction("帮助",self)
        my_menu.addAction(actHelp)

        self.show()

    def myNewWin(self):
        mc2 = MyClass2()
        list1.append(mc2)
        pass


    def ljyHelp(self):
        msgbox = QMessageBox( \
            QMessageBox.information( \
                self, "标题", "消息", QMessageBox.Yes | QMessageBox.No \
                ),self)
        # msgbox = QMessageBox(QMessageBox.Information,"帮助","欢迎",self)
        msgbox.show()

class MyClass2(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("编程创造城市")
        self.show()





if __name__ == '__main__':

    app = QApplication(sys.argv)
    mc = MyClass()
    list1 = []
    app.exec_()
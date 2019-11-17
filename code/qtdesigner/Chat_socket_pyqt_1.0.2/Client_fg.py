# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Client_fg.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import threading
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from Client_bg import *
class Ui_Form(object):
    def __init__(self):
        self.connect_init()



    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(528, 291)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 40, 291, 121))
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 200, 481, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.send_message)
        self.horizontalLayout.addWidget(self.pushButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", ""))
        self.pushButton.setText(_translate("Form", "发送"))



    def connect_init(self):
        self.c = Connect()
        self.c.socket_init('127.0.0.1')
        # 测试发送数据
        self.c.input_chat_content("我来冒个泡!")
        # t = threading.Thread(target=self.set_label_content, args=())
        # t.start()
        # t.join()


    def send_message(self):
        name = "victor"
        # 发送出去
        con = self.lineEdit.text()
        # 获取现在时间
        t = str(time.strftime("%H:%M:%S", time.localtime()))
        new_con = "\n" + t + " " + name + "说:" + con
        self.c.input_chat_content(new_con)
        self.label.setText(new_con)
        """
        # 设置本label显示
        con = self.lineEdit.text()
        # 获取现在时间
        t = str(time.strftime("%H:%M:%S", time.localtime()))
        new_con = self.label.text()+"\n"+t+" "+name+"说:"+con
        self.label.setText(new_con)
        # print()
        """
        # 清空input框
        self.lineEdit.setText("")

        print("--------------")
        print(message_content)
        print("--------------")


    def set_label_content(self):
        # while True:
        #     print("线程执行")
        self.label.setText(message_content)

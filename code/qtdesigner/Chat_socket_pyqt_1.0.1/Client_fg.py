# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Client_fg.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from Client_bg import *
from PyQt5.QtWidgets import QInputDialog


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(528, 291)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(140, 40, 259, 78))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(140, 140, 259, 78))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(320, 230, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.Connect_init)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "服务器IP地址:"))
        self.label_2.setText(_translate("Form", "请输入用户名:"))
        self.pushButton.setText(_translate("Form", "登录"))

    def Connect_init(self):
        c = Connect()
        c.socket_init('127.0.0.1')
        # 测试发送数据
        c.input_chat_content("我来冒个泡!")
        # 获取输入IP
        # text, ok = QInputDialog.getText(self, 'Input Dialog',
        #                                 'Enter your name:')
        # print("text--->",text)
        # print("ok--->",ok)

    #
    # def send_message(self):
    #     self.lbl.setText(mydate.toString(1))
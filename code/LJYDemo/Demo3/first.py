# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 300)
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(60, 70, 37, 18))
        self.toolButton.setObjectName("toolButton")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(180, 140, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.buttonBox = QtWidgets.QDialogButtonBox(Form)
        self.buttonBox.setGeometry(QtCore.QRect(300, 240, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.toolButton.setText(_translate("Form", "..."))
        self.pushButton.setText(_translate("Form", "PushButton"))

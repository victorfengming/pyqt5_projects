# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(459, 330)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.toolButton = QtWidgets.QToolButton(Dialog)
        self.toolButton.setGeometry(QtCore.QRect(30, 50, 37, 18))
        self.toolButton.setObjectName("toolButton")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(190, 30, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(210, 90, 89, 16))
        self.radioButton.setObjectName("radioButton")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(50, 100, 71, 16))
        self.checkBox.setObjectName("checkBox")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(Dialog)
        self.commandLinkButton.setGeometry(QtCore.QRect(110, 150, 185, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(30, 200, 120, 80))
        self.groupBox.setObjectName("groupBox")
        self.buttonBox_2 = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox_2.setGeometry(QtCore.QRect(260, 120, 156, 23))
        self.buttonBox_2.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_2.setObjectName("buttonBox_2")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(40, 290, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.toolButton.setText(_translate("Dialog", "..."))
        self.pushButton.setText(_translate("Dialog", "PushButton"))
        self.radioButton.setText(_translate("Dialog", "RadioButton"))
        self.checkBox.setText(_translate("Dialog", "CheckBox"))
        self.commandLinkButton.setText(_translate("Dialog", "CommandLinkButton"))
        self.groupBox.setTitle(_translate("Dialog", "GroupBox"))

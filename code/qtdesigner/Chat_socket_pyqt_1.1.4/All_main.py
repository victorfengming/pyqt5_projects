#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by 秋叶夏风

# 本模块的功能:<图形化聊天界面主模块>



# 导入python系统类库
import sys

# 导入时间模块,用于获取聊天提示信息
import time

# 导入生成界面类的模块
from PyQt5 import QtCore, QtGui, QtWidgets
# 导入pyqt5类用到的类库,QApplication应用程序类,Qwidget控件的基类
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog

# 导入socket模块
import socket
import threading


# 定义连接类
class Connect:
    def socket_init(self,ip):

        # 创建socket对象
        self.s = socket.socket()
        # 连接远程主机
        self.s.connect((ip, 6666))
        def read_from_server(s):
            global message_content
            while True:
                mes = s.recv(2048).decode('utf-8')
                message_content += mes
                print("message_content--->",message_content)
                # main.form.set_label_content()
                # TODO 这里在局部调用了全局的变量
                # TODO 有待优化
                form.set_label_content()

        # 客户端启动线程不断地读取来自服务器的数据
        threading.Thread(target=read_from_server, args=(self.s, )).start()


    def input_chat_content(self,line):
        # line = input('')
        if line is None or line == 'exit':
            return
        # 将用户的键盘输入内容写入socket
        self.s.send(line.encode('utf-8'))



# 定义UI类
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Client_fg.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

class Ui_Form(object):
    def __init__(self):
        # TODO 初始化连接,这里需要改掉,加上用户名验证
        self.connect_init()


    def showDialog(self):
        self.name, ok = QInputDialog.getText(QWidget(), '用户登陆',
            'Enter your name:')
        if ok:
            print(self.name)
            # self.le.setText(str(text))
            # print(self.name+"哈哈")
        else:
            exit()

    # 初始化界面
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
        # 绑定按钮点击事件
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
        # 创建连接对象
        self.c = Connect()
        # self.c.socket_init('127.0.0.1')
        self.c.socket_init('39.106.139.40')
        # # 测试发送数据
        # con = "我来冒个泡!!!"
        # # 获取现在时间
        # t = str(time.strftime("%H:%M:%S", time.localtime()))
        # new_con = "\n" + t + " [" + self.name + "]:" + con
        #
        # # 发送出去
        # self.c.input_chat_content(new_con)



    # TODO 这个类中的方法用到了那个模块的
    def send_message(self):
        # name = "victor"
        # 获取输入框中的内容
        con = self.lineEdit.text()
        # 获取现在时间
        t = str(time.strftime("%H:%M:%S", time.localtime()))
        new_con = "\n" + t + " [" + self.name + "]:" + con

        # 发送出去
        self.c.input_chat_content(new_con)
        # self.label.setText(new_con)
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
        self.label.setText(message_content)


if __name__ == '__main__':

    # TODO 这里的显示内容的当前模块的
    # TODO 在一个模块中的变量所有的类都能用上,要不然就会出现调用的时候还没定义
    # TODO 而且还没有传递引用,传递的是值这就难受了

    message_content = "init_content"


    # 实例化App对象
    app = QApplication(sys.argv)

    # 实例化界面基类
    w1 = QWidget()

    # 实例化生成的界面的类
    form = Ui_Form()
    # 先输入服务端ip
    # 将生成的窗体控件及配置载入到w控件对象汇总
    form.setupUi(w1)
    form.showDialog()
    # 使用窗体显示
    # 这里就执行了一次
    form.set_label_content()

    # 显示窗体
    w1.show()

    # 主消息循环
    sys.exit(app.exec_())


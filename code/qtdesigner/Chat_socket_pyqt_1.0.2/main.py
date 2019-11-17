#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by 秋叶夏风

# 本模块的功能:<图形化聊天界面主模块>



# 导入python系统类库
import sys

# 导入pyqt5类用到的类库,QApplication应用程序类,Qwidget控件的基类

from PyQt5.QtWidgets import QApplication,QWidget

# 导入生成界面类的模块
from Client_fg import *
from Client_bg import *



if __name__ == '__main__':


    app = QApplication(sys.argv)

    # 实例化界面基类
    w1 = QWidget()

    # 实例化生成的界面的类
    form = Ui_Form()
    # 将生成的窗体控件及配置载入到w控件对象汇总
    form.setupUi(w1)
    # 使用窗体显示
    form.set_label_content()

    w1.show()

    sys.exit(app.exec_())


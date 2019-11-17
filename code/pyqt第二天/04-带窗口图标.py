#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>

# 首先还是要导入对应的模块
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QIcon


# 之前的例子是过程式编程,python当然支持面向对象编程
# 创建一个类
class Test(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()  # 使用initUI方法创建了一个GUI

    '''
    面向对象编程最重要的三个部分是类(class),数据和方法.
    我们创建了一个类的调用,这个类继承自QWidget.
    这个就意味着,我们调用了两个构造器,一个是这个类本身的,一个是这个类继承的
    super()构造器方法返回父级的对象.__init()方法是构造器的一个方法.
    俗称初始化魔术方法
    '''

    def initUI(self):
        self.setGeometry(300, 200, 700, 400)
        self.setWindowTitle('标题起啥都行')
        self.setWindowIcon(QIcon('logo.png'))
        '''
        上面三个方法都是继承自QWidget类.
        setGeometry() 有两个作用: 把窗口放到屏幕上并且设置窗口大小.
                                参数分别代表屏幕坐标的x y 和窗口大小的长和宽
        setWindowTitle就是设置标题内容,不用多说
        也就是说这个方法是 resize()和move()的合体.
        最后一个方法就是添加图标,先创建一个QIcon对象,然后接受一个路径主辅材作为参数,显示图标
        '''
        self.show()


yingyong = QApplication(sys.argv)
ex1 = Test()
sys.exit(yingyong.exec_())

# 应用和示例的对象创立,主循环开始



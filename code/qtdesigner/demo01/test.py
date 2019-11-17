
import sys
from PyQt5.QtWidgets import *
# 导入生成的 py模块
from demo01 import *
# 创建app
app = QApplication(sys.argv)
# 实例化主窗口对象
w = QMainWindow()
# 实例化并调用初始化方法
Ui_MainWindow().setupUi(w)
# 显示窗口
w.show()
sys.exit(app.exec_())

# pyinstaller -F -w --paths=C:\Python\Python35\Lib\site-packages\PyQt5\Qt\bin --paths=C:\Python\Python35\Lib\site-packages\PyQt5\Qt\plugins  master.py
# ————————————————
# 版权声明：本文为CSDN博主「damnivictory」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/damnivictory/article/details/73527160
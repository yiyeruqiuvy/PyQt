# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'close.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from diaoyong  import *

class SecondUi(QtWidgets.QWidget):#建立第二个窗口的类
    def __init__(self):
        super(SecondUi, self).__init__()
        self.init_ui()
 
    def init_ui(self):
        self.resize(500, 350)#设置第二个窗口代码
        self.setWindowTitle('Second Ui')#设置第二个窗口标题
        self.btn = QtWidgets.QPushButton('jump', self)#设置按钮和按钮名称
        self.btn.setGeometry(150, 150, 100, 50)#前面是按钮左上角坐标，后面是按钮大小
        self.btn.clicked.connect(self.slot_btn_function)#将信号连接到槽
 
    def slot_btn_function(self):
        self.hide()#隐藏此窗口
        self.f = FirstUi()#将第一个窗口换个名字
        self.f.show()#将第一个窗口显示出来


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = FirstUi()#将第一和窗口换个名字
    w.show()#将第一和窗口换个名字显示出来
    sys.exit(app.exec_())
1.PyQt5提供了布局管理模块来支持部件的水平布局和垂直布局：

- QHBoxLayout：水平布局；
- QVBoxLayout ：垂直布局。

2.网格布局QGridLayout



3.qt designer  command +r 预览gui



4.![3B67B912-E8F3-4ABE-A7F3-E6EE792C0E83](/Users/vy/Library/Containers/com.tencent.qq/Data/Library/Application Support/QQ/Users/1163434981/QQ/Temp.db/3B67B912-E8F3-4ABE-A7F3-E6EE792C0E83.png)

![image-20191012204352934](/Users/vy/Library/Application Support/typora-user-images/image-20191012204352934.png)





## 5多窗口切换*



思路：将不同的窗口写成不同的类，一个主窗口，多个子窗口

在类里面初始化运行方法显示写好的窗口

在不同的类里面链接不同的信号槽实现窗口的跳转

主窗口：diaoyong.py

```
import sys#导入系统
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from close import *
 
class FirstUi(QMainWindow):#第一个窗口类
    def __init__(self):
        super(FirstUi, self).__init__()
        self.init_ui()
 
    def init_ui(self):
        self.resize(300, 200)#设置窗口大小
        self.setWindowTitle('First Ui')#设置窗口标题
        self.btn = QPushButton('jump111111', self)#设置按钮和按钮名称
        self.btn.setGeometry(50, 100, 100, 50)#前面是按钮左上角坐标，后面是窗口大小
        self.btn.clicked.connect(self.slot_btn_function)#将信号连接到槽
 
    def slot_btn_function(self):
        self.hide()#隐藏此窗口
        self.s = SecondUi()#将第二个窗口换个名字
        self.s.show()#经第二个窗口显示出来
 
 
def main():
    app = QApplication(sys.argv)
    w = FirstUi()#将第一和窗口换个名字
    w.show()#将第一和窗口换个名字显示出来
    sys.exit(app.exec_())#app.exet_()是指程序一直循环运行直到主窗口被关闭终止进程（如果没有这句话，程序运行时会一闪而过）
 
 
if __name__ == '__main__':#只有在本py文件中才能用，被调用就不执行
    main()
```

子窗口：close.py

```
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
```

参考：

https://blog.csdn.net/shangxiaqiusuo1/article/details/85253264
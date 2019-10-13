# coding:utf-8
import sys
from PyQt5.QtWidgets import QMainWindow,QGridLayout,QApplication,QAction,QLabel,QPushButton,QHBoxLayout,QVBoxLayout,QWidget
from PyQt5.QtCore import Qt

class GUi(QMainWindow):
	def __init__(self):
		super().__init__()
		self.add_menu()
		self.add_position()

	def add_menu(self):
		self.setWindowTitle("vy的第一个pyqt5")
		self.statusBar().showMessage("状态栏不能动态显示")
		self.resize(500,300)

		#菜单栏
		menu = self.menuBar()
		#menu_2 = self.menuBar()
		#菜单
		file_menu = menu.addMenu("文件")

		select_menu = menu.addMenu("选择")

		new_action_1 = QAction('新文件',self)
		#跟新状态栏
		new_action_1.setStatusTip('打开新文件')
		# 添加一个行为到菜单
		file_menu.addAction(new_action_1)

		# 创建退出行为
		exit_action = QAction('退出',self)
		#退出操作
		exit_action.setStatusTip("点击退出应用程序")
		#点击关闭程序
		exit_action.triggered.connect(self.close)
		#设置退出快捷键
		exit_action.setShortcut('Ctrl+Q')
		file_menu.addAction(exit_action)


		new_action_2 = QAction('选择1',self)
		select_menu.addAction(new_action_2)
		new_action_3 = QAction('选择2',self)
		select_menu.addAction(new_action_3)

	def add_position(self):
		#mbar_height = self.menuBar().height(). 获取高度
		#两个标签
		label_1 = QLabel('标签1',self)
		#label_1.move(10,mbar_height) 移动标签
		label_2 = QLabel('标签2',self)


		#两个按钮
		button_1 = QPushButton('按钮1',self)
		button_2 = QPushButton('按钮2',self)
		button_3 = QPushButton('按钮3',self)

		'''#使用水平和垂直盒子来达到效果
		#创建2水平盒子
		hbox_1 = QHBoxLayout()
		hbox_2 = QHBoxLayout()

		#给盒子添加相应的标签和按钮
		hbox_1.addWidget(label_1)
		hbox_1.addWidget(button_1)
		hbox_2.addWidget(label_2)
		hbox_2.addWidget(button_2)

		#创建垂直盒子包含以上2水平盒子
		vbox = QVBoxLayout()
		vbox.addLayout(hbox_1)
		vbox.addLayout(hbox_2)

		#创建一个窗口部件，设置布局为垂直盒子
		layout_widget = QWidget()
		layout_widget.setLayout(vbox)'''

		#创建一个网格布局
		grid_layout = QGridLayout()

		#在网格中添加窗口部件
		grid_layout.addWidget(label_1,0,0)# 0行0列
		grid_layout.addWidget(button_1,0,1)# 0行1列
		grid_layout.addWidget(label_2,1,0)# 1行0列
		grid_layout.addWidget(button_2,1,1)# 1行1列
		grid_layout.addWidget(button_3,2,0,1,5)# 1行1列

		#对齐方式
		grid_layout.setAlignment(Qt.AlignTop)
		grid_layout.setAlignment(label_1,Qt.AlignRight)

		#创建一个窗口对象
		layout_widget = QWidget()
		#设置窗口的布局层
		layout_widget.setLayout(grid_layout)




		self.setCentralWidget(layout_widget)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	gui = GUi()
	gui.show()
	sys.exit(app.exec_())


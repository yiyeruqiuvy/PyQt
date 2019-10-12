# coding:utf-8
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QAction,QLabel,QPushButton
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
		mbar_height = self.menuBar().height()
		#两个标签
		label_1 = QLabel('标签1',self)
		label_1.move(10,mbar_height)

		label_2 = QLabel('标签2',self)
		label_2.move(10,mbar_height*2)

		#两个按钮
		button_1 = QPushButton('按钮1',self)
		button_1.move(label_1.width(),mbar_height)

		button_2 = QPushButton('按钮1',self)
		button_2.move(label_1.width(),mbar_height*2)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	gui = GUi()
	gui.show()
	sys.exit(app.exec_())


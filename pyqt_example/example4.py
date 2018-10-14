import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from pyqt import Ui_MainWindow


# form_class = uic.loadUiType("./pyqt.ui")[0]

class TestForm(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

if __name__=="__main__":
	app = QApplication(sys.argv)
	window = TestForm()
	window.show()
	app.exec_()
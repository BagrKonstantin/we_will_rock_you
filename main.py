from test import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui, QtCore
import time
import sys
from session_2 import main as second_session





class Loader(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Loader, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Window 1')

        #self.pushButton.clicked.connect(self.first)
        self.pushButton_2.clicked.connect(self.second)



    def second(self):
        self.sec_window = second_session.Loader()
        self.sec_window.show()








if __name__ == "__main__":



    app = QtWidgets.QApplication(sys.argv)
    mainWindow = Loader()
    mainWindow.show()
    sys.exit(app.exec())
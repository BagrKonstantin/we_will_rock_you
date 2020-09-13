from test import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui, QtCore
import time



class Loader(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Loader, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Window 1')

        self.pushButton.clicked.connect(self.first)
        self.pushButton_2.clicked.connect(self.second)

    def first(self):
        pass








#if __name__ == "__main__":
    import sys

group_id = int("/post_super_post_by_author -1001276132597".split(" ")[1])
print(group_id)

    # app = QtWidgets.QApplication(sys.argv)
    # mainWindow = Loader()
    # mainWindow.show()
    # sys.exit(app.exec())
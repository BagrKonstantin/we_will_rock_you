from ui_main import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui, QtCore
import time
import sys

from session_1 import first_window as first_session
from session_2 import main as second_session
from session_3 import main as third_session
from session_4 import main as forth_session


class Main_Window(QMainWindow, Ui_MainWindow):
    def __init__(self, path):
        self.path = path
        super(Main_Window, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Window 1')

        # self.pushButton.clicked.connect(self.first)
        self.pushButton_1.clicked.connect(self.first)
        self.pushButton_2.clicked.connect(self.second)

        self.pushButton_3.clicked.connect(self.third)
        self.pushButton_4.clicked.connect(self.fourth)

        self.pushButton_5.clicked.connect(self.fifth)
        self.pushButton_6.clicked.connect(self.sixth)

        self.pushButton_7.clicked.connect(self.seventh)
        self.pushButton_8.clicked.connect(self.eighth)

    def first(self):
        print(1)
        self.first_window = first_session.Loader(self.path)
        self.first_window.show()

    def second(self):
        print(2)
        self.second_window = second_session.UI_Session2(self.path)
        self.second_window.show()

    def third(self):
        print(3)
        try:
            self.third_window = third_session.UI_Session3(self.path)
            self.third_window.show()
        except Exception as error:
            print(error)

    def fourth(self):
        print(4)
        self.forth_window = forth_session.UI_Session4(self.path)
        self.forth_window.show()

    def fifth(self):
        print(5)
        self.forth_window = forth_session.UI_Session4(self.path)
        self.forth_window.show()

    def sixth(self):
        print(6)

    def seventh(self):
        print(7)

    def eighth(self):
        print(8)


if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        mainWindow = Main_Window("nti_base.db")
        mainWindow.show()
        sys.exit(app.exec())
    except Exception as error:
        print(error)

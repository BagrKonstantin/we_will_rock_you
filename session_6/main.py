from session_6.ui_session6 import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui, QtCore
import sqlite3
import time
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg


def get_seconds(day, month, year):
    return time.mktime((year, month, day, 23, 59, 59, 0, 0, 0))

class UI_Session6(QMainWindow, Ui_MainWindow):
    def __init__(self, path):
        super(UI_Session6, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Window 4')

        #self.setCentralWidget(self.graphWidget)

        self.dateEdit_first = QtWidgets.QDateEdit(self)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateEdit_first.setFont(font)
        self.dateEdit_first.setCalendarPopup(True)  # +++
        self.dateEdit_first.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateEdit_first.setGeometry(QtCore.QRect(100, 20, 133, 30))

        self.dateEdit_second = QtWidgets.QDateEdit(self)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateEdit_second.setFont(font)
        self.dateEdit_second.setCalendarPopup(True)  # +++
        self.dateEdit_second.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateEdit_second.setGeometry(QtCore.QRect(300, 20, 133, 30))

        self.dateEdit_first.setDate(QtCore.QDate.currentDate())
        self.dateEdit_second.setDate(QtCore.QDate.currentDate())

        self.dateEdit_first.dateChanged.connect(lambda: self.update(self.dateEdit_first.text(), self.dateEdit_second.text()))
        self.dateEdit_second.dateChanged.connect(lambda: self.update(self.dateEdit_first.text(), self.dateEdit_second.text()))


        hour =         [1, 2,  3,  4,  5,  6,  7,  8,  9,  10]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]

        self.pyqtgraph.setBackground('w')
        pen = pg.mkPen("g")
        self.pyqtgraph.plot(hour, temperature, pen=pen)

    def update(self, first, second):
        day, month, year = [int(i) for i in first.split(".")]
        first = get_seconds(day, month, year) - 3600 * 24
        day, month, year = [int(i) for i in second.split(".")]
        second = get_seconds(day, month, year)
        # извлеч из бд все акб и время которые first < секунды <= second В формате (АКБ, секунды)



        print((int(second - first) // 3600 // 24))

        #достать из бд все (first <= АКБ <= second)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = UI_Session6("../nti_base.db")
    mainWindow.show()
    sys.exit(app.exec())

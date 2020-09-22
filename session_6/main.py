from session_6.ui_session6 import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui, QtCore
import sqlite3
import time
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from  random import choice


def get_seconds(day, month, year):
    return time.mktime((year, month, day, 23, 59, 59, 0, 0, 0))

class UI_Session6(QMainWindow, Ui_MainWindow):
    def __init__(self, path):
        super(UI_Session6, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Window 4')
        self.path = path

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

        self.dateEdit_first.dateChanged.connect(lambda: self.update_graph(self.dateEdit_first.text(), self.dateEdit_second.text()))
        self.dateEdit_second.dateChanged.connect(lambda: self.update_graph(self.dateEdit_first.text(), self.dateEdit_second.text()))




        self.pyqtgraph.setBackground('w')
        self.pen = pg.mkPen("g")


        self.con = sqlite3.connect(self.path)
        self.cur = self.con.cursor()

    def update_graph(self, first, second):
        day, month, year = [int(i) for i in first.split(".")]
        first = get_seconds(day, month, year) - 3600 * 24
        day, month, year = [int(i) for i in second.split(".")]
        second = get_seconds(day, month, year)
        print(first, second)

        print(self.cur.execute("""SELECT COUNT(*) FROM information_about_entrance WHERE id IN (SELECT id FROM entrance_details WHERE date BETWEEN {} AND {}) AND detail LIKE 'АКБ%'""".format(first, second)).fetchone())

        # извлеч из бд все акб и время которые first < секунды <= second В формате (АКБ, секунды)
        #
        date = []
        amount = []
        for i in range(int(second - first) // 3600 // 24):
            a = self.cur.execute(
                """SELECT SUM(amount) FROM information_about_entrance WHERE id IN (SELECT id FROM entrance_details WHERE date < {}) AND detail LIKE 'АКБ%'""".format(i * 3600 * 24 + first)).fetchone()
            date.append(i)
            amount.append(a[0])


        print(date)
        print(amount)
        print((int(second - first) // 3600 // 24))
        self.pyqtgraph.clear()
        self.pyqtgraph.plot(date, amount, pen=self.pen)

        #достать из бд все (first <= АКБ <= second)


# con = sqlite3.connect("../nti_base.db")
# cur = con.cursor()
#
# for i in range(1599685199, 1600203599, 3600 * 24 * 3):
#     id = choice([2, 6, 12])
#     cur.execute("INSERT INTO entrance_details (date) values ({})".format(i))
#     cur.execute("""INSERT INTO information_about_entrance (id, detail, amount) VALUES ((SELECT id FROM entrance_details WHERE date={}), (SELECT title FROM details WHERE id={}), 1)""".format(i, id))
#
# con.commit()
# cur.close()
#

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = UI_Session6("../nti_base.db")
    mainWindow.show()
    sys.exit(app.exec())

print(1599685199 + 3600 * 24 * 6)

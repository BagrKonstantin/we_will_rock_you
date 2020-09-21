from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets
import datetime
import sqlite3
import sys

from session_3.dialog import Ui_Dialog


class UI_Session3(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, path):
        super(UI_Session3, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Window 3')

        # подключение к бд
        self.con = sqlite3.connect(path)
        self.cur = self.con.cursor()
        data = self.cur.execute("""select * from details""").fetchall()

        # выпадающий календарь

        now = datetime.datetime.now()
        self.dateEdit = QtWidgets.QDateEdit(self)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateEdit.setFont(font)
        self.dateEdit.setCalendarPopup(True)  # +++
        self.dateEdit.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateEdit.setGeometry(QtCore.QRect(220, 120, 133, 30))

        self.dateEdit.setDate(QtCore.QDate.currentDate())

        ######################

        # Заполняем таблицу
        self.tableWidget.setColumnCount(3)

        for i in data:
            print(i)


        self.tableWidget.setHorizontalHeaderLabels(["№", "Комплектующие", "Остаток"])
        self.tableWidget.resizeColumnsToContents()
        ###################

        self.ApplyButton.clicked.connect(self.show_information)
        self.CloseButton.clicked.connect(self.close)

    def printing(self):
        pass

    def show_information(self):
        print(self.dateEdit.text())
        a = self.dateEdit.text().split('.')
        day, month, year = [int(i) for i in a]
        #(year, month, day, 23, 59, 59, 0, 0, 0)

    def close(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = UI_Session3("../nti_base.db")
    mainWindow.show()
    sys.exit(app.exec())


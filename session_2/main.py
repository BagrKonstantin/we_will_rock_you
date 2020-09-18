from session_2.ui_session2 import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui, QtCore
import sqlite3
import time


class UI_Session2(QMainWindow, Ui_MainWindow):
    def __init__(self, path):
        super(UI_Session2, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Window 2')
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setHorizontalHeaderLabels(["Комплектующие", "Серийник", "Колличесиво"])
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

        # self.tableWidget

        self.spinBox.setValue(1)
        self.spinBox.setMinimum(1)
        self.spinBox.valueChanged.connect(self.lines)
        # self.ProgressBar.hide()

        self.pushButton.clicked.connect(self.check)
        self.pushButton_2.clicked.connect(self.write)

        # получаем данные из бд
        self.con = sqlite3.connect(path)
        self.cur = self.con.cursor()

        # это названия комплектующих
        self.list_of_details = []
        try:
            for i in self.cur.execute("""Select title from details""").fetchall():
                for j in i:
                    self.list_of_details.append(j)
        except Exception as e:
            print(e)
        for i in self.cur.execute("""Select title from details""").fetchall():
            for j in i:
                self.list_of_details.append(j)
        self.list_of_details.insert(0, '')
        print(self.list_of_details)

        # это названия акамуляторов
        self.list_of_akb = []
        for i in self.cur.execute("""
                            select title from details where category='Аккумуляторные батареи'""").fetchall():
            for j in i:
                self.list_of_akb.append(j)

        #######################

        self.add_row(0)

        # self.tableWidget.cellWidget.currentTextChanged.connect(self.ptint)

        # self.dic = dict()

    # def go(self):
    #     for i in range(100):
    #         self.ProgressBar.setValue(i)
    #         time.sleep(0.025)
    #     self.ProgressBar.hide()

    #     self.timer = QtCore.QBasicTimer()
    #     self.timer.start(100, self)
    #
    # def timerEvent(self, e):
    #
    #     if self.step >= 100:
    #         self.timer.stop()
    #         return
    #
    #     self.step = self.step + 1
    #     self.ProgressBar.setValue(self.step)

    def write(self):
        for i in self.check():
            id_detail = self.cur.execute("""select id from details where title='{}' """.format(i[0])).fetchall()
            self.cur.execute(
                """insert into amount_details (title, amount) values (?, ?)""", (id_detail[0][0], i[1]))

        self.con.commit()
        print("recording was successful")

    def lines(self):
        if (self.tableWidget.rowCount() < self.spinBox.value()) and self.spinBox.value() != 0:
            self.tableWidget.setRowCount(self.spinBox.value())
            for i in range(self.tableWidget.rowCount() - 1, self.spinBox.value()):
                self.add_row(i)
        else:
            if self.spinBox.value() > 0:
                self.tableWidget.setRowCount(self.spinBox.value())
                for i in range(self.tableWidget.rowCount(), self.spinBox.value()):
                    self.add_row(i)

    def ptint(self):
        print(1)

    def add_row(self, i):
        comboBox = QtWidgets.QComboBox()
        self.tableWidget.setItem(i, 1, QTableWidgetItem())
        self.tableWidget.setItem(i, 2, QTableWidgetItem())
        # self.tableWidget.closePersistentEditor(self.tableWidget.item(i, 1))
        self.tableWidget.item(i, 1).setFlags(QtCore.Qt.ItemIsEditable)
        self.tableWidget.item(i, 1).setBackground(QtGui.QColor(120, 120, 120))
        # self.tableWidget.setItem(i, 1, QTableWidgetItem())

        # self.tableWidget.item(i, 1).setFlags(QtCore.Qt.Item)

        # spinbox = QtWidgets.QSpinBox()

        # self.ProgressBar

        # заполняем выпадающее меню
        comboBox.addItems(self.list_of_details)

        self.tableWidget.setCellWidget(i, 0, comboBox)
        self.tableWidget.cellWidget(i, 0).currentTextChanged.connect(lambda: self.unlock(i))

        # self.tableWidget.setCellWidget(i, 2, spinbox)

    def unlock(self, i):
        if self.tableWidget.cellWidget(i, 0).currentText() in self.list_of_akb:
            self.tableWidget.setItem(i, 1, QTableWidgetItem())
        else:
            self.tableWidget.setItem(i, 1, QTableWidgetItem())
            self.tableWidget.item(i, 1).setFlags(QtCore.Qt.ItemIsEditable)

    # def add(self):
    #     self.tableWidget.setRowCount(self.tableWidget.rowCount())
    #     self.add_row(self.tableWidget.rowCount() - 1)
    #     self.tableWidget.Stretch()

    def check(self):
        # self.ProgressBar.show()
        # self.go()
        # print(1)

        # Я закоментировал это, потому что оно мешало коду двигаться дальше

        # if self.lineEdit.text():
        #     print("Ответсвенный:", self.lineEdit.text())
        # else:
        #     return

        supply = []
        # проверка на правильность заполнения таблицы
        try:
            for i in range(self.tableWidget.rowCount()):  # заменил переменную на атрибут объекта
                if self.tableWidget.cellWidget(i, 0).currentText() in self.list_of_akb:
                    if self.tableWidget.item(i, 1).text():
                        if self.tableWidget.item(i, 2).text() == "1":

                            print(self.tableWidget.cellWidget(i, 0).currentText(), self.tableWidget.item(i, 1).text(),
                                  self.tableWidget.item(i, 2).text(), "Штука")

                            supply.append([self.tableWidget.cellWidget(i, 0).currentText(), 1])
                        else:
                            raise AttributeError

                    else:
                        raise AttributeError


                elif self.tableWidget.cellWidget(i, 0).currentText() != "":
                    if self.tableWidget.item(i, 2).text() != "0":
                        supply.append(
                            [self.tableWidget.cellWidget(i, 0).currentText(), int(self.tableWidget.item(i, 2).text())])
                    else:
                        raise AttributeError
            return supply
        except Exception as error:
            print(error.__repr__())

        # print(supply)
        # print("all is fine")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = UI_Session2("../nti_base.db")
    mainWindow.show()
    sys.exit(app.exec())

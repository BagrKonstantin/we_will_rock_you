from test import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui, QtCore
import time


class Loader(QMainWindow, Ui_MainWindow):
    def __init__(self):
        #super(Loader, self).__init__()
        #self.setupUi(self)

        super().__init__()
        self.setupUi(self)

        self.setWindowTitle('Window 1')
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["Комплектующие", "Серийник", "Колличесиво"])
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

        #self.tableWidget

        self.spinBox.setValue(3)
        self.spinBox.valueChanged.connect(self.lines)
        #self.ProgressBar.hide()

        self.pushButton.clicked.connect(self.check)
        self.pushButton_2.clicked.connect(self.write)

        self.n = 3

        self.list = ['АКБ "Сириус-1"', 'АКБ "Пурга-3"', 'АКБ "BreakPower"']




        for i in range(3):
            self.add_row(i)



        #self.tableWidget.cellWidget.currentTextChanged.connect(self.ptint)



        #self.dic = dict()





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
        print("writing..")

    def lines(self):
        if self.n < self.spinBox.value():
            self.tableWidget.setRowCount(self.spinBox.value())
            for i in range(self.n, self.spinBox.value()):
                self.add_row(i)
        else:
            self.tableWidget.setRowCount(self.spinBox.value())
            for i in range(self.n, self.spinBox.value()):
                self.add_row(i)

        self.n = self.spinBox.value()

    def ptint(self):
        print(1)

    def add_row(self, i):
        comboBox = QtWidgets.QComboBox()
        self.tableWidget.setItem(i, 1, QTableWidgetItem())
        self.tableWidget.setItem(i, 2, QTableWidgetItem())
        #self.tableWidget.closePersistentEditor(self.tableWidget.item(i, 1))
        self.tableWidget.item(i, 1).setFlags(QtCore.Qt.ItemIsEditable)
        #self.tableWidget.setItem(i, 1, QTableWidgetItem())

        #self.tableWidget.item(i, 1).setFlags(QtCore.Qt.Item)


        #spinbox = QtWidgets.QSpinBox()

        #self.ProgressBar


        comboBox.addItems(["",
                           'АКБ "Сириус-1"',
                           'Лопасть МК-83 - 100',
                           'Лопасть Аранж',
                           'Полетный контроллер  ПК-17-03',
                           'АКБ "Пурга-3"',
                           'Регулятор хода РХ-10319',
                           'Электромотор ДВИЖ-10.50.2019',
                           'Радиопередатчик "ЭХО-3"',
                           'Плата распределения питания "ПРП 30.04"',
                           'Электромотор ВЕТРЯК',
                           'АКБ "BreakPower"',
                           'Плата распределения питания "ПРП 20.05"',
                           ])
        self.tableWidget.setCellWidget(i, 0, comboBox)
        self.tableWidget.cellWidget(i, 0).currentTextChanged.connect(lambda: self.unlock(i))

        #self.tableWidget.setCellWidget(i, 2, spinbox)

    def unlock(self, i):
        if self.tableWidget.cellWidget(i, 0).currentText() in self.list:
            self.tableWidget.setItem(i, 1, QTableWidgetItem())
        else:
            self.tableWidget.setItem(i, 1, QTableWidgetItem())
            self.tableWidget.item(i, 1).setFlags(QtCore.Qt.ItemIsEditable)


    def add(self):
        self.n += 1

        self.tableWidget.setRowCount(self.n)
        self.add_row(self.n - 1)
        self.tableWidget.Stretch()

    def check(self):
        # self.ProgressBar.show()
        # self.go()
        #print(1)
        #print(self.tableWidget.cellWidget(0, 0).currentText())
        if self.lineEdit.text():
            print("Ответсвенный:", self.lineEdit.text())
        else:
            return
        for i in range(self.n):
            if self.tableWidget.cellWidget(i, 0).currentText() in self.list:
                print(1)
                if self.tableWidget.item(i, 1).text():
                    self.tableWidget.item(i, 1).setBackground(QtGui.QColor(255, 255, 255))
                    if self.tableWidget.item(i, 2).text() == "1":
                        self.tableWidget.item(i, 2).setBackground(QtGui.QColor(255, 255, 255))
                        print(self.tableWidget.cellWidget(i, 0).currentText(), self.tableWidget.item(i, 1).text(), self.tableWidget.item(i, 2).text(), "Штука")


                    else:
                        self.tableWidget.item(i, 2).setBackground(QtGui.QColor(255,0,0))
                        return

                else:

                    self.tableWidget.item(i, 1).setBackground(QtGui.QColor(255, 0, 0))
                    return
            else:
                pass
                # print("not_battery")
        print("all is fine")








if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = Loader()
    mainWindow.show()
    sys.exit(app.exec())
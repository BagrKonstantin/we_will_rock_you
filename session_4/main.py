from session_4.ui_session4 import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui, QtCore
import sqlite3
import time


class UI_Session4(QMainWindow, Ui_MainWindow):
    def __init__(self, path):
        super(UI_Session4, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Window 4')

        self.swap("")

        self.lineEdit.setEnabled(False)
        self.tableWidget_of_orders.setHorizontalHeaderLabels(["№ п.п.", "Дата создания", "Дата изменения состояния", "Состояние", "Общая сумма заявки"])
        self.tableWidget_order.setHorizontalHeaderLabels(["Модель", "Цена", "Колличество"])

        self.list_of_drones = ["", "Шура", "Антон", "Арамис"]
        self.dict_of_drones = {"": 0, "Шура": 10000, "Антон": 12000, "Арамис": 15000}

        self.tableWidget_order.setRowCount(1)
        self.add_row(0)

        for i in range(5):
            self.tableWidget_of_orders.horizontalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        for i in range(3):
            self.tableWidget_order.horizontalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

        self.pushButton_swap.clicked.connect(lambda: self.swap(self.pushButton_swap.text()))

        self.radioButton.clicked.connect(self.change_client)

        self.spinBox.setValue(1)
        self.spinBox.valueChanged.connect(self.lines)

        self.list_of_clients = ["", "Костя", "Саня"]
        self.comboBox.addItems(self.list_of_clients)



    def lines(self):
        if (self.tableWidget_order.rowCount() < self.spinBox.value()) and self.spinBox.value() != 0:
            self.tableWidget_order.setRowCount(self.spinBox.value())
            for i in range(self.tableWidget_order.rowCount() - 1, self.spinBox.value()):
                self.add_row(i)
        else:
            if self.spinBox.value() > 0:
                self.tableWidget_order.setRowCount(self.spinBox.value())
                for i in range(self.tableWidget_order.rowCount(), self.spinBox.value()):
                    self.add_row(i)

    def add_row(self, i):
        comboBox = QtWidgets.QComboBox()
        spinbox = QtWidgets.QSpinBox()
        spinbox.setMinimum(1)

        self.tableWidget_order.setItem(i, 1, QTableWidgetItem())
        self.tableWidget_order.item(i, 1).setText("0")
        self.tableWidget_order.setItem(i, 2, QTableWidgetItem())
        self.tableWidget_order.item(i, 1).setFlags(QtCore.Qt.ItemIsEditable)

        #self.tableWidget_order.item(i, 1).setBackground(QtGui.QColor(120, 120, 120))

        comboBox.addItems(self.list_of_drones)

        self.tableWidget_order.setCellWidget(i, 2, spinbox)

        self.tableWidget_order.setCellWidget(i, 0, comboBox)
        self.tableWidget_order.cellWidget(i, 0).currentTextChanged.connect(lambda: self.set_price(i, self.tableWidget_order.cellWidget(i, 0).currentText()))
        self.tableWidget_order.cellWidget(i, 2).valueChanged.connect(lambda: self.set_price(i, self.tableWidget_order.cellWidget(i, 0).currentText()))

    def set_price(self, i, name):
        self.tableWidget_order.item(i, 1).setText(str(self.dict_of_drones[name] * self.tableWidget_order.cellWidget(i, 2).value()))
        try:
            self.label_2.setText("Цена заказа: {}".format(sum([int(self.tableWidget_order.item(i, 1).text()) for i in range(self.tableWidget_order.rowCount())])))
        except Exception as error:
            print(error)


    def change_client(self):
        if self.radioButton.isChecked():
            self.comboBox.setEnabled(False)
            self.lineEdit.setEnabled(True)
        else:
            self.comboBox.setEnabled(True)
            self.lineEdit.setEnabled(False)

    def swap(self, text):
        if text == "Сделать заказ":
            self.tableWidget_of_orders.hide()

            self.pushButton_swap.setText("Заказы")

            self.tableWidget_order.show()
            self.lineEdit.show()
            self.radioButton.show()
            self.pushButton_commit.show()
            self.label.show()
            self.comboBox.show()
            self.spinBox.show()
            self.label_2.show()

        else:
            self.tableWidget_of_orders.show()

            self.pushButton_swap.setText("Сделать заказ")

            self.tableWidget_order.hide()
            self.lineEdit.hide()
            self.radioButton.hide()
            self.pushButton_commit.hide()
            self.label.hide()
            self.comboBox.hide()
            self.spinBox.hide()
            self.label_2.hide()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = UI_Session4("../nti_base.db")
    mainWindow.show()
    sys.exit(app.exec())

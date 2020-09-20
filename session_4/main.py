from session_4.ui_session4 import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui, QtCore
import sqlite3
import time

print(int(time.time()))


def get_seconds(day, month, year):
    return time.mktime((year, month, day, 23, 59, 59, 0, 0, 0))


class Order():  # класс в котором хранится информация о заказе(надо расширять)
    def __init__(self, num, creation_date, last_change_date, state, price, client_name, licence=True):
        self.num = num  # 1 столбик
        self.creation_date = creation_date
        self.last_change_date = last_change_date
        self.state = state
        self.price = price  # столбик

        self.client_name = client_name
        self.licence = licence  # bool

    def get_info_for_orders_table(self):
        return self.num, self.creation_date, self.last_change_date, self.state, self.price


class UI_Session4(QMainWindow, Ui_MainWindow):
    def __init__(self, path):
        super(UI_Session4, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Window 4')

        self.con = sqlite3.connect(path)
        self.cur = self.con.cursor()

        self.swap("")

        self.lineEdit.setEnabled(False)

        self.list_of_drones = [""]
        self.dict_of_drones = {}
        self.dict_of_drones[''] = 0

        for i in self.cur.execute("""Select title, price  from drones""").fetchall():
            self.list_of_drones.append(i[0])
            self.dict_of_drones[i[0]] = i[1]

        self.tableWidget_of_orders.setHorizontalHeaderLabels(
            ["№ п.п.", "Дата создания", "Дата изменения состояния", "Состояние", "Общая сумма заявки"])
        self.tableWidget_order.setRowCount(1)
        self.add_row_to_order(0)
        self.tableWidget_order.setHorizontalHeaderLabels(["Модель", "Цена", "Колличество"])

        self.list_of_statuses = ["Создана", "Идёт сборка", "Готова к отгрузке", "Запрошено разрешение у ФСБ",
                                 "Анулирована", "Отгружена", "Произвести сборку"]  # бд сюда

        for i in range(3, 5):
            self.tableWidget_of_orders.horizontalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_of_orders.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_of_orders.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_of_orders.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        for i in range(3):
            self.tableWidget_order.horizontalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

        self.tableWidget_of_orders.horizontalHeader().sectionClicked.connect(self.sorting)

        self.pushButton_swap.clicked.connect(lambda: self.swap(self.pushButton_swap.text()))
        self.pushButton_commit.clicked.connect(self.create_order)

        self.radioButton.clicked.connect(self.change_client)

        self.spinBox.setValue(1)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(1000)
        self.spinBox.valueChanged.connect(self.lines)

        self.list_of_client_names = [""]
        for i in self.cur.execute("""select title from customers""").fetchall():
            self.list_of_client_names.append(i[0])
        self.comboBox.addItems(self.list_of_client_names)

        self.list_of_orders = []  # [Order(1, 1600501329, 1600105329, "Создана", 12000, "Костя"),
        #                        Order(2, 1600495329, 1600505329, "Запрошено разрешение у ФСБ", 14000, "Петя",
        #                              licence=False),
        #                        Order(3, 1600405329, 1600405329, "Идет сборка", 14000, "Вася",
        #                              licence=True),
        #                        Order(4, 1600305329, 1600305329, "Анулирована", 14000, "Макс",
        #                              licence=False),
        #                        Order(5, 1600205329, 1600205329, "Готова к отгрузке", 14000, "Слуга народа",
        #                              licence=True)]  # бд сюда

        for i in self.cur.execute("""select * from applications""").fetchall():
            date_creation = time.strftime("%d.%m.%Y", time.gmtime(i[1]))
            last_change_date = time.strftime("%d.%m.%Y", time.gmtime(i[2]))
            customer, licence = \
                self.cur.execute("""select title, license from customers where id = ?""", (i[3],)).fetchall()[0]
            print(i[4])
            status = self.cur.execute("""select title from application_status where id = ?""", (i[4],)).fetchall()[0][0]

            self.list_of_orders.append(Order(i[0], i[1], i[2], status, i[5], customer, licence))
        self.update_orders()

        self.t = 1

    def sorting(self):
        try:
            self.t *= -1
            n = self.tableWidget_of_orders.horizontalHeader().sortIndicatorSection()
            if n == 0:
                self.list_of_orders.sort(key=lambda x: int(x.num) * self.t)
                self.update_orders()
            elif n == 1:
                self.list_of_orders.sort(key=lambda x: int(x.creation_date) * self.t)
                self.update_orders()
            elif n == 2:
                self.list_of_orders.sort(key=lambda x: int(x.last_change_date) * self.t)
                self.update_orders()
            elif n == 3:
                self.list_of_orders.sort(key=lambda x: len(x.state) * self.t)
                self.update_orders()
        except Exception as error:
            print(error)

    def status_changed(self, i):  # изменение статуса заказа отсылает сюда
        print(i)
        try:
            # это пока не работает
            if self.tableWidget_of_orders.cellWidget(i, 3).currentText() == "Готова к отгрузке":
                possible = False # possible хватает деталей на сборку
                if possible: #

                    self.list_of_orders[i].state = self.tableWidget_of_orders.cellWidget(i, 3).currentText()


                    print("update customers set status =(select id from application_status where title = {})".format())
                    # self.cur.execute("update customers set status =(select id from application_status where title = {})".format(
                    #                          self.tableWidget_of_orders.cellWidget(i, 3).currentText()))
                    self.list_of_orders[i].num  # id по которому надо поменять статус в бд
                    self.tableWidget_of_orders.cellWidget(i, 3).currentText()  # статус
                else:
                    self.tableWidget_of_orders.cellWidget(i, 3).setCurrentIndex(
                    self.list_of_statuses.index("Произвести сборку"))
                    QMessageBox.critical(self, "Ошибка", "Недостаточно комплектующих\nНе хватает :", QMessageBox.Ok)
        except Exception as ex:
            print(ex)

    def update_orders(self):  # обновление таблицы заказов
        self.tableWidget_of_orders.setRowCount(len(self.list_of_orders))
        for i in range(len(self.list_of_orders)):
            self.refresh(i)

    def refresh(self, i):
        combobox = QtWidgets.QComboBox()
        combobox.addItems(self.list_of_statuses)

        self.tableWidget_of_orders.setItem(i, 0, QTableWidgetItem())
        self.tableWidget_of_orders.setItem(i, 1, QTableWidgetItem())
        self.tableWidget_of_orders.setItem(i, 2, QTableWidgetItem())
        # self.tableWidget_of_orders.setItem(i, 3, QTableWidgetItem())
        self.tableWidget_of_orders.setItem(i, 4, QTableWidgetItem())

        self.tableWidget_of_orders.item(i, 0).setText(str(self.list_of_orders[i].num))
        self.tableWidget_of_orders.item(i, 1).setText(
            time.strftime("%d.%m.%Y", time.gmtime(self.list_of_orders[i].creation_date)))
        self.tableWidget_of_orders.item(i, 2).setText(
            time.strftime("%d.%m.%Y", time.gmtime(self.list_of_orders[i].last_change_date)))

        self.tableWidget_of_orders.item(i, 4).setText(str(self.list_of_orders[i].price))

        self.tableWidget_of_orders.item(i, 0).setFlags(QtCore.Qt.ItemIsEditable)
        self.tableWidget_of_orders.item(i, 1).setFlags(QtCore.Qt.ItemIsEditable)
        self.tableWidget_of_orders.item(i, 2).setFlags(QtCore.Qt.ItemIsEditable)
        self.tableWidget_of_orders.item(i, 4).setFlags(QtCore.Qt.ItemIsEditable)

        self.tableWidget_of_orders.setCellWidget(i, 3, combobox)

        self.tableWidget_of_orders.cellWidget(i, 3).setCurrentIndex(
            self.list_of_statuses.index(self.list_of_orders[i].state))
        self.tableWidget_of_orders.cellWidget(i, 3).currentTextChanged.connect(lambda: self.status_changed(i))


            # self.tableWidget_of_orders.cellWidget(i, 0).currentTextChanged.connect(
            #     lambda: self.set_price(i, self.tableWidget_order.cellWidget(i, 0).currentText()))
            # self.tableWidget_of_orders.cellWidget(i, 2).valueChanged.connect(
            #     lambda: self.set_price(i, self.tableWidget_order.cellWidget(i, 0).currentText()))

    def create_order(self):  # создание заказа
        if self.radioButton.isChecked():
            self.list_of_orders.append(
                Order(3, int(time.time()), int(time.time()), "Запрошено разрешение у ФСБ", self.label_price.text(),
                      self.lineEdit.text(), licence=False))
            client_name = self.lineEdit.text()

        else:
            self.list_of_orders.append(
                Order(3, int(time.time()), int(time.time()), "Идет сборка", self.label_price.text(),
                      self.comboBox.currentText()))
            client_name = self.comboBox.currentText()

        shopping_dict = {}
        for i in range(self.tableWidget_order.rowCount()):
            if self.tableWidget_order.cellWidget(i, 0).currentText():
                shopping_dict[
                    self.tableWidget_order.cellWidget(i, 0).currentText()] = self.tableWidget_order.cellWidget(i,
                                                                                                               2).value()

        item_list = [time.time(), client_name, shopping_dict, self.label_price.text(),
                     self.radioButton.isChecked()]
        print(item_list)
        # добавляем заказ в бд

        # проверка покупателя
        if item_list[4]:
            self.cur.execute("insert into customers (title) values ( '{}' )".format(item_list[1]))
            customer = self.cur.execute("select id from customers where title = ?", (item_list[1],)).fetchall()
        else:
            customer = self.cur.execute("""select id from customers where title = ?""", (item_list[1],)).fetchall()

        self.cur.execute(
            """insert into applications
             (date_creation, last_change_date, customer, status, total_cost) values (?, ?, ?, 1, ?)""",
            (item_list[0], item_list[0], customer[0][0], item_list[3]))

        id_application = self.cur.execute("""select id from applications where date_creation = ?""",
                                          (item_list[0],)).fetchall()

        # # добавление дронов в список покупок
        for j in item_list[2]:
            self.cur.execute("""insert into shoping_lists (id, drone, amount) values ( ?, ?, ? )""",
                             (id_application[0][0], j, item_list[2][j]))

        self.con.commit()
        self.clean_order_table()
        self.update_orders()
        self.swap("")

    def clean_order_table(self):
        self.lineEdit.clear()
        self.lineEdit.setEnabled(False)
        self.comboBox.setEnabled(True)
        self.radioButton.setChecked(False)
        self.spinBox.setValue(1)
        self.add_row_to_order(0)
        self.comboBox.setCurrentIndex(0)
        self.label_price.setText("0")

    def lines(self):
        n = self.tableWidget_order.rowCount()
        if self.tableWidget_order.rowCount() < self.spinBox.value():
            self.tableWidget_order.setRowCount(self.spinBox.value())
            for i in range(n, self.spinBox.value()):
                self.add_row_to_order(i)
        else:
            self.tableWidget_order.setRowCount(self.spinBox.value())
            # for i in range(n + 1, self.spinBox.value() + 1):
            #     self.add_row(i)

    def add_row_to_order(self, i):
        spinbox = QtWidgets.QSpinBox()
        spinbox.setMinimum(1)
        spinbox.setMaximum(1000)

        combobox = QtWidgets.QComboBox()
        combobox.addItems(self.list_of_drones)

        self.tableWidget_order.setItem(i, 1, QTableWidgetItem())
        self.tableWidget_order.item(i, 1).setText("0")

        self.tableWidget_order.setItem(i, 2, QTableWidgetItem())
        self.tableWidget_order.item(i, 1).setFlags(QtCore.Qt.ItemIsEditable)

        self.tableWidget_order.setCellWidget(i, 2, spinbox)
        self.tableWidget_order.setCellWidget(i, 0, combobox)

        self.tableWidget_order.cellWidget(i, 0).currentTextChanged.connect(
            lambda: self.set_price(i, self.tableWidget_order.cellWidget(i, 0).currentText()))
        self.tableWidget_order.cellWidget(i, 2).valueChanged.connect(
            lambda: self.set_price(i, self.tableWidget_order.cellWidget(i, 0).currentText()))

    def set_price(self, i, name):
        self.tableWidget_order.item(i, 1).setText(
            str(self.dict_of_drones[name] * self.tableWidget_order.cellWidget(i, 2).value()))
        try:
            self.label_price.setText(str(
                sum([int(self.tableWidget_order.item(i, 1).text()) for i in range(self.tableWidget_order.rowCount())])))
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
            self.label_price.show()

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
            self.label_price.hide()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = UI_Session4("../nti_base.db")
    mainWindow.show()
    sys.exit(app.exec())

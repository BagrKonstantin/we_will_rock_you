# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1013, 710)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget_of_orders = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_of_orders.setEnabled(True)
        self.tableWidget_of_orders.setGeometry(QtCore.QRect(110, 90, 811, 511))
        self.tableWidget_of_orders.setColumnCount(5)
        self.tableWidget_of_orders.setObjectName("tableWidget_of_orders")
        self.tableWidget_of_orders.setRowCount(0)
        self.pushButton_swap = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_swap.setGeometry(QtCore.QRect(810, 30, 111, 23))
        self.pushButton_swap.setObjectName("pushButton_swap")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(240, 30, 341, 22))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 30, 131, 21))
        self.label.setObjectName("label")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(110, 60, 131, 17))
        self.radioButton.setObjectName("radioButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(240, 60, 341, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_commit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_commit.setGeometry(QtCore.QRect(850, 610, 75, 23))
        self.pushButton_commit.setObjectName("pushButton_commit")
        self.tableWidget_order = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_order.setGeometry(QtCore.QRect(110, 90, 811, 511))
        self.tableWidget_order.setColumnCount(3)
        self.tableWidget_order.setObjectName("tableWidget_order")
        self.tableWidget_order.setRowCount(0)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(880, 60, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(620, 610, 71, 21))
        self.label_2.setObjectName("label_2")
        self.label_price = QtWidgets.QLabel(self.centralwidget)
        self.label_price.setGeometry(QtCore.QRect(690, 610, 151, 21))
        self.label_price.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_price.setObjectName("label_price")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1013, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_swap.setText(_translate("MainWindow", "Сделать заказ"))
        self.label.setText(_translate("MainWindow", "Покупатель"))
        self.radioButton.setText(_translate("MainWindow", "Новый покупатель"))
        self.pushButton_commit.setText(_translate("MainWindow", "Заказать"))
        self.label_2.setText(_translate("MainWindow", "Цена заказа:"))
        self.label_price.setText(_translate("MainWindow", "0"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(506, 469)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 370, 195, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ApplyButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.ApplyButton.setObjectName("ApplyButton")
        self.horizontalLayout_2.addWidget(self.ApplyButton)
        self.CloseButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.CloseButton.setObjectName("CloseButton")
        self.horizontalLayout_2.addWidget(self.CloseButton)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 110, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 170, 471, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.printing = QtWidgets.QPushButton(Dialog)
        self.printing.setGeometry(QtCore.QRect(390, 400, 93, 28))
        self.printing.setObjectName("printing")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 40, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ApplyButton.setText(_translate("Dialog", "Выполнить"))
        self.CloseButton.setText(_translate("Dialog", "Закрыть"))
        self.label.setText(_translate("Dialog", "Показывать остатки на:"))
        self.printing.setText(_translate("Dialog", "Печать"))
        self.label_2.setText(_translate("Dialog", "Остатки комплектующих"))

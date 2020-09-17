from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))


class Window(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.dateEdit = QtWidgets.QDateEdit(self)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateEdit.setFont(font)
        self.dateEdit.setCalendarPopup(True)                            # +++
        self.dateEdit.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateEdit.setGeometry(QtCore.QRect(220, 31, 133, 20))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = Window() #QtWidgets.QDialog()
#    ui = Ui_Dialog()
#    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

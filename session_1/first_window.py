from session_1.load_window import Ui_MainWindow
from session_1.main import load_tech_cards, load_drones, load_details
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets


class Loader(QMainWindow, Ui_MainWindow):
    def __init__(self, path):
        super(Loader, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Window 1')

        self.path = path

        self.load_button_details.clicked.connect(self.dialog_for_load_details)
        self.load_button_drones.clicked.connect(self.dialog_for_load_drones)
        self.load_button_tech_cards.clicked.connect(self.dialog_for_load_tech_cards)
        self.download_all.clicked.connect(self.load_all_files)

    def dialog_for_load_details(self):
        file_path = QFileDialog.getOpenFileName(self, "Select file", "", "Files (*.xlsx)")
        self.line_details_download.setText(file_path[0])

    def dialog_for_load_drones(self):
        file_path = QFileDialog.getOpenFileName(self, "Select file", "", "Files (*.xlsx)")
        self.line_drons_download.setText(file_path[0])

    def dialog_for_load_tech_cards(self):
        file_path = QFileDialog.getOpenFileName(self, "Select file", "", "Files (*.xlsx)")
        self.line_card_download.setText(file_path[0])

    def load_all_files(self):
        if len(self.line_details_download.displayText()) and len(self.line_drons_download.displayText()) and len(
                self.line_card_download.displayText()) > 0:
            load_details(self.line_details_download.displayText(), self.path)
            load_drones(self.line_drons_download.displayText(), self.path)
            load_tech_cards(self.line_card_download.displayText(), self.path)
        else:
            error = QMessageBox.question(self, '',
                                             "Загружены не все файлы", QMessageBox.Ok)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = Loader("../nti_base.db")
    mainWindow.show()
    sys.exit(app.exec())

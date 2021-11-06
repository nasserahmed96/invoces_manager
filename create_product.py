import sys
from PyQt5.QtWidgets import (QApplication, QMessageBox, QMainWindow)
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

from python_forms.createProduct_GUI import Ui_createProductWindow
from helpers import get_table_data

from main_form import MainForm


class CreateProduct(QMainWindow):
    def __init__(self):
        super(CreateProduct, self).__init__()
        self.ui = Ui_createProductWindow()
        self.ui.setupUi(self)
        self.initialize_db()
        self.initializeUI()
        self.show()

    def fill_combo_boxes(self):
        """
        Fill the combo box from get_table_data items which returns a dictionary
        that its keys act like text for combo box
        """
        self.categories = get_table_data("categories")
        self.brands = get_table_data("brands")
        self.ui.categoryComboBox.addItems(self.categories.keys())
        self.ui.brandComboBox.addItems(self.brands)

    def initialize_validators(self):
        """
        Setup the validators with the required regex
        :return:
        """
        arabic_text_regex = QRegExp("^[a-zA-Z\u0621-\u064A\u0660-\u0669\s\,\:\;0-9]+$")
        text_regex = QRegExp("^[a-zA-Z\s\,\:\;0-9]+$")
        self.arabic_text_validator = QRegExpValidator(arabic_text_regex)
        self.text_validator = QRegExpValidator(text_regex)

    def initializeUI(self):
        self.mandatory_widgets = [self.ui.nameLineEdit, self.ui.descriptionLineEdit, self.ui.barcodeLineEdit]
        self.fill_combo_boxes()
        self.ui.categoryComboBox.setCurrentIndex(1)
        self.ui.brandComboBox.setCurrentIndex(1)
        self.initialize_validators()
        self.assign_validators()
        self.connect_signals_slots()

    def assign_validators(self):
        """
        Assign validators for each widget
        :return:
        """
        self.ui.nameLineEdit.setValidator(self.arabic_text_validator)
        self.ui.descriptionLineEdit.setValidator(self.arabic_text_validator)
        self.ui.barcodeLineEdit.setValidator(self.text_validator)

    def connect_signals_slots(self):
        self.ui.save_btn.clicked.connect(self.save)


    def initialize_db(self):
        database = QSqlDatabase.addDatabase("QSQLITE")
        database.setDatabaseName("clear_vision.db")
        if not database.open():
            print("Unable to open database")
            sys.exit(1)

    def validate_form(self):
        """
        Iterate over all the mandatory field and check if it has a valid data or not
        :param widgets:
        :return:
        """
        for widget in self.mandatory_widgets:
            if widget.text() == '':
                QMessageBox.information(self, 'error', f"{widget.placeholderText()} is a mandatory field")
                return False
        return True

    def build_insert_query(self, table_name, cols):
        cols_values = "VALUES ("
        cols_names = ""
        query = f"INSERT INTO {table_name}("
        for col_name in cols:
            cols_names += col_name + ","
            cols_values += f":{col_name},"

        query += f"{cols_names[:-1]}) {cols_values[:-1]})"
        return query

    def save(self):
        if not self.validate_form():
            QMessageBox.information(self, 'Error', 'Please fill all fields')
            return

        query = QSqlQuery()
        values = {"name": self.ui.nameLineEdit.text(),
                  "description": self.ui.descriptionLineEdit.text(),
                  "barcode": self.ui.barcodeLineEdit.text(),
                  "price": self.ui.priceDoubleSpinBox.text(),
                  "quantity": self.ui.quantitySpinBox.text(),
                  "notes": self.ui.notesLineEdit.text(),
                  "category": self.categories[self.ui.categoryComboBox.currentText()],
                  "brand": self.brands[self.ui.brandComboBox.currentText()]}
        query.prepare(self.build_insert_query("products", values.keys()))
        query.exec_()
        errors = query.lastError().text()
        if errors:
            print("Error: ", errors)
        else:
            QMessageBox.information(self, "Success", "Saved new product")

    def bind_values(self, query, values):
            [query.bindValue(f':{value}', values[value]) for value in values.keys()]

    def closeEvent(self, event):
        quit_msg = "Are you sure you want to exit the program?"
        reply = QMessageBox.question(self, 'Message',
                                           quit_msg, QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CreateProduct()
    sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import (QApplication, QMessageBox, QMainWindow)
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from python_forms.createProduct_GUI import Ui_createProductWindow
from helpers import get_table_data


class CreateForm(QMainWindow):
    """
    To do
    If there is any other forms, please generalize this and put it in MainForm
    """
    def __init__(self, table_name):
        super(CreateForm, self).__init__()
        self.ui = Ui_createProductWindow()
        self.ui.setupUi(self)
        self.table_name = table_name
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

    def set_mandatory_widgets(self, mandatory_widgets):
        self.mandatory_widgets = mandatory_widgets

    def add_mandatory_widget(self, mandatory_widget):
        self.mandatory_widgets.append(mandatory_widget)

    def remove_mandatory_widget(self, mandatory_widget):
        self.mandatory_widgets.remove(mandatory_widget)

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
        pass

    def connect_signals_slots(self):
        pass


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

    def build_insert_query(self, cols):
        cols_values = "VALUES ("
        cols_names = ""
        query = f"INSERT INTO {self.table_name}("
        for col_name in cols:
            cols_names += col_name + ","
            cols_values += f":{col_name},"

        query += f"{cols_names[:-1]}) {cols_values[:-1]})"
        return query

    def save(self, cols_values):
        if not self.validate_form():
            QMessageBox.information(self, 'Error', 'Please fill all fields')
            return

        query = QSqlQuery()

        query.prepare(self.build_insert_query(cols_values.keys()))
        query.exec_()
        errors = query.lastError().text()
        print("Error: ", errors) if errors else QMessageBox.information(self, "Success", "Saved new product")


    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                           "Are you sure you want to exit the program?", QMessageBox.Yes, QMessageBox.No)

        event.accept() if reply == QMessageBox.Yes else event.ignore()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CreateForm()
    sys.exit(app.exec_())

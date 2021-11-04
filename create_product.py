import sys, csv, re
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMessageBox, QWidget)
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from python_forms.createProduct_GUI import Ui_createProductWindow
from helpers import encrypt_text, get_table_data
from MainForm import MainForm


class CreateProduct(MainForm):
    def __init__(self):
        super(CreateProduct, self).__init__()
        self.ui = Ui_createProductWindow()
        self.ui.setupUi(self)
        self.initialize_db()
        self.initializeUI()
        self.validation_widgets = []
        self.validation_error = False
        """
        Fill the combo box from get_table_data items which returns a dictionary 
        that its keys act like text for combo box
        """
        self.categories = get_table_data("categories")
        self.brands = get_table_data("brands")
        self.ui.categoryComboBox.addItems(self.categories.keys())
        self.ui.brandComboBox.addItems(self.brands)
        self.show()

    def initializeUI(self):
        self.ui.save_btn.clicked.connect(self.save)
        self.ui.clear_btn.clicked.connect(self.clear_validation_errors)

    def initialize_db(self):
        database = QSqlDatabase.addDatabase("QSQLITE")
        database.setDatabaseName("clear_vision.db")
        if not database.open():
            print("Unable to open database")
            sys.exit(1)

    def clear_validation_errors(self):
        """
        Clear all validation colors and tool tips that appeared, mainly it clears the password fields, but if widgets
        are provided it clears it too.
        :return:
        """
        for widget in self.validation_widgets:
            widget["widget"].setStyleSheet("")

    def save(self):
        query = QSqlQuery()
        query.prepare("""
                INSERT INTO products(name, description, barcode, price, quantity, notes, category, brand)  
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """)
        """
        Append widgets to be validated
        """
        self.append_validation_widget(self.validation_widgets, self.ui.nameLineEdit, "text")
        self.append_validation_widget(self.validation_widgets, self.ui.descriptionLineEdit, "text")
        self.append_validation_widget(self.validation_widgets, self.ui.barcodeLineEdit, "text")
        self.append_validation_widget(self.validation_widgets, self.ui.notesLineEdit, "text")
        self.validate_form(self.validation_widgets)

        if self.validation_error:
            for widget in self.validation_widgets:
                if "error" in widget:
                    QMessageBox.information(self, "validation error", widget["error"])
            return

        self.bind_values(query)
        query.exec_()
        errors = query.lastError().text()
        if errors:
            print("Error: ", errors)
        else:
            QMessageBox.information(self, "Success", "Saved new product")

    def bind_values(self, query):
        """name, description, barcode, price, quantity, notes, category, brand"""
        query.addBindValue(self.ui.nameLineEdit.text())
        query.addBindValue(self.ui.descriptionLineEdit.text())
        query.addBindValue(self.ui.barcodeLineEdit.text())
        query.addBindValue(self.ui.priceDoubleSpinBox.text())
        query.addBindValue(self.ui.quantitySpinBox.text())
        query.addBindValue(self.ui.notesLineEdit.text())
        query.addBindValue(self.categories[self.ui.categoryComboBox.currentText()])
        query.addBindValue(self.brands[self.ui.brandComboBox.currentText()])

    def append_validation_widget(self, widgets:list, widget:QWidget, regex:str):
        """
        Append the widget I want to validate, along side with required regex
        :param widgets:
        :param widget:
        :param regex:
        :return: It doesn't return any thing, it just fills the widgets list
        """
        widget_dict = dict()
        widget_dict["widget"] = widget
        widget_dict["regex"] = regex
        widgets.append(widget_dict)

    def validate_form(self, widgets:list):
        try:
            """
            Validate with widgets in widgets list
            :param widgets: A list of dictionaries
            :return: If an error detected, it sets the validation_error flag to True, the user should check for this flag
            after calling the function
            """
            regex = dict()
            regex["text"] = re.compile("^[a-zA-Z\u0621-\u064A\u0660-\u0669\s\,\:\;0-9]*$")
            regex["name"] = re.compile("^[a-zA-Z\u0621-\u064A]+[a-zA-Z\u0621-\u064A]$")
            regex["phone_number"] = re.compile("^(\+[0-9]{1,3}){0,1}[0-9]{1,13}")
            regex["email"] = re.compile("[a-zA-Z\.1-9\-\\\/\_]*@[A-Za-z]+(\.[a-zA-Z]+)*[a-zA-Z]$")
            for widget in widgets:
                if not regex[widget["regex"]].match(widget["widget"].text()):
                    widget["error"] = "Not a valid: " + widget["widget"].placeholderText()
                    widget["widget"].setStyleSheet("""background-color: red;""")
                    self.validation_error = True
        except KeyError as e:
            print("Unsupported regex: ", e)


    def check_password_confirm(self):
        if self.ui.passwordLineEdit.text() != self.ui.confirmPasswordLineEdit.text():
            return False
        return True

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CreateProduct()
    sys.exit(app.exec_())

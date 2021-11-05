import sys
from PyQt5.QtWidgets import (QApplication, QMessageBox)
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from python_forms.createProduct_GUI import Ui_createProductWindow
from helpers import get_table_data
from main_form import MainForm


class CreateProduct(MainForm):
    def __init__(self):
        super(CreateProduct, self).__init__()
        self.ui = Ui_createProductWindow()
        self.ui.setupUi(self)
        self.initialize_db()
        self.initializeUI()
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

        error_widgets = self.validate_form(self.validation_widgets)
        if error_widgets:
            for widget in error_widgets:
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


    def check_password_confirm(self):
        if self.ui.passwordLineEdit.text() != self.ui.confirmPasswordLineEdit.text():
            return False
        return True

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CreateProduct()
    sys.exit(app.exec_())

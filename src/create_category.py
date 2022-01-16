import sys,re
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMessageBox, QLineEdit)
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from python_forms.createCategory_GUI import Ui_createCategoryWindow
from src.Models.CategoriesTableModel import CategoriesTableModel
from src.DataObjects.Brand import Brand


class CreateCategory(QMainWindow):
    def __init__(self, parent=None):
        super(CreateCategory, self).__init__(parent)
        self.ui = Ui_createCategoryWindow()
        self.ui.setupUi(self)
        self.model = CategoriesTableModel()
        self.initialize_ui()
        self.connect_signals_slots()
        self.validation_widgets = []
        self.validation_error = False
        #The sum of the valid inputs, add 1 to current_valid_inputs and compare it against this number
        self.valid_inputs = 2
        self.current_valid_inputs = 0
        """
        Fill the combo box from get_table_data items which returns a dictionary 
        that its keys act like text for combo box
        """
        self.initialize_validators()
        self.assign_validators()
        self.assign_mandatory_fields()
        self.assign_unique_fields()
        self.assign_labels()
        self.show()

    def initialize_ui(self):
        self.ui.nameLineEdit.set_database_attributes('name', 'categories')
        self.ui.descriptionLineEdit.set_database_attributes('description', 'categories')

    def connect_signals_slots(self):
        self.ui.save_btn.clicked.connect(self.save)

    def assign_labels(self):
        self.ui.nameLineEdit.set_label(self.ui.nameLabelInfo)
        self.ui.descriptionLineEdit.set_label(self.ui.descriptionLabelInfo)

    def assign_validators(self):
        self.ui.nameLineEdit.setValidator(self.arabic_text_validator)
        self.ui.descriptionLineEdit.setValidator(self.arabic_text_validator)

    def initialize_validators(self):
        """
        Setup the validators with the required regex
        :return:
        """
        arabic_text_regex = QRegExp("^[a-zA-Z\u0621-\u064A\u0660-\u0669\s\,\:\;0-9]+$")
        arabic_name_regex = QRegExp("^[a-zA-Z]+$|^[\u0621-\u064A]+$")
        text_regex = QRegExp("^[a-zA-Z\s\,\:\;0-9]+$")
        phone_number_regex = QRegExp("^(\+[0-9]{1,3}){0,1}([0-9]{11,13})$")
        email_regex = QRegExp("^[a-zA-Z\.1-9\-\\\/\_]+@[A-Za-z]+(\.[a-zA-Z]+)*[a-zA-Z]$")
        self.arabic_text_validator = QRegExpValidator(arabic_text_regex)
        self.arabic_name_validator = QRegExpValidator(arabic_name_regex)
        self.text_validator = QRegExpValidator(text_regex)
        self.phone_number_validator = QRegExpValidator(phone_number_regex)
        self.email_validator = QRegExpValidator(email_regex)

    def assign_mandatory_fields(self):
        self.ui.nameLineEdit.set_mandatory(True)

    def assign_unique_fields(self):
        self.ui.nameLineEdit.set_unique(True)

    def prepare_category(self):
        columns = dict()
        for widget in self.ui.fieldsLayout.parentWidget().findChildren(QLineEdit):
            columns[widget.column_name] = widget.text()
        return Brand(name=columns['name'], description=columns['description'])

    def save(self):
        """
        """
        self.current_valid_inputs = sum([widget.is_valid() for widget in
                                         self.ui.fieldsLayout.parentWidget().findChildren(QLineEdit)])
        if not self.valid_inputs == self.current_valid_inputs:
            QMessageBox.information(self, 'Validation error', 'Please enter valid fields')
            return
        QMessageBox.information(self, 'Error while saving', 'An error has occurred while saving to DB') if not self.model.save(self.prepare_category()) else QMessageBox.information(self, 'Save', 'The item has been saved')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CreateCategory()
    window.show()
    sys.exit(app.exec_())

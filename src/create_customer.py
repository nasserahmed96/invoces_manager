import sys,re
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMessageBox, QLineEdit)
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from python_forms.createCustomer_GUI import Ui_createCustomerWindow
from src.Models.CustomersTableModel import CustomerTableModel
from src.DataObjects.User import User
from src.DataObjects.Customer import Customer


class CreateCustomer(QMainWindow):
    def __init__(self, parent=None):
        super(CreateCustomer, self).__init__(parent)
        self.ui = Ui_createCustomerWindow()
        self.ui.setupUi(self)
        self.model = CustomerTableModel()
        self.initializeUI()
        self.connect_signals_slots()
        self.validation_widgets = []
        self.validation_error = False
        #The sum of the valid inputs, add 1 to current_valid_inputs and compare it against this number
        self.valid_inputs = 6
        self.current_valid_inputs = 0
        """
        Fill the combo box from get_table_data items which returns a dictionary 
        that its keys act like text for combo box
        """
        self.initialize_validators()
        self.assign_validators()
        self.assign_mandatory_fields()
        self.assign_labels()
        self.show()

    def initializeUI(self):
        self.ui.firstNameLineEdit.set_database_attributes('first_name', 'employees')
        self.ui.middleNameLineEdit.set_database_attributes('middle_name', 'employees')
        self.ui.lastNameLineEdit.set_database_attributes('last_name', 'employees')
        self.ui.phoneNumberLineEdit.set_database_attributes('phone_number', 'employees')
        self.ui.emailLineEdit.set_database_attributes('email', 'employees')
        self.ui.addressLineEdit.set_database_attributes('address', 'employees')

    def connect_signals_slots(self):
        self.ui.save_btn.clicked.connect(self.save)

    def assign_labels(self):
        self.ui.firstNameLineEdit.set_label(self.ui.firstNameLabelInfo)
        self.ui.middleNameLineEdit.set_label(self.ui.middleNameLabelInfo)
        self.ui.lastNameLineEdit.set_label(self.ui.lastNameLabelInfo)
        self.ui.phoneNumberLineEdit.set_label(self.ui.phoneNumberLabelInfo)
        self.ui.emailLineEdit.set_label(self.ui.emailLabelInfo)

    def assign_validators(self):
        self.ui.firstNameLineEdit.setValidator(self.arabic_name_validator)
        self.ui.middleNameLineEdit.setValidator(self.arabic_name_validator)
        self.ui.lastNameLineEdit.setValidator(self.arabic_name_validator)
        self.ui.phoneNumberLineEdit.setValidator(self.phone_number_validator)
        self.ui.addressLineEdit.setValidator(self.arabic_text_validator)
        self.ui.emailLineEdit.setValidator(self.email_validator)

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
        self.ui.firstNameLineEdit.set_mandatory(True)
        self.ui.lastNameLineEdit.set_mandatory(True)
        self.ui.phoneNumberLineEdit.set_mandatory(True)


    def prepare_customer(self):
        gender = {'gender': self.ui.genderComboBox.currentText()}
        columns = dict()
        for widget in self.ui.basicInformationLayout.parentWidget().findChildren(QLineEdit):
            columns[widget.column_name] = widget.text()
        columns.update(gender)
        user = User(first_name=columns['first_name'],
                    middle_name=columns['middle_name'],
                    last_name=columns['last_name'],
                    phone_number=columns['phone_number'],
                    email=columns['email'],
                    address=columns['address'],
                    gender=columns['gender'])
        return Customer(user=user)

    def save(self):
        """
        """
        self.current_valid_inputs = sum([widget.is_valid() for widget in
                                         self.ui.basicInformationLayout.parentWidget().findChildren(QLineEdit)])
        if self.current_valid_inputs != self.valid_inputs:
            QMessageBox.information(self, "validation error", 'Invalid input')
            return
        QMessageBox.information(self, 'Error while saving', 'An error has occurred while saving to DB') if not self.model.save(self.prepare_customer()) else QMessageBox.information(self, 'Save', 'The item has been saved')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CreateCustomer()
    sys.exit(app.exec_())

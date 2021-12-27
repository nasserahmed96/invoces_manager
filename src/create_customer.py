import sys
from PyQt5.QtWidgets import QApplication
from CreateForm import CreateForm
from python_forms.createCustomer_GUI import Ui_createCustomerWindow


class CreateCustomer(CreateForm):
    def __init__(self):
        super(CreateCustomer, self).__init__('customers', Ui_createCustomerWindow())

    def initializeUI(self):
        self.set_mandatory_widgets([self.ui.firstNameLineEdit, self.ui.lastNameLineEdit, self.ui.phoneNumberLineEdit])
        self.initialize_validators()
        self.assign_validators()
        self.connect_signals_slots()

    def assign_validators(self):
        """
        Assign validators for each widget
        :return:
        """
        self.ui.firstNameLineEdit.setValidator(self.arabic_name_validator)
        self.ui.middleNameLineEdit.setValidator(self.arabic_text_validator)
        self.ui.lastNameLineEdit.setValidator(self.arabic_text_validator)
        self.ui.phoneNumberLineEdit.setValidator(self.phone_number_validator)
        self.ui.emailLineEdit.setValidator(self.email_validator)

    def connect_signals_slots(self):
        self.ui.save_btn.clicked.connect(self.before_save)

    def before_save(self):
        cols_values = {'parent_table': {
            'first_name': self.ui.firstNameLineEdit.text(),
            'middle_name': self.ui.middleNameLineEdit.text(),
            'last_name': self.ui.lastNameLineEdit.text(),
            'email': self.ui.emailLineEdit.text(),
            'address': self.ui.addressLineEdit.text(),
            'phone_number': self.ui.phoneNumberLineEdit.text(),
            'gender': self.ui.genderComboBox.currentText()
        },
        'child_table': {}
        }
        self.save_one_to_one('users', 'customers', cols_values, 'user_id')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CreateCustomer()
    sys.exit(app.exec_())

import sys, csv, re
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMessageBox, QWidget)
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from python_forms.createEmployee_GUI import Ui_createEmployeeWindow
from helpers import encrypt_text, get_table_data


class CreateEmployee(QMainWindow):
    def __init__(self):
        super(CreateEmployee, self).__init__()
        self.ui = Ui_createEmployeeWindow()
        self.ui.setupUi(self)
        self.initialize_db()
        self.initializeUI()
        self.validation_widgets = []
        self.validation_error = False
        """
        Fill the combo box from get_table_data items which returns a dictionary 
        that its keys act like text for combo box
        """
        self.job_titles = get_table_data("job_titles")
        self.ui.jobTitleComboBox.addItems(self.job_titles.keys())
        self.show()

    def initializeUI(self):
        self.ui.save_btn.clicked.connect(self.save)
        self.ui.clear_btn.clicked.connect(self.clear_validation_errors)

    def initialize_db(self):
        database = QSqlDatabase.addDatabase("QSQLITE")
        database.setDatabaseName("")
        if not database.open():
            print("Unable to open database")
            sys.exit(1)

    def clear_validation_errors(self):
        """
        Clear all validation colors and tool tips that appeared, mainly it clears the password fields, but if widgets
        are provided it clears it too.
        :return:
        """
        self.ui.passwordLineEdit.setStyleSheet("")
        self.ui.confirmPasswordLineEdit.setStyleSheet("")
        for widget in self.validation_widgets:
            widget["widget"].setStyleSheet("")

    def save(self):
        query = QSqlQuery()
        query.prepare("""
                INSERT INTO users(first_name, middle_name, last_name, email, address, phone_number, gender, 
                password) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """)

        self.append_validation_widget(self.validation_widgets, self.ui.firstNameLineEdit, "name")
        self.append_validation_widget(self.validation_widgets, self.ui.middleNameLineEdit, "name")
        self.append_validation_widget(self.validation_widgets, self.ui.lastNameLineEdit, "name")
        self.append_validation_widget(self.validation_widgets, self.ui.emailLineEdit, "email")
        self.append_validation_widget(self.validation_widgets, self.ui.phoneNumberLineEdit, "phone_number")

        self.validate_form(self.validation_widgets)
        if self.validation_error:
            for widget in self.validation_widgets:
                if "error" in widget:
                    QMessageBox.information(self, "validation error", widget["error"])
            return

        if not self.check_password_confirm():
            QMessageBox.information(self, "Form validation", "Password doesn't match",
                                    QMessageBox.Ok, QMessageBox.Ok)
            self.ui.passwordLineEdit.setStyleSheet("background-color: red;")
            self.ui.confirmPasswordLineEdit.setStyleSheet("background-color: red;")
            return
        self.bind_values(query)
        query.exec_()
        errors = query.lastError().text()
        if errors:
            print("Error: ", errors)
        else:
            print("Saved new user successfully")
            query.prepare(
            """INSERT INTO employees(user_id, job_title, username) VALUES (?, ?, ?)
            """)
            query.addBindValue(query.lastInsertId())
            query.addBindValue(self.job_titles[self.ui.jobTitleComboBox.currentText()])
            query.addBindValue(self.ui.userNameLineEdit.text())
            query.exec_()
            print(query.lastError().text())

    def bind_values(self, query):
        query.addBindValue(self.ui.firstNameLineEdit.text())
        query.addBindValue(self.ui.middleNameLineEdit.text())
        query.addBindValue(self.ui.lastNameLineEdit.text())
        query.addBindValue(self.ui.emailLineEdit.text())
        query.addBindValue(self.ui.addressLineEdit.text())
        query.addBindValue(self.ui.phoneNumberLineEdit.text())
        query.addBindValue(self.ui.genderComboBox.currentText())
        query.addBindValue(encrypt_text(self.ui.passwordLineEdit.text()))

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
        """
        Validate with widgets in widgets list
        :param widgets: A list of dictionaries
        :return: If an error detected, it sets the validation_error flag to True, the user should check for this flag
        after calling the function
        """
        regex = dict()
        regex["name"] = re.compile("^[a-zA-Z]+[a-zA-Z]$")
        regex["phone_number"] = re.compile("^(\+[0-9]{1,3}){0,1}[0-9]{1,13}")
        regex["email"] = re.compile("[a-zA-Z\.1-9\-\\\/\_]*@[A-Za-z]+(\.[a-zA-Z]+)*[a-zA-Z]$")
        for widget in widgets:
            if not regex[widget["regex"]].match(widget["widget"].text()):

                widget["error"] = "Not a valid: " + widget["widget"].placeholderText()
                widget["widget"].setStyleSheet("""background-color: red;""")
                self.validation_error = True


    def check_password_confirm(self):
        if self.ui.passwordLineEdit.text() != self.ui.confirmPasswordLineEdit.text():
            return False
        return True

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CreateEmployee()
    sys.exit(app.exec_())

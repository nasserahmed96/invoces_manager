import re
import sys
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QMessageBox
from PyQt5.QtSql import QSqlQuery, QSqlDatabase
from python_forms.createCategory_GUI import Ui_createCategoryFrom


class CreateCategory(QWidget):
    def __init__(self):
        super(CreateCategory, self).__init__()
        self.ui = Ui_createCategoryFrom()
        self.ui.setupUi(self)
        self.initialize_db()
        self.initializeUI()
        self.validation_widgets = []
        self.validation_error = False

    def initializeUI(self):
            self.ui.save_btn.clicked.connect(self.save)

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
        self.ui.name_line_edit.setStyleSheet("")
        self.ui.description_line_edit.setStyleSheet("")
        for widget in self.validation_widgets:
            widget["widget"].setStyleSheet("")

    def save(self):
        query = QSqlQuery()
        query.prepare("""
                    INSERT INTO categories(name, description) 
                    VALUES (?, ?)
                    """)
        self.append_validation_widget(self.validation_widgets, self.ui.name_line_edit, "text")
        self.append_validation_widget(self.validation_widgets, self.ui.description_line_edit, "text")
        self.validate_form(self.validation_widgets)

        if self.validation_error:
            for widget in self.validation_widgets:
                if "error" in widget:
                    QMessageBox.information(self, "validation error", widget["error"])
            return

        self.bind_values(query)
        query.exec_()
        errors = query.lastError().number()
        if errors and errors != -1:
            print("Errors: ", errors)
            QMessageBox.information(self, "Failed", self.error_human_mapping(errors))
        else:
            QMessageBox.information(self, "Success", "Saved new category successfully")

    def error_human_mapping(self, number: int):
        """
        Get the human readable form of the error number to be viewed to the user
        :param number:
        :return: A string containing a user friendly message error
        """
        try:
            errors = dict()
            errors["19"] = "This entity already exists in the database"
            return errors[str(number)]
        except KeyError:
            QMessageBox.information(self, "Database error", "Unknown error")
            return None

    def bind_values(self, query):
        query.addBindValue(self.ui.name_line_edit.text())
        query.addBindValue(self.ui.description_line_edit.text())

    def append_validation_widget(self, widgets: list, widget: QWidget, regex: str):
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

    def validate_form(self, widgets: list):
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

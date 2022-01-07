import sys
from PyQt5.QtWidgets import (QVBoxLayout, QApplication, QMessageBox, QMainWindow, QLabel, QToolTip)
from PyQt5.QtCore import QRegExp, QPoint
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from helpers import show_validation_error
import config


class CreateForm(QMainWindow):
    """
    To do
    If there is any other forms, please generalize this and put it in MainForm
    """
    def __init__(self, table_name, ui_class):
        super(CreateForm, self).__init__()
        self.table_name = table_name
        self.ui = ui_class
        self.ui.setupUi(self)
        self.initialize_db()
        self.initializeUI()
        self.show()


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


    def set_mandatory_widgets(self, mandatory_widgets):
        self.mandatory_widgets = mandatory_widgets

    def add_mandatory_widget(self, mandatory_widget):
        self.mandatory_widgets.append(mandatory_widget)

    def remove_mandatory_widget(self, mandatory_widget):
        self.mandatory_widgets.remove(mandatory_widget)

    def initializeUI(self):
      pass

    def assign_validators(self):
        """
        Assign validators for each widget
        :return:
        """
        pass

    def connect_signals_slots(self):
        pass

    def before_save(self):
        pass

    def initialize_db(self):
        database = QSqlDatabase.addDatabase("QSQLITE")
        database.setDatabaseName('')
        if not database.open():
            print("Unable to open database")
            sys.exit(1)

    def validate_mandatory_widgets(self):
        """
        Iterate over all the mandatory field and check if it has a valid data or not
        :param widgets:
        :return:
        """
        for widget in self.mandatory_widgets:
            if widget.text() == '' or not widget.validator().validate(widget.text(), 0)[0] == widget.validator().Acceptable:
                show_validation_error(widget)
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

    def set_table_name(self, table_name):
        self.table_name = table_name

    def get_table_name(self):
        return self.table_name

    def save_one_to_one(self, parent_table_name, child_table_name, cols_values, parent_table_col):
        """
        This function create row for the first table and get the last inserted ID, then create the row for child table
        :param parent_table_name:
        :param child_table_name:
        :param cols_values: A dictionary contains two key 'parent_table_values' and 'child_table_values',
        :param parent_table_col: The parent table column name in the child table (The foreign key column)
        then the function extracts the parent and child data from the dictionary
        :return:
        """
        parent_table_data = cols_values.pop('parent_table')
        child_table_data = cols_values.pop('child_table')
        self.set_table_name(parent_table_name)
        parent_table_id = self.save(parent_table_data)
        if parent_table_id:
            child_table_data[parent_table_col] = parent_table_id
            self.set_table_name(child_table_name)
            return self.save(child_table_data)
        return

    def save(self, cols_values):
        if self.validate_mandatory_widgets():
            query = QSqlQuery()
            query.prepare(self.build_insert_query(cols_values.keys()))
            self.bind_values(query, cols_values)
            query.exec_()
            errors = query.lastError().text()
            print("Error: ", errors) if errors else print('Success')
            return query.lastInsertId() if not errors else None
        return

    def bind_values(self, query, values):
        [query.bindValue(f':{value}', values[value]) for value in values.keys()]

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                           "Are you sure you want to exit the program?", QMessageBox.Yes, QMessageBox.No)
        event.accept() if reply == QMessageBox.Yes else event.ignore()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CreateForm()
    sys.exit(app.exec_())

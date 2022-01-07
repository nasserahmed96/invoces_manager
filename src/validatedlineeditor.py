from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtCore import pyqtSignal


class ValidatedLineEditor(QLineEdit):

    def __init__(self, parent):
        super().__init__(parent=parent)
        self.is_mandatory_field = False
        self.is_valid_input = True if self.allowed_empty() else False
        self.is_unique = False
        #Corresponding column name in the database
        self.column_name = ''
        self.table_name = ''
        #Last error presented by different functions in the field, this can be used to retrieve
        self.last_error = ''
        self.label = None

    def get_column_name(self):
        return self.column_name

    def set_database_attributes(self, column_name, table_name):
        self.table_name = table_name
        self.column_name = column_name

    def set_label(self, label):
        self.label = label

    def set_column_name(self, column_name):
        self.column_name = column_name

    def set_table_name(self, table_name):
        self.table_name = table_name

    def get_table_name(self):
        return self.table_name

    def get_last_error(self):
        return self.last_error

    def is_valid(self):
        return self.is_valid_input

    def set_unique(self, unique=True):
        self.is_unique = unique

    def focusInEvent(self, event):
        super(ValidatedLineEditor, self).focusInEvent(event)
        self.setStyleSheet("")

    def focusOutEvent(self, event):
        """
        First check if the widget has a validator assigned to it, then check if it's not mandatory empty and also an
        empty to ignore false warnings OR it's a mandatory so check if it has a valid input
        :param event:
        :return:
        """
        if not self.allowed_empty() and self.valid_text() and not self.is_duplicate():
            self.valid_input()
        super(ValidatedLineEditor, self).focusOutEvent(event)

    def valid_text(self):
        """
        Check if the current text in the field are valid according to the field's validator or not
        :return: True if it's a valid input, False instead
        """
        if self.validator() and self.validator().validate(self.text(), 0)[0] == self.validator().Acceptable:
            return True
        if self.text() != '':
            self.raise_error('You have entered a wrong text, please enter a valid text')
            return False

    def allowed_empty(self):
        """
        Check if this field is allowed to be empty or not
        :return: True if it's allowed to be empty False instead
        """
        if not self.is_mandatory_field and self.text() == "":
            return True
        elif self.is_mandatory_field and self.text() == "":
            self.raise_error("This field can't be empty")
            return False
        return False

    def valid_input(self):
        self.is_valid_input = True
        self.setStyleSheet('')
        self.last_error = ''
        self.label.setText('')

    def raise_error(self, msg):
        self.is_valid_input = False
        self.setStyleSheet(f"{type(self).__name__} {{border: 2px solid red}}")
        self.last_error = msg
        self.label.setText(self.last_error)

    def set_mandatory(self, mandatory=True):
        self.is_mandatory_field = mandatory

    def is_mandatory(self):
        return self.is_mandatory_field

    def get_validation_confirm(self):
        return self.validation_confirmed if self.validation_confirmed else False

    def is_duplicate(self):
        """
        Check if the column name with column value exists in table name
        :param table_name:
        :param column_name:
        :param column_value:
        :return: True if the value exists in DB False instead
        """
        if self.is_unique:
            query = QSqlQuery()
            query.prepare(f"SELECT {self.column_name} FROM {self.table_name} WHERE {self.column_name}=:column_value")
            query.bindValue(':column_value', self.text())
            query.exec_()
            if query and query.first():
                self.raise_error(msg=f'There is already a field with the same {self.placeholderText()}, please choose a different one')
                return True
            self.last_error = 'Your input is correct, go to next step'
            return False

import sys
import re
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtSql import QSqlQuery
from python_forms.employees_manager_GUI import Ui_employee_management_window
from src.Models.EmployeesTableModel import EmployeesTableModel

from create_employee import CreateEmployee
from src.EmployeeProfile import EmployeeProfile


class EmployeesManager(QMainWindow):
    def __init__(self):
        super(EmployeesManager, self).__init__()
        self.ui = Ui_employee_management_window()
        self.ui.setupUi(self)
        self.model = EmployeesTableModel()
        self.connect_signals_slots()
        self.initializeUI()

    def connect_signals_slots(self):
        self.ui.add_employee_btn.clicked.connect(self.open_create_employee)
        self.ui.search_employee_btn.clicked.connect(self.search)
        self.ui.employees_table_view.doubleClicked.connect(self.open_employee_profile)

    def open_employee_profile(self):
        print('Employee profile')
        idx = self.ui.employees_table_view.selectionModel().selectedIndexes()[0]
        print('Employee ID ', self.model.index(idx.row(), 0).data())
        employee_profile = EmployeeProfile(self.model.index(idx.row(), 0).data(), self)
        employee_profile.show()


    def build_conditions(self, conditions):
        """
        This function builds conditions for the SELECT query, based on whether the required widget has something in it
        or not
        :return:
        """
        return ' WHERE ' + ' '.join([self.get_condition_string(condition) for condition in conditions]) if any(conditions) else ""

    def search(self):
        conditions = []
        conditions.append(
            self.build_condition('employees.username', self.ui.username_line_edit.text(), '=', 'COLLATE NOCASE', 'AND')
        ) if self.ui.username_line_edit.text() != '' else None
        conditions.append(
            self.build_condition('users.email', self.ui.email_line_edit.text(), '=', 'COLLATE NOCASE', 'AND')
        ) if self.ui.email_line_edit.text() != '' else None
        conditions.append(
            self.build_condition('users.phone_number', self.ui.phone_number_line_edit.text(), '=', 'COLLATE NOCASE', 'AND')
        ) if self.ui.phone_number_line_edit.text() != '' else None
        conditions.extend(self.search_by_name()) if self.ui.name_line_edit.text() != '' else None
        self.model.select(re.sub('(AND|OR)$', '', self.build_conditions(conditions)), self.extract_values_from_conditions(conditions))
        self.ui.employees_table_view.update()

    def build_condition(self, column, value, operator, options='', logic=''):
        return {
            'column': column,
            'value': value,
            'operator': operator,
            'options': options,
            'logic': logic
        }

    def extract_values_from_conditions(self, conditions):
        placeholder = dict()
        for condition in conditions:
            placeholder[condition['column'].replace('.', '_')] = condition['value']
        return placeholder

    def search_by_name(self):
        name_array = self.ui.name_line_edit.text().split(' ')
        name_array_length = len(name_array)
        result = ''
        if name_array_length == 1:
            result = [
                self.build_condition('users.first_name', name_array[name_array_length - 1], '=', 'COLLATE NOCASE', 'OR'),
                self.build_condition('users.middle_name', name_array[name_array_length - 1], '=', 'COLLATE NOCASE', 'OR'),
                self.build_condition('users.last_name', name_array[name_array_length - 1],'=', 'COLLATE NOCASE')
            ]
        elif name_array_length == 2:
            result = [
                self.build_condition('users.first_name', name_array[name_array_length - 2], '=', 'COLLATE NOCASE', 'AND'),
                self.build_condition('users.middle_name', name_array[name_array_length - 1], '=', 'COLLATE NOCASE', 'OR'),
                self.build_condition('users.last_name', name_array[name_array_length - 1], '=', 'COLLATE NOCASE')
            ]
        elif name_array_length == 3:
            result = [
                self.build_condition('users.first_name', name_array[name_array_length - 3], '=', 'COLLATE NOCASE', 'AND'),
                self.build_condition('users.middle_name', name_array[name_array_length - 2], '=', 'COLLATE NOCASE', 'AND'),
                self.build_condition('users.last_name', name_array[name_array_length - 1], '=', 'COLLATE NOCASE',)
            ]
        return result

    def get_condition_string(self, condition):
        """
        Get a condition string out of a condition object
        :param condition: A condition object contains the required parameters for the condition
        :return: A condition string to be used in SQL query
        """
        return f"{condition['column']} {condition['operator']} :{condition['column'].replace('.', '_')} {condition['options']} {condition['logic']}"

    def execute_select_query(self, query_str):
        query = QSqlQuery()
        query.exec_(query_str)
        return query

    def open_create_employee(self):
        create_employee = CreateEmployee(self)
        create_employee.show()

    def initializeUI(self):
        self.setupTable()

    def setupTable(self):
        self.ui.employees_table_view.setModel(self.model)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmployeesManager()
    window.show()
    sys.exit(app.exec_())
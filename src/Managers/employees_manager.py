import sys
import re
from PyQt5.QtWidgets import QApplication
from python_forms.employees_manager_GUI import Ui_employee_management_window
from src.Managers.base_manager import BaseManager
from src.Models.EmployeesTableModel import EmployeesTableModel
from src.create_employee import CreateEmployee
from src.EmployeeProfile import EmployeeProfile


class EmployeesManager(BaseManager):
    def __init__(self, parent=None):
        super(EmployeesManager, self).__init__(parent=parent, ui=Ui_employee_management_window(), model=EmployeesTableModel())

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

    def open_create_employee(self):
        create_employee = CreateEmployee(self)
        create_employee.show()

    def setup_table(self):
        print('Child setup table')
        self.ui.employees_table_view.setModel(self.model)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmployeesManager()
    window.show()
    sys.exit(app.exec_())